kubectl autoscale deployment webdb --cpu-percent=10 --min=1 --max=10 -n irjiba
kubectl autoscale deployment webnodb --cpu-percent=60 --min=1 --max=10 -n irjiba
kubectl autoscale deployment mongodb --cpu-percent=60 --min=1 --max=10 -n irjiba

# commande pour tester : 
# while sleep 0.0001; do wget -q -O- http://webdb.irjiba.net4255.luxbulb.org/ ; done
# kubectl get hpa -n irjiba
