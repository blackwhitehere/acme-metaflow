
# Episode 12-configure-k8-metadata-service

#### Shows how to setup metaflow metadata service on local k8 cluster

#### Pre-requisites

1. Running postgres DB
1. Minikube installation with 4GB of memory


#### To start local K8 cluster

See setup in dir `infra/k8` for Kubernetes deployment setup:

    # Start minikube
    minikube start --memory=3933
    kubectl config use-context minikube
    # set env vars in /infra/k8/db.env file: MF_METADATA_DB_PSWD, MF_METADATA_DB_USER, MF_METADATA_DB_NAME, MF_METADATA_DB_HOST, MF_METADATA_DB_PORT, MF_METADATA_DB_SSL_MODE
    # Apply kustomization
    kubectl apply -k infra/k8
    kubectl config set-context --current --namespace=acme-metaflow
    kubectl get services
    # see https://minikube.sigs.k8s.io/docs/start/?arch=%2Fmacos%2Farm64%2Fstable%2Fbinary+download#Service
    # for how to access ClusterIP type service
    kubectl port-forward service/acme-metaflow-service-k8-service 7080:8080
    curl http://localhost:7080/ping

Then:

1. Run `kubectl port-forward service/acme-metaflow-service-k8-service 7080:8080` to forward from local port 7080 to metadata service running on port 8080 in the service.
1. Run `metaflow configure kubernetes`
and provide configuration:

        "METAFLOW_DEFAULT_METADATA": "service",
        "METAFLOW_KUBERNETES_CONTAINER_IMAGE": "python:3.12",
        "METAFLOW_KUBERNETES_NAMESPACE": "acme-metaflow",
        "METAFLOW_KUBERNETES_SECRETS": "k8-job-auth-<unique identifier for secret>",
        "METAFLOW_KUBERNETES_SERVICE_ACCOUNT": "default",
        "METAFLOW_SERVICE_INTERNAL_URL": "http://acme-metaflow-service-k8-service.acme-metaflow.svc.cluster.local:8080",
        "METAFLOW_SERVICE_URL": "http://localhost:7080"`

1. Run `python tutorials/00-helloworld/helloworld.py run` to execue the flow against metadataservice.
