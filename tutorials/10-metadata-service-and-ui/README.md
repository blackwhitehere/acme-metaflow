# Episode 10-metadata-service-and-ui

**Shows how to use a common metadata provider and view flows in Metaflow UI**

In `05-access-results` recall that we relied on a metadata provider to provide information about stored flow runs.
In that tutorial the metadata provider was provided by a local file system.
However, if we'd like to collaborate with other people on the flows metaflow provides a shared metadata provider implemented as a service.

#### Showcasing:

- Setting up a localy running instance of Metaflow Provider service
- Setting up Metaflow UI that uses the Metaflow Provider service
- Viewing flow output in Metaflow UI

#### To play this episode:
1. In your main source code directory (e.g. `src`) run `git clone https://github.com/Netflix/metaflow-service`
1. In the `metaflow-service` dir run `docker-compose -f docker-compose.development.yml up`
1. In your main source code directory (e.g. `src`) run `git clone https://github.com/Netflix/metaflow-ui`
1. In the `metaflow-ui` dir run `docker build --tag metaflow-ui:latest .`
1. In the `metaflow-ui` dir run `docker run -p 3000:3000 -e METAFLOW_SERVICE=http://localhost:8083/ metaflow-ui:latest`
1. In `tutorials` dir run `METAFLOW_SERVICE_URL=http://localhost:8080 METAFLOW_DEFAULT_METADATA="service" python 00-helloworld/helloworld.py run`
1. Navigate to `localhost:3000` to see Metaflow UI

# TODO: Local datastore is not well supported by the remote metadata service and UI so we can't access some artifacts data saved to local store (e.g. DAG graph)
