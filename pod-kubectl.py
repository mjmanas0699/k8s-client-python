import json
import subprocess

cmd="kubectl get po -n jlab -o json"
output=subprocess.Popen(cmd,shell=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
(stdout,stderr)=output.communicate()
sts_data=json.loads(stdout)
notebook_data=[]

for sts in sts_data["items"]:
    print(str(sts["metadata"]["name"]) + " -> " + str(sts["status"]["containerStatuses"][1]["ready"]))

    
#     notebook_data.append(sts_dict)
# print(notebook_data)
