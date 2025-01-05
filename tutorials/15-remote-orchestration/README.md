# Episode 15-remote-orchestration

**We use Argo Worflows as an orchestrator for Metaflow Flows**

#### Showcasing:
- `argo-workflows create` command line option
- `argo-workflows trigger` command line option
- Use `project` decorator to create distinct namespaces for results.

#### To play this episode:
`cd tutorials`
`python 15-remote-orchestration/hello-cloud.py --with retry argo-workflows create`
`python 15-remote-orchestration/hello-cloud.py --with retry argo-workflows trigger`