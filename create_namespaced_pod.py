from kubernetes import client, config
from kubernetes.client.models import V1Pod, V1ObjectMeta, V1Container, V1PodSpec
# config.load_kube_config(config_file="~/.kube/config")
config.load_incluster_config()
def create_pod():
    v1 = client.CoreV1Api()
    pod=client.V1Pod()
    pod.metadata=client.V1ObjectMeta(name="busybox-python") #pod name

    container=client.V1Container(name="busybox", image="busybox", image_pull_policy="IfNotPresent")
    container.args=["sleep", "3600"]

    spec=client.V1PodSpec(containers=[container], restart_policy="Always")
    pod.spec = spec

    v1.create_namespaced_pod(namespace="default",body=pod)

    print("Pod deployed.")


if __name__ == "__main__":
    create_pod()