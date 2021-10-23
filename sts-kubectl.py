import json
import subprocess

sts_cmd="kubectl get sts -n jlab -o json"
sts_cmd_output=subprocess.Popen(sts_cmd,shell=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
sts_cmd_stdout=sts_cmd_output.communicate()[0]
sts_cmd_data=json.loads(sts_cmd_stdout)

sts_status_cmd="kubectl get po -n jlab -o json"
sts_status_output=subprocess.Popen(sts_status_cmd,shell=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
sts_status_stdout=sts_status_output.communicate()[0]
sts_status_data=json.loads(sts_status_stdout)
status_data=[]
i=0
notebook_data=[]
for status in sts_status_data["items"]:
    data=status["status"]["phase"]
    status_data.append(data)
for sts in sts_cmd_data["items"]:
    sts_dict={}
    sts_dict["sts_name"] = sts["metadata"]["name"]
    sts_dict["sts_create_time"] = sts["metadata"]["creationTimestamp"]
    sts_dict["sts_image_name"] = sts["spec"]["template"]["spec"]["containers"][0]["image"]
    sts_dict["sts_cpu"] = sts["spec"]["template"]["spec"]["containers"][0]["resources"]["limits"]["cpu"]
    sts_dict["sts_memory"] = sts["spec"]["template"]["spec"]["containers"][0]["resources"]["limits"]["memory"]
    sts_dict["sts_volume"] = sts["spec"]["template"]["spec"]["containers"][0]["volumeMounts"][0]["name"]
    sts_dict["sts_status"] = status_data[i]
    i=i+1
    notebook_data.append(sts_dict)
print(notebook_data)
