#!/bin/bash

kubectl set image deployments/webnodb webnodb=docker.io/ilefrjiba/webnodb:v2
kubectl set image deployments/webdb webdb=docker.io/ilefrjiba/flask-app:v3
