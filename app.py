from kubernetes import client, config

# Load kubeconfig from ~/.kube/config
config.load_kube_config()

# Create API client
v1 = client.CoreV1Api()

# List pods in default namespace
pods = v1.list_namespaced_pod(namespace="default")

print("Pods in default namespace:")

for pod in pods.items:
    print(pod.metadata.name)
