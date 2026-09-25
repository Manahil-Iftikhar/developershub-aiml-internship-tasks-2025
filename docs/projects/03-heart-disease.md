# Heart disease classification

**Assignment task 3 · Manahil Iftikhar**

Binary classification and error analysis.

[Maintained notebook](../../notebooks/03-heart-disease.ipynb) · [Original submission](../../archive/Task%203%20-%20Heart%20Disease%20Prediction.ipynb) · [Portfolio](../../README.md)

## Current state

Original CSV required.

## Data and model provenance

HeartDiseaseTrain-Test.csv with a binary target column named target. The original output describes 1,025 rows and 14 columns. Its exact download source was not recorded.

## Evidence in the original submission

Saved original outputs: accuracy 0.7902, ROC-AUC 0.8654, confusion matrix [[76, 26], [17, 86]]. The maintained pipeline changes preprocessing and splitting, so these are not scores for the new code.

These statements describe source and saved outputs from the original commit `725186ed2c34`. They are not fresh benchmark measurements.

## Improvements and remaining work

The maintained workflow uses training-only imputation and encoding, stratified splits, and a dummy baseline. It is an educational classification exercise, not a diagnostic tool.

## Reproduce

Follow the [VS Code setup](../SETUP.md), open the maintained notebook, and select the installed environment. Supply the data described above where required. The [verification record](../VERIFICATION.md) distinguishes executed checks from workflows requiring external assets.

## Questions to answer in the next experiment

- What baseline is the method compared against?
- Does the evaluation split represent the intended use?
- Which errors remain, and what evidence explains them?
- Can another person reproduce the result from the documented data and settings?
