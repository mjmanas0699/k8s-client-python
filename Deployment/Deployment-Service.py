from kubernetes import client, config 
from yaml import dump
config.load_kube_config()
appsv1 = client.AppsV1Api()
corev1api=client.CoreV1Api()

pod_spec=client.V1PodSpec(containers=[client.V1Container(
                            image="nginx",
                            name="conpy",
                            ports=[client.V1ContainerPort(protocol="TCP",container_port=80,name="containerport")])])

deploy_template=client.V1PodTemplateSpec(metadata=client.V1ObjectMeta(
                            name="pody",
                            labels={"app":"test"}),
                            spec=pod_spec)

deploy_spec=client.V1DeploymentSpec(
                            replicas=1,
                            selector=client.V1LabelSelector(match_labels={"app":"test"}),
                            template=deploy_template)

deploy=client.V1Deployment(kind="Deployment",
                            metadata=client.V1ObjectMeta(name="testfrompython"),
                            spec=deploy_spec)

service_spec=client.V1ServiceSpec(type="ClusterIP",
                            ports=[client.V1ServicePort(target_port=80,port=8080)],
                            selector={"app":"test"})

service=client.V1Service(kind="Service",metadata=client.V1ObjectMeta(name="testfrompython"),spec=service_spec)


# print(dump(deploy.to_dict()))
# print(dump(service.to_dict()))
deploy_result=appsv1.create_namespaced_deployment(namespace="default",body=deploy) #SERVICE CREATION

service_result=corev1api.create_namespaced_service(namespace="default",body=service) #Deployment CREATION

