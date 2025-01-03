# Episode 13-remote-compute

#### Pre-requisites

1. Follow tutorial `12-configure-k8-metadata-service` to setup k8 cluster and metadata service.

#### Showcasing:

- `@resources` decorator to define resource requirements
- `@kubernetes` decorator to force step to execute on k8
- `--with kubernetes` command line option to execute all steps on k8
- `--max-workers` command line option to limit number of pods

`cd tutorials`
to run just one step in k8:
`python 13-remote-compute/hello-cloud.py run`
to run all sets in k8:
`python 13-remote-compute/hello-cloud.py run --with kubernetes`