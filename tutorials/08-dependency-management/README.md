# Episode 08-dependency-management

**Shows Metaflow's environment and package management features**

More info at [Link](https://docs.metaflow.org/scaling/dependencies)


#### Showcasing:
- Metaflow can run each step in a distinct python environment. This is activated by passing `--environment=<pypi/conda>` on flow CLI to indiacte which type of environment to use (venv or conda).
- Ability to define exact library versions to install in those environment with `pypi_base`/`conda_base` and `pypi`/`conda` decorators.
- Metaflow automatically packages python packages & modules in the flow's directory and installs them in the steps' envrionments.
- When dependency management decorators are not used (or `disabled=True` kwarg is used) the host python environment is used.

#### Notes:
 
 - Metaflow creates the environments when flows are run. This makes a run less stable as it can run into a build issue. To avoid is, depend on host environment which in production should have the right dependencies installed.
 - Specifying the version of a used library in a step (e.g. pandas `1.5.3`) is alone not enough to make the environment stable as transient dependencies also need to be included in the list.
 - Sharable code across flows should be maintained as a distinct library in `/src`. Those can be published to `PyPi` or a private artifact repository, but don't need to as they can be just built into host environment in production.


#### To play this episode:
1. ```cd tutorials```
1. ```python 08-dependency-management/dependency_flow.py --environment=conda run```
1. ```python 08-dependency-management/dependency_flow.py --environment=conda package list```
