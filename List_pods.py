from kubernetes import client, config
# config.load_incluster_config()
config.load_kube_config(config_file="~/.kube/config")
def get_pods():  
    v1 = client.CoreV1Api()
    pod_list = v1.list_namespaced_pod("jlab")
    print(pod_list)
    for pod in pod_list.items:
        print(pod)    

get_pods()

