#!/bin/bash

SERVICE=$1 
IMAGE=$2
DOMAIN=$3
PORT=$4
API_SERVER=$5
TOKEN=$6
ORG=$7
CLUSTER_ID=$8

# build swarm.json
sed -e "
s,%SERVICE%,$SERVICE,g;
s,%IMAGE%,$IMAGE,g;
s,%DOMAIN%,$DOMAIN,g;
s,%PORT%,$PORT,g;
" swarm.json.template > swarm.json

# build swarm-api.json to be checked into repo
sed -e "
s,%SERVICE%,$SERVICE,g;
s,%IMAGE%,$IMAGE,g;
s,%DOMAIN%,$DOMAIN,g;
s,%PORT%,$PORT,g;
" swarm-api.json.template > swarm-api.json

# build the configuration file for python
echo "
auth = {
	'token':'$TOKEN',
	'server':'$API_SERVER',
	'org':'$ORG',
	'cluster_id': '$CLUSTER_ID'
} 
" > swarmconfig.py
