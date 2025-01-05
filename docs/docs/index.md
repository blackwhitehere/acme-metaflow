# Description

Metaflow based orchestration

## Motivation

Metaflow is a powerful framework to orchestrate computation for data intensive applications. However, with multitude of features and infrastrucutre options it may become difficult to start using it.
This repo aims to present a straigtforward implementation of using metaflow to implement data processing applications.

## Features

- `tutorials` dir contains a series of exercices introduing a new user to metaflow concepts
- `src/acme_metaflow` dir contains example workflows where metaflow is used to implement data processing
- `admin` includes useful scripts for managing credentials, installing dependencies
- `infra/k8` contains resource definitions for setting up metaflow infrastructure on Kubernetes