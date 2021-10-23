import json
import subprocess

cmd="kubectl get vs -n jlab -o json"
output=subprocess.Popen(cmd,shell=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
(stdout,stderr)=output.communicate()
sts_data=json.loads(stdout)
notebook_data=[]

for sts in sts_data["items"]:
    print("ip.nip.io" + sts["spec"]["http"][0]["match"][0]["uri"]["prefix"])

    
#     notebook_data.append(sts_dict)
# print(notebook_data)
