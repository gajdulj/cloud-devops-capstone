[![gajdulj](https://circleci.com/gh/gajdulj/cloud-devops-capstone.svg?style=svg)](https://app.circleci.com/pipelines/github/gajdulj/cloud-devops-capstone)

## Project Overview

* This project demonstrates automatic update capabilities of CICD pipeline.
* Every change of the main branch of the github repository will triger the update of this application.
* The infrastructure as code starts a Kubernetes cluster on AWS that the app is running in.
* Code linting and automated tests are performed before any update takes place.
* Deployment method used: rolling

## Testing locally before circleci pipeline gets used:

## Setup the Environment

* Create a virtualenv and activate it
* Run `make install` to install the necessary dependencies

### Running `app.py`

1. Standalone:  `python app.py`
2. Run in Docker:  `./run_docker.sh`
3. Run in Kubernetes:  `./run_kubernetes.sh`

### Kubernetes Steps

* Setup and Configure Docker locally
* Setup and Configure Kubernetes locally
* Create Flask app in Container
* Run via kubectl