# Health information chatbot

**Assignment task 4 · Manahil Iftikhar**

Prompt design with a pretrained text model.

[Maintained notebook](../../notebooks/04-health-chatbot.ipynb) · [Original submission](../../archive/Task%204%20-%20General%20Health%20Query%20Chatbot%20%28Prompt.ipynb) · [Portfolio](../../README.md)

## Current state

Model download required; responses need evaluation.

## Data and model provenance

Original checkpoint: google/flan-t5-large. The maintained example uses google/flan-t5-small to reduce setup requirements. No clinical dataset or validated evaluation set was supplied.

## Evidence in the original submission

The archive contains sample conversations, including incorrect answers. There is no verified medical-accuracy result. Changing the prompt or checkpoint does not establish safety or factual accuracy.

These statements describe source and saved outputs from the original commit `725186ed2c34`. They are not fresh benchmark measurements.

## Improvements and remaining work

Evaluate an explicit set of questions and refusal cases before publishing a public health demo. Prompts alone do not enforce response safety.

## Reproduce

Follow the [VS Code setup](../SETUP.md), open the maintained notebook, and select the installed environment. Supply the data described above where required. The [verification record](../VERIFICATION.md) distinguishes executed checks from workflows requiring external assets.

## Questions to answer in the next experiment

- What baseline is the method compared against?
- Does the evaluation split represent the intended use?
- Which errors remain, and what evidence explains them?
- Can another person reproduce the result from the documented data and settings?
