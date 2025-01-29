# Episode 15-remote-orchestration

**We use Argo Worflows as an orchestrator for Metaflow Flows**

#### Showcasing:
- `argo-workflows create` command line option to create a new flow on remore orchestrator
- `argo-workflows trigger` command line option to start a flow on remote orchestrator
- Use `project` decorator to create distinct namespaces for results.

#### To play this episode:
`cd tutorials`
`python 15-remote-orchestration/hello-cloud.py --with retry --with kubernetes --production argo-workflows create`
`python 15-remote-orchestration/hello-cloud.py --with retry --with kubernetes --production --branch experiment argo-workflows create`
`python 15-remote-orchestration/hello-cloud.py --with retry --with kubernetes argo-workflows create`
`python 15-remote-orchestration/hello-cloud.py --with retry argo-workflows trigger`