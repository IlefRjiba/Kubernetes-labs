kubectl autoscale deployment webdb --cpu-percent=60 --min=1 --max=10
kubectl autoscale deployment webnodb --cpu-percent=60 --min=1 --max=10
kubectl autoscale deployment mongodb --cpu-percent=60 --min=1 --max=10