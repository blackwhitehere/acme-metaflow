# acme-metaflow

Shows how metaflow can be used to orchestrate python programs.

View `/tutorials`.

# Project template

This project has been setup with `acme-project-create`, a python code template library.

# Required setup post use

* Enable GitHub Pages to be published via [GitHub Actions](https://docs.github.com/en/pages/getting-started-with-github-pages/configuring-a-publishing-source-for-your-github-pages-site#publishing-with-a-custom-github-actions-workflow)
* Create `release` environment for [GitHub Actions](https://docs.github.com/en/actions/managing-workflow-runs-and-deployments/managing-deployments/managing-environments-for-deployment#creating-an-environment)
* Setup auth to PyPI for the GitHub Action implemented in release.yml: [Link](https://docs.pypi.org/trusted-publishers/adding-a-publisher/) uv publish [doc](https://docs.astral.sh/uv/guides/publish/#publishing-your-package)