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

The GitHub Actions workflow runs the offline checks above when GitHub enables it. Local success does not by itself establish a successful hosted CI run. Historical task scores remain identified in the individual project pages.
