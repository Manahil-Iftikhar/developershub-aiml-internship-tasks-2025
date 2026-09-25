# Stock forecasting

**Assignment task 2 · Manahil Iftikhar**

Next-session regression and chronological evaluation.

[Maintained notebook](../../notebooks/02-stock-forecasting.ipynb) · [Original submission](../../archive/Task%202%20-%20%20Predict%20Future%20Stock%20Prices%20%28Short-Term%29.ipynb) · [Portfolio](../../README.md)

## Current state

Local CSV or an explicit Yahoo Finance download required.

## Data and model provenance

Original: TSLA OHLCV from Yahoo Finance, 2020-01-01 through 2024-01-01 (end exclusive). Downloaded prices may change after vendor adjustments.

## Evidence in the original submission

Saved original outputs: linear regression R² 0.9545 / MSE 55.56; random forest R² 0.9319 / MSE 83.19. These are historical notebook outputs, not rerun results or evidence of profitable trading.

These statements describe source and saved outputs from the original commit `725186ed2c34`. They are not fresh benchmark measurements.

## Improvements and remaining work

The maintained version adds a persistence baseline, validation-based selection, date labels, and one-session gaps so training targets precede evaluation inputs.

## Reproduce

Follow the [VS Code setup](../SETUP.md), open the maintained notebook, and select the installed environment. Supply the data described above where required. The [verification record](../VERIFICATION.md) distinguishes executed checks from workflows requiring external assets.

## Questions to answer in the next experiment

- What baseline is the method compared against?
- Does the evaluation split represent the intended use?
- Which errors remain, and what evidence explains them?
- Can another person reproduce the result from the documented data and settings?
