# Run locally in VS Code

Use Python 3.11 or 3.12. Start in the repository root after cloning `developershub-aiml-internship-tasks-2025`.

## Create and select an environment

```bash
python -m venv .venv
```

Windows PowerShell:

```powershell
.venv\Scripts\Activate.ps1
```

Windows Command Prompt:

```bat
.venv\Scripts\activate.bat
```

macOS/Linux:

```bash
source .venv/bin/activate
```

```bash
python -m pip install -r requirements-notebook.txt
```

Install the Python and Jupyter VS Code extensions. Open a file in `notebooks/`, choose **Select Kernel**, and select `.venv`. Run cells in order. Model training can require substantial memory and time; the README of each task documents the evidence and remaining requirements.

## Lightweight checks

```bash
python tools/check_workspace.py
python -m unittest discover -s tests -v
```

These checks exercise repository structure and small fixtures. They do not download datasets, validate model-generated health advice, train BERT, or establish real-world model quality.

## Reusable tabular runner

```bash
python -m portfolio.tabular --help
```

The runner requires a CSV, target column, task type, and explicit `--data-kind external` or `--data-kind synthetic`. It writes `metrics.json`, `predictions.csv`, and `model.joblib` under the chosen output directory. The JSON records the data hash, package versions, split sizes, baseline, validation selection, and final test metrics.

Only load joblib/pickle artifacts you trust. Keep downloaded datasets, local models, and credentials out of Git commits.

## Additional environments

```bash
python -m pip install -r requirements-llm.txt
```

These pins follow versions recorded in the original model notebooks where available. The complete model environment was not installed or executed during portfolio maintenance. The first model run needs network access and disk space for public checkpoints. Use a separate environment if your hardware requires a different PyTorch build.

## Data and reproduction limits

External dataset files used in the original submissions were not committed. Supply the original files and record their exact source/version before reporting new benchmark results. The original notebooks remain in `archive/`; the maintained notebooks have cleared outputs so stale results cannot be mistaken for a fresh run.

## House price example

Place the original CSV in `data/`, then run:

```bash
python -m portfolio.tabular --csv "data/House Price Prediction Dataset.csv" --target Price --task regression --data-kind external --output artifacts/house-prices
```

For heart disease, use `--csv data/HeartDiseaseTrain-Test.csv --target target --task classification`.

For stock downloads, install `requirements-stocks.txt` and explicitly enable the download switch in the stock notebook. Otherwise supply a local CSV with a Date column and OHLCV prices.
