# Commands

## General

```bash
kubectl create -f nginx-deployment.yaml
```

```bash
kubectl replace --force -f <file_name>
```
![img_1.png](img_1.png)

```bash



- `-dry-run`: By default as soon as the command is run, the resource will be created. If you simply want to test your command , use the `-dry-run=client` option. This will not create the resource, instead, tell you whether the resource can be created and if your command is right.
- `-o yaml`: This will output the resource definition in YAML format on screen.

## PODs

```bash
kubectl run nginx --image=nginx
```

```bash
kubectl run nginx --image=nginx --dry-run=client -o yaml
```

```bash
kubectl edit pod <pod-name>
```

When changing a running POD, it will fail but it will save the POD configuration in a temporary file `/tmp/...yaml` and that can be used to ******************replace****************** the existing POD with `kubectl replace --force -f /tmp/....yaml`

## Deployments

```bash
kubectl create deployment --image=nginx nginx
```

```bash
kubectl create deployment --image=nginx nginx --dry-run=client -o yaml
```

```bash
kubectl create deployment --image=nginx nginx --replicas=4 --dry-run=client -o yaml > nginx-deployment.yaml
```

## Services

```bash
kubectl expose pod redis --port=6379 --name redis-service --dry-run=client -o yaml
```

`kubectl create service clusterip redis --tcp=6379:6379 --dry-run=client -o yaml` (This will not use the pods labels as selectors, instead it will assume selectors as **app=redis.** [You cannot pass in selectors as an option.](https://github.com/kubernetes/kubernetes/issues/46191) So it does not work very well if your pod has a different label set. So generate the file and modify the selectors before creating the service)

**Create a Service named nginx of type NodePort to expose pod nginx's port 80 on port 30080 on the nodes:**

`kubectl expose pod nginx --type=NodePort --port=80 --name=nginx-service --dry-run=client -o yaml`

(This will automatically use the pod's labels as selectors, [but you cannot specify the node port](https://github.com/kubernetes/kubernetes/issues/25478). You have to generate a definition file and then add the node port in manually before creating the service with the pod.)

Or

`kubectl create service nodeport nginx --tcp=80:80 --node-port=30080 --dry-run=client -o yaml`

(This will not use the pods labels as selectors)

Both the above commands have their own challenges. While one of it cannot accept a selector the other cannot accept a node port. I would recommend going with the `kubectl expose` command. If you need to specify a node port, generate a definition file using the same command and manually input the nodeport before creating the service.

## Taints and Tolerations

```bash
kubectl describe nodes node01 | grep Taint
```

```bash
kubectl taint nodes node01 spray=mortein:NoSchedule
```

For removing a taint, the same command can be used, just with a `-` at the end.

```bash
kubectl taint nodes node01 spray=mortein:NoSchedule-
```

## NODES

To go to specific node:

`kubectl get nodes -o wide`

And `ssh` to the `IP`

[Schedulers](https://www.notion.so/Schedulers-d64c898690564f8a8c17a68ff6f64457?pvs=21)