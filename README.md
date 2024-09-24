# Istio Kubernetes Services Mesh Microservices

Studies based in day 7-8 of 100 Days System Design for DevOps and Cloud Engineers

https://deoshankar.medium.com/100-days-system-design-for-devops-and-cloud-engineers-18af7a80bc6f

Days 1–10: Advanced Architectural Concepts.

Day 7–8: Learn about service mesh technologies; deploy Istio in a Kubernetes cluster and configure a sample microservices application.

This example uses Kind with Istio as service mesh using sidecar pattern.

Install Kind and Istio.

Create cluster:
```
kind create cluster --name istio-test
```

Install Istio with the Demo Profile:
```
istioctl install --set profile=demo -y
```

Verify Istio instalation:
```
kubectl get pods -n istio-system
```

Label the Default Namespace:
```
kubectl label namespace default istio-injection=enabled
```

Apply services:
```
kubectl apply -f deployment.yaml
kubectl apply -f service.yaml
kubectl apply -f gateway.yaml
```

Get the Ingress Gateway’s External IP:
```
kubectl port-forward svc/istio-ingressgateway -n istio-system 8080:80
```

Listen to the application:
```
curl http://localhost:8080
```

What is the Sidecar Pattern?
The sidecar pattern refers to a microservices architecture design pattern where additional functionalities, like logging, monitoring, networking, or security, are offloaded to a separate container (sidecar) that runs alongside the main application container in a pod. This way, the application doesn't need to include these capabilities itself but can rely on the sidecar to handle them.

In the case of Istio, the sidecar container is an Envoy proxy, which is automatically injected into every pod in your service mesh. This proxy manages network traffic, routing, security, and observability for the application container without requiring any changes to the application code.

Delete Cluster:
```
kind delete cluster --name istio-test
```