from flask import request,Flask,render_template
from kubernetes import client, config
from kubernetes.client.models import V1Pod, V1ObjectMeta, V1Container, V1PodSpec

app = Flask(__name__)
config.load_incluster_config()

@app.route('/', methods=['GET', 'POST'])
def create_pod():
    if request.method=="POST":
        data=request.form
        
        v1 = client.CoreApi()

        pod=client.V1Pod()

        pod.metadata=client.V1ObjectMeta(name=data["con_name"]) #pod name

        container=client.V1Container(name=data["con_name"], image=data["img_name"], image_pull_policy="IfNotPresent")
        container.args=["sleep", "3600"]

        spec=client.V1PodSpec(containers=[container], restart_policy="Always")
        pod.spec = spec
        v1.create_namespaced_pod(namespace="default",body=pod)
        return "Pod deployed "+ data["con_name"]
    else:
      return render_template('index.html')