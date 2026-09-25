# House price regression

**Assignment task 6 · Manahil Iftikhar**

Tabular regression with reproducible preprocessing.

[Maintained notebook](../../notebooks/06-house-prices.ipynb) · [Original submission](../../archive/Task%206%20-%20House%20Price%20Prediction.ipynb) · [Portfolio](../../README.md)

## Current state

Original CSV required; pipeline tested with synthetic fixtures.

## Data and model provenance

House Price Prediction Dataset.csv with Price, Area, Bedrooms, Bathrooms, Floors, YearBuilt, Location, Condition, and Garage. The source and currency were not recorded; Id is excluded from modelling.

## Evidence in the original submission

Saved original outputs: MAE 237,415.30 and RMSE 279,721.23 in dataset price units. The original scaled features before splitting and included Id. These outputs are not validated scores for the maintained version.

These statements describe source and saved outputs from the original commit `725186ed2c34`. They are not fresh benchmark measurements.

## Improvements and remaining work

The new runner separates train, validation, and test data, fits preprocessing inside each pipeline, compares a median baseline with Ridge and Random Forest, and exports measured results.

## Reproduce

Follow the [VS Code setup](../SETUP.md), open the maintained notebook, and select the installed environment. Supply the data described above where required. The [verification record](../VERIFICATION.md) distinguishes executed checks from workflows requiring external assets.

## Questions to answer in the next experiment

- What baseline is the method compared against?
- Does the evaluation split represent the intended use?
- Which errors remain, and what evidence explains them?
- Can another person reproduce the result from the documented data and settings?
