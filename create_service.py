from kubernetes import client, config
import kubernetes.client.models  
config.load_kube_config(config_file="~/.kube/config")

def service():
    config.load_kube_config()

    v1 = client.CoreV1Api()

    service=client.V1Service(api_version="v1",kind="Service")
    
    service.metadata=client.V1ObjectMeta(name="busybox-service") # service name

    ports=client.V1ServicePort(node_port=True,port=80,protocol="TCP",target_port=80)

    spec=client.V1ServiceSpec(ports=ports) #service-spec

    service.spec=spec

    v1.create_namespaced_service(namespace="default",body=service)

    print("service deployed.")


if __name__ == "__main__":
    service()