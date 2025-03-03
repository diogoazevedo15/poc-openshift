# OpenShift POC

This project runs on an OpenShift cluster (deployed locally with CodeReady Containers **crc**). Below is a simple diagram of how the components are connected:

![Architecture Diagram](docs/images/architecture.png)

1. **Pods**: Each pod runs your containerized front-end or back-end application.
2. **Services**: They provide a stable endpoint (cluster-internal IP) for each set of pods.
3. **Routes**: They expose the Services externally, allowing the user to access the applications from outside the cluster.

## Project Structure

```
project-root/
│
├── openshift/
│   ├── backend-deployment.yaml # Contains the YAML files for deploying the applications (front-end and back-end) to OpenShift.
│   ├── backend-route.yaml
│   ├── backend-service.yaml
│   ├── frontend-deployment.yaml
│   ├── frontend-route.yaml
│   └── frontend-service.yaml
│
├── backend/ # Basic Python back-end.
│   ├── app.py
│   ├── Dockerfile
│   └── requirements.txt
│
├── frontend/ # Basic Python front-end.
│   ├── app.py
│   ├── Dockerfile
│   └── requirements.txt
│
└── README.md

```

---

## How to Use

1. **Set up CodeReady Containers (crc)**:
    - Install `crc` and follow the official documentation to configure your local OpenShift cluster.
    - Start your cluster using the commands listed in the [CRC Commands](https://www.notion.so/Openshift-1a83dd4d61fb80089f2ad6cc8c931b8f?pvs=21) section.
2. **Log into your cluster**:
    - Once the cluster is up, you can use the `oc` CLI to log in. You’ll need the administrator credentials provided by `crc`.
3. **Create the `poc-openshift` namespace** (if it doesn’t already exist):
    
    ```bash
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
