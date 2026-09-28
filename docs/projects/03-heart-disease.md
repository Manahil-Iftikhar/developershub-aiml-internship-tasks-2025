# Heart disease classification

**Assignment task 3 · Manahil Iftikhar**

[Maintained notebook](../../notebooks/03-heart-disease.ipynb) · [Original submission](../../archive/Task%203%20-%20Heart%20Disease%20Prediction.ipynb) · [Portfolio](../../README.md)

## Current state

A reproducible educational experiment now runs on the UCI processed Cleveland dataset. This is a **new, separately sourced case study**, not a reconstruction of the original internship dataset. It is not a diagnostic or future-risk prediction tool.

## Source and attribution

Dataset: **Heart Disease**, Andras Janosi, William Steinbrunn, Matthias Pfisterer and Robert Detrano (1989), UCI Machine Learning Repository, [DOI 10.24432/C52P4X](https://doi.org/10.24432/C52P4X). UCI lists the dataset under [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/).

[Dataset page and variable dictionary](https://archive.ics.uci.edu/dataset/45/heart+disease) · [Source archive](https://archive.ics.uci.edu/static/public/45/heart+disease.zip)

The experiment uses only `processed.cleveland.data`: 303 rows and 13 predictors. It maps the original `num` value 0 to class 0 and values 1–4 to class 1. These transformations, categorical encoding, and missing-value handling are portfolio modifications. The raw source remains outside version control; the adapted evaluation report and predictions retain this attribution.

Expected raw-file SHA-256:

```text
a74b7efa387bc9d108d7d0115d831fe9b414b29ae7124f331b622b4efa0427c8
```

The downloader verifies this hash and refuses changed source bytes. The parser checks schema, category codes and target values. `?` marks missing values: four in `ca` and two in `thal`. Categorical codes are encoded as categories; the numeric vessel count remains numeric. Numeric imputation and scaling are fitted inside each training pipeline; missing categorical values receive an explicit category.

## Experiment design

Seed 42 stratified splits: **181 training / 61 validation / 61 test rows**. No rows were removed as exact duplicates or missing targets. Candidate models are a class-prior dummy baseline, logistic regression, and a random forest. The shared pipeline selects by validation ROC-AUC, refits the selected model on training plus validation rows, then evaluates once on the untouched test partition. It does not tune a decision threshold on the test set.

## Measured portfolio run · September 29, 2026

| Model | Test accuracy | Class-1 F1 | Test ROC-AUC |
| --- | ---: | ---: | ---: |
| Class-prior baseline | 0.5410 | 0.0000 | 0.5000 |
| Selected logistic regression | 0.8689 | 0.8667 | 0.9578 |

The confusion matrix uses rows = actual class and columns = predicted class:

| | Predicted 0 | Predicted 1 |
| --- | ---: | ---: |
| Actual 0 | 27 | 6 |
| Actual 1 | 2 | 26 |

There are **2 false negatives and 6 false positives** among 61 test examples. [Full metrics](../../reports/heart-cleveland/metrics.json) record validation scores, source identity, missing values, feature columns and package versions. [Held-out predictions](../../reports/heart-cleveland/predictions.csv) identify source rows by zero-based index; no direct identifiers are added.

## Reproduce

From the repository root, in the environment described in [VS Code setup](../SETUP.md):

```bash
python -m pip install -r requirements.txt
python -m portfolio.heart --download
python -m unittest discover -s tests -v
```

The download flag explicitly fetches UCI data. Later runs can omit it. Outputs go to `artifacts/heart-cleveland/`; use `--output` to choose another directory. Once downloaded, the maintained notebook runs offline. It includes a confusion-matrix visualization, and its committed outputs remain cleared.

## Limitations and next experiment

This is one small, historical, single-site random holdout. Its score does not establish transportability, calibration, fairness, clinical utility, or performance on contemporary populations. Some predictors require clinical tests; this is not a symptoms-only screening system. No prospective or external-site evaluation was performed. Further model or threshold choices require fresh evaluation data rather than repeated optimization on this test set.

## Original internship evidence

The archived submission used `HeartDiseaseTrain-Test.csv`, described as 1,025 rows and 14 columns; its exact source was not recorded. Saved original outputs report accuracy 0.7902, ROC-AUC 0.8654 and confusion matrix [[76, 26], [17, 86]]. Those historical scores are preserved separately and are **not directly comparable** to this Cleveland experiment. Original source commit: `725186ed2c34`.
