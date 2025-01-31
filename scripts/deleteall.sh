#!/bin/bash

echo "Deleting all resources in all namespaces..."

  # Delete all resources in the namespace
  kubectl delete all --all -n irjiba

  # Optionally delete configmaps, secrets, and other resource types
  kubectl delete configmap --all -n irjiba
  kubectl delete secret --all -n irjiba
  kubectl delete pvc --all -n irjiba
  kubectl delete serviceaccount --all -n irjiba
  kubectl delete ingress -n irjiba
  kubectl delete statefulsets --all


echo "All resources have been deleted."
