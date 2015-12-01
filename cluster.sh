#!/bin/bash

# leaseweb
if [ "$1" == "lw" ]; then
	# API_SERVER
	if [ "$2" == "api" ]; then
		echo "api.leaseweb-alpha.giantswarm.io"
		exit
	fi

	# REGISTRY
	if [ "$2" == "registry" ]; then
		echo "registry02.giantswarm.io"
		exit
	fi

	# CLUSTER_ID
	if [ "$2" == "id" ]; then
		echo "leaseweb-alpha-private.giantswarm.io"
		exit
	fi

	# DOMAIN
	if [ "$2" == "domain" ]; then
		echo ".leaseweb-alpha.giantswarm.io"
		exit
	fi
fi

# aws
if [ "$1" == "aws" ]; then
	# API_SERVER
	if [ "$2" == "api" ]; then
		echo "api.giantswarm.io"
		exit
	fi

	# REGISTRY
	if [ "$2" == "registry" ]; then
		echo "registry.giantswarm.io"
		exit
	fi

	# CLUSTER_ID
	if [ "$2" == "id" ]; then
		echo "aws-alpha.giantswarm.io"
		exit
	fi

	# DOMAIN
	if [ "$2" == "domain" ]; then
		echo ".gigantic.io"
		exit
	fi
fi