from kubernetes import client, config
import json
# config.load_incluster_config()
config.load_kube_config(config_file="~/.kube/config")
def get_sts():  
    v1 = client.AppsV1Api()
    sts_list = v1.list_namespaced_stateful_set("jlab")
    print(sts_list)
    # for sts in sts_list.items:
    #     print(sts) 

get_sts()

