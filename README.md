# acme-metaflow

Shows how metaflow can be used to orchestrate python programs.

View `/tutorials`.

## Dev environment

The project comes with a python development environment.
To generate it, after checking out the repo run:

    chmod +x create_env.sh

Then to generate the environment (or update it to latest version based on state of `uv.lock`), run:

    ./create_env.sh

This will generate a new python virtual env under `.venv` directory. You can activate it via:

    source .venv/bin/activate

If you are using VSCode, set to use this env via `Python: Select Interpreter` command.

## Dev deployment

See details in `tutorials/12-configure-k8-metadata-service`

## Project template

This project has been setup with `acme-project-create`, a python code template library.

## Required setup post use

* Enable GitHub Pages to be published via [GitHub Actions](https://docs.github.com/en/pages/getting-started-with-github-pages/configuring-a-publishing-source-for-your-github-pages-site#publishing-with-a-custom-github-actions-workflow)
* Create `release` environment for [GitHub Actions](https://docs.github.com/en/actions/managing-workflow-runs-and-deployments/managing-deployments/managing-environments-for-deployment#creating-an-environment)
* Setup auth to PyPI for the GitHub Action implemented in release.yml: [Link](https://docs.pypi.org/trusted-publishers/adding-a-publisher/) uv publish [doc](https://docs.astral.sh/uv/guides/publish/#publishing-your-package)
