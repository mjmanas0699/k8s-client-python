from kubernetes import client, config 
from yaml import dump
config.load_kube_config()
appsv1 = client.AppsV1Api()
corev1api=client.CoreV1Api()


persistent_vol_spec=client.V1PersistentVolumeClaimSpec(access_modes=["ReadWriteOnce"],
                                                      resources=client.V1ResourceRequirements(requests={"storage":"1Gi"}
                                                      )	)
persistent_vol=client.V1PersistentVolumeClaim(kind="PersistentVolumeClaim",
                                              metadata=client.V1ObjectMeta(name="testfrompython"),
                                              spec=persistent_vol_spec)

persistent_volumeclaim=client.V1Volume(persistent_volume_claim=client.V1PersistentVolumeClaimVolumeSource(claim_name="testfrompython"),name="testfrompython")

persistent_volume_claim_mounts=client.V1VolumeMount(mount_path="/data",name="testfrompython")

pod_spec=client.V1PodSpec(volumes=[persistent_volumeclaim],containers=[client.V1Container(
                            image="nginx",
                            name="conpy",
                            ports=[client.V1ContainerPort(protocol="TCP",
                            container_port=80,name="containerport")],volume_mounts=[persistent_volume_claim_mounts])])

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


print(dump(deploy.to_dict()))
# print(dump(service.to_dict()))
# deploy_result=appsv1.create_namespaced_deployment(namespace="default",body=deploy) #SERVICE CREATION

# service_result=corev1api.create_namespaced_service(namespace="default",body=service) #Deployment CREATION

# persistent_vol_result=corev1api.create_namespaced_persistent_volume_claim(namespace="default",body=persistent_vol)