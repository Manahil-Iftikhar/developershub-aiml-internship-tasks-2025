# Local datasets

Place original CSV files here when a task requires them. Dataset contents are excluded from version control; document their source, license, version/date, and SHA-256 hash in experiment results. The repository does not redistribute the missing external datasets.

Read the individual project pages for required filenames and targets. The advanced churn task generates explicitly synthetic rows and requires no external CSV. `sample-knowledge-base.txt`, where present, is demonstration text supplied with the repository.

For the maintained UCI Cleveland case study, use `python -m portfolio.heart --download` from the repository root. This fetches and hash-checks `processed.cleveland.data`. See [provenance and license](../docs/projects/03-heart-disease.md); it is a separate dataset from the original internship CSV.
