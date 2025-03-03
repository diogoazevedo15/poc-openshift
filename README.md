# OpenShift POC

This repository contains a simple proof of concept (POC) project demonstrating how to work with an OpenShift cluster (deployed locally using [crc](https://crc.dev/)). It features two components: a front-end application and a back-end application, each running in its own container, deployed to the `poc-openshift` namespace within the cluster.

## Table of Contents

1. [Project Structure](https://www.notion.so/Openshift-1a83dd4d61fb80089f2ad6cc8c931b8f?pvs=21)
2. [Architecture Overview](https://www.notion.so/Openshift-1a83dd4d61fb80089f2ad6cc8c931b8f?pvs=21)
3. [OpenShift Concepts](https://www.notion.so/Openshift-1a83dd4d61fb80089f2ad6cc8c931b8f?pvs=21)
4. [How to Use](https://www.notion.so/Openshift-1a83dd4d61fb80089f2ad6cc8c931b8f?pvs=21)
5. [Cheat Sheets](https://www.notion.so/Openshift-1a83dd4d61fb80089f2ad6cc8c931b8f?pvs=21)
    - [CRC Commands](https://www.notion.so/Openshift-1a83dd4d61fb80089f2ad6cc8c931b8f?pvs=21)
    - [OC Commands](https://www.notion.so/Openshift-1a83dd4d61fb80089f2ad6cc8c931b8f?pvs=21)

---

## Project Structure

```
project-root/
│
├── openshift/
│   ├── backend-deployment.yaml
│   ├── backend-route.yaml
│   ├── backend-service.yaml
│   ├── frontend-deployment.yaml
│   ├── frontend-route.yaml
│   └── frontend-service.yaml
│
├── backend/
│   ├── app.py
│   ├── Dockerfile
│   └── requirements.txt
│
├── frontend/
│   ├── app.py
│   ├── Dockerfile
│   └── requirements.txt
│
└── README.md

```

- **openshift/**: Contains the YAML files for deploying the applications (front-end and back-end) to OpenShift.
- **backend/**: Basic Python back-end, `app.py`, `Dockerfile`, and `requirements.txt`.
- **frontend/**: Basic Python front-end, `app.py`, `Dockerfile`, and `requirements.txt`.

---

## Architecture Overview

This project runs on an OpenShift cluster (deployed locally with CodeReady Containers **crc**). Below is a simple diagram of how the components are connected:

(i have an image of the architecture. Make it so i can add the path to the image here.)

1. **Pods**: Each pod runs your containerized front-end or back-end application.
2. **Services**: They provide a stable endpoint (cluster-internal IP) for each set of pods.
3. **Routes**: They expose the Services externally, allowing the user to access the applications from outside the cluster.

---

## OpenShift Concepts

- **Pod**: The smallest deployable unit in OpenShift/Kubernetes. Think of it as a single instance of a running process in your cluster.
- **Service**: An abstraction that defines a logical set of pods and a policy by which they can be accessed. This ensures that if pods change IP addresses or are recreated, the Service endpoint remains constant.
- **Route**: A way to expose a Service outside the OpenShift cluster. A route provides an externally accessible hostname.

---

## How to Use

1. **Set up CodeReady Containers (crc)**:
    - Install `crc` and follow the official documentation to configure your local OpenShift cluster.
    - Start your cluster using the commands listed in the [CRC Commands](https://www.notion.so/Openshift-1a83dd4d61fb80089f2ad6cc8c931b8f?pvs=21) section.
2. **Log into your cluster**:
    - Once the cluster is up, you can use the `oc` CLI to log in. You’ll need the administrator credentials provided by `crc`.
3. **Create the `poc-openshift` namespace** (if it doesn’t already exist):
    
    ```bash
    CopyEdit
    oc new-project poc-openshift
    
    ```
    
4. **Deploy the applications**:
    - Navigate to the `openshift/` directory in this repository.
    - Apply the YAML files to create deployments, services, and routes:
        
        ```bash
        oc apply -f backend-deployment.yaml
        oc apply -f backend-service.yaml
        oc apply -f backend-route.yaml
        oc apply -f frontend-deployment.yaml
        oc apply -f frontend-service.yaml
        oc apply -f frontend-route.yaml
        
        ```
        
5. **Verify that pods, services, and routes are running**:
    
    ```bash
    oc get pods
    oc get svc
    oc get route
    
    ```
    
6. **Test the application**:
    - Use the routes (URLs) returned by `oc get route` to access the front-end and back-end applications from your browser or via `curl`.

---

## Cheat Sheets

### CRC Commands

```bash
# Initial setup
crc setup

# Configure resources
crc config set memory 14336
crc config set cpus 6
crc config set enable-cluster-monitoring true

# Start CRC (specify your pull secret path)
crc start --pull-secret-file ~/Downloads/pull-secret.txt

```

### OC Commands

```bash
# Apply a YAML file to create or update resources
oc apply -f "file_name"

# View resources (pods, svc, routes) with optional name
oc get pod/svc/route "name"

# Delete resources by name
oc delete pod/svc/route "name"

```

---

## License

This project is licensed under MIT License – feel free to customize the license section to whatever suits your project best.