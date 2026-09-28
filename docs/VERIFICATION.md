# Verification record

Portfolio maintenance: 2026-09-24.

Validated locally with Python 3.12.14 and the pinned core environment in `requirements.txt`.

| Check | Observed result |
| --- | --- |
| Repository validation | Passed: six maintained notebooks, local Markdown links, Python syntax, cover SVG, and six original notebook blob hashes |
| Focused offline tests | 10 passed |
| Iris notebook | Every code cell executed successfully in order with a shared namespace and a noninteractive plotting backend |
| Original submissions | All six archived notebook contents match their original Git blob SHA |

The tests cover fitted preprocessing, unseen categories, input validation, model serialization, stock-date ordering, and the gap between training labels and later evaluation inputs. They use small synthetic fixtures to check behavior; their scores are not portfolio benchmarks.

The [Iris figure](../assets/iris-petals.svg) is generated from the bundled 150-row dataset. Rebuild it with `python tools/render_iris.py`.

## Repeat the checks

```bash
python -m pip install -r requirements.txt
python tools/check_workspace.py
python -m unittest discover -s tests -v
```

Open `notebooks/01-iris-exploration.ipynb` in VS Code to rerun the exploration interactively. Notebook outputs remain cleared in version control; the README figure provides a compact recorded visual result.

## Execution limits

The stock workflow has offline behavior tests; it has not been rerun against a downloaded market dataset during this maintenance. The heart-disease and house-price datasets were absent, so those full task runs remain pending. The health and support language models were not downloaded or executed. Their maintained notebooks were checked for Python syntax only, and no model-quality or medical-reliability claim follows from these checks.

Historical task scores remain identified in the individual project pages.

## Hosted CI evidence

[GitHub Actions run 36143467044](https://github.com/Manahil-Iftikhar/developershub-aiml-internship-tasks-2025/actions/runs/36143467044) completed successfully on **September 25, 2026**, for commit `16ff782d60d2f393f79d1001b3bf300f377bbbc5`. It used Python 3.12 and installed the pinned core requirements. Repository validation and focused offline test steps both passed.

The [workflow](../.github/workflows/checks.yml) runs `python tools/check_workspace.py` and `python -m unittest discover -s tests -v` on pushes and pull requests. It does not execute all notebook cells, download market data or model weights, or evaluate medical response quality. The local Iris execution above is separate evidence, not a notebook run performed by CI.

