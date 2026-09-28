"""Reproduce an educational classification experiment on UCI Cleveland data.

Download is explicit; no network requests or training occur during import.
"""
from __future__ import annotations

import argparse
import hashlib
import importlib.metadata
import io
import json
from pathlib import Path
from urllib.request import urlopen
import zipfile

import numpy as np
import pandas as pd

from portfolio.tabular import train

SOURCE_URL = 'https://archive.ics.uci.edu/static/public/45/heart+disease.zip'
SOURCE_PAGE = 'https://archive.ics.uci.edu/dataset/45/heart+disease'
RAW_SHA256 = 'a74b7efa387bc9d108d7d0115d831fe9b414b29ae7124f331b622b4efa0427c8'
COLUMNS = ['age', 'sex', 'cp', 'trestbps', 'chol', 'fbs', 'restecg',
           'thalach', 'exang', 'oldpeak', 'slope', 'ca', 'thal', 'num']
CATEGORIES = {'sex': {0, 1}, 'cp': {1, 2, 3, 4}, 'fbs': {0, 1},
              'restecg': {0, 1, 2}, 'exang': {0, 1},
              'slope': {1, 2, 3}, 'thal': {3, 6, 7}}


def parse_cleveland(raw):
    frame = pd.read_csv(io.BytesIO(raw), header=None, na_values='?')
    if frame.shape[1] != len(COLUMNS):
        raise ValueError('Expected 14 columns in processed Cleveland data.')
    frame.columns = COLUMNS
    frame = frame.apply(pd.to_numeric, errors='raise')
    if np.isinf(frame.to_numpy()).any():
        raise ValueError('Infinite values are not valid.')
    if frame['num'].isna().any() or not frame['num'].isin(range(5)).all():
        raise ValueError('Target num must contain integer codes 0 through 4.')
    missing = frame.isna().sum().astype(int).to_dict()
    # Preserve categorical meaning instead of treating integer codes as distances.
    for column, allowed in CATEGORIES.items():
        if not frame[column].dropna().isin(allowed).all():
            raise ValueError(f'Unknown category in {column}.')
        frame[column] = frame[column].map(
            lambda value: 'missing' if pd.isna(value) else f'code_{int(value)}')
    frame['target'] = (frame.pop('num') > 0).astype(int)
    return frame, missing


def load_cleveland(path):
    raw = Path(path).read_bytes()
    if hashlib.sha256(raw).hexdigest() != RAW_SHA256:
        raise ValueError('Dataset SHA-256 differs from the reviewed UCI source.')
    return parse_cleveland(raw)


def download_cleveland(path):
    path = Path(path)
    if path.exists():
        load_cleveland(path)
        return
    with urlopen(SOURCE_URL, timeout=60) as response:
        archive = response.read(2_000_001)
    if len(archive) > 2_000_000:
        raise ValueError('Unexpectedly large dataset archive.')
    with zipfile.ZipFile(io.BytesIO(archive)) as bundle:
        raw = bundle.read('processed.cleveland.data')
    if hashlib.sha256(raw).hexdigest() != RAW_SHA256:
        raise ValueError('Downloaded data differs from the reviewed source.')
    parse_cleveland(raw)
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_bytes(raw)


def run(path, output):
    frame, missing = load_cleveland(path)
    _, report, predictions = train(frame, 'target', 'classification', seed=42)
    report['dataset'] = {
        'name': 'UCI Heart Disease, processed Cleveland subset',
        'source': SOURCE_PAGE, 'download': SOURCE_URL,
        'doi': '10.24432/C52P4X', 'license': 'CC BY 4.0',
        'filename': 'processed.cleveland.data', 'sha256': RAW_SHA256,
        'rows': len(frame), 'missing_before_preprocessing': missing,
        'target_mapping': 'num 0 -> 0; num 1,2,3,4 -> 1',
        'categorical_columns': list(CATEGORIES),
        'class_counts': {str(k): int(v) for k, v in frame.target.value_counts().items()},
    }
    report['environment'] = {name: importlib.metadata.version(name)
                             for name in ['numpy', 'pandas', 'scikit-learn', 'joblib']}
    report['limitations'] = (
        'Educational retrospective classification, not future-risk prediction or diagnosis. '
        'Small historical single-site sample; one seed and random stratified holdout. '
        'No external validation, calibration, subgroup evaluation or clinical utility study. '
        'Some predictors require clinical tests; this is not a symptoms-only screening model. '
        'The original internship CSV is different and its scores are not directly comparable.')
    output = Path(output)
    output.mkdir(parents=True, exist_ok=True)
    (output / 'metrics.json').write_text(json.dumps(report, indent=2) + '\n')
    predictions.to_csv(output / 'predictions.csv', index=False)
    return report


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--data', type=Path, default=Path('data/processed.cleveland.data'))
    parser.add_argument('--download', action='store_true')
    parser.add_argument('--output', type=Path, default=Path('artifacts/heart-cleveland'))
    args = parser.parse_args()
    if args.download:
        download_cleveland(args.data)
    report = run(args.data, args.output)
    print(json.dumps({'selected_model': report['selected_model'],
                      'rows': report['rows'], 'test': report['test']}, indent=2))


if __name__ == '__main__':
    main()
