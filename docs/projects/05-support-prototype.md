# Support chatbot prototype

**Assignment task 5 · Manahil Iftikhar**

Inspection of pretrained causal-language-model inference.

[Maintained notebook](../../notebooks/05-support-prototype.ipynb) · [Original submission](../../archive/Task%205%20-%20Mental%20Health%20Support%20Chatbot%20%28Fine-Tuned%29.ipynb) · [Portfolio](../../README.md)

## Current state

Inference prototype; fine-tuning remains to be implemented.

## Data and model provenance

tiiuae/falcon-rw-1b. The submitted source loads the pretrained checkpoint and generates replies; no training dataset, optimizer, trainer, or updated weights are present.

## Evidence in the original submission

No fine-tuning result is established by the submitted notebook. The original assignment title is retained here to make the project traceable.

These statements describe source and saved outputs from the original commit `725186ed2c34`. They are not fresh benchmark measurements.

## Improvements and remaining work

Complete the assignment with an appropriately sourced conversation dataset, a reproducible training script, held-out evaluation, and a base-versus-tuned comparison. Current code is not a mental-health service.

## Reproduce

Follow the [VS Code setup](../SETUP.md), open the maintained notebook, and select the installed environment. Supply the data described above where required. The [verification record](../VERIFICATION.md) distinguishes executed checks from workflows requiring external assets.

## Questions to answer in the next experiment

- What baseline is the method compared against?
- Does the evaluation split represent the intended use?
- Which errors remain, and what evidence explains them?
- Can another person reproduce the result from the documented data and settings?
