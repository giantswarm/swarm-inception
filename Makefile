# account info
USERNAME = $(shell swarm user)
TOKEN = $(shell cat ~/.swarm/token)
ENV = $(shell swarm env)
ORG = $(shell swarm env | cut -d'/' -f1)

# service info
SERVICE = inception
#API_SERVER = api.leaseweb-alpha.giantswarm.io
API_SERVER = api.giantswarm.io
#REGISTRY = registry02.giantswarm.io
REGISTRY = registry.giantswarm.io
#CLUSTER_ID = leaseweb-alpha-private.giantswarm.io
CLUSTER_ID = aws-alpha.giantswarm.io
#DOMAIN = inception-$(USERNAME).leaseweb-alpha.giantswarm.io
DOMAIN = inception-$(USERNAME).gigantic.io
IMAGE = $(REGISTRY)/$(ORG)/$(SERVICE)
PORT = 5000
DEV_DOMAIN = $(shell boot2docker ip):$(PORT)

config:
	@ ./config.sh '$(SERVICE)' '$(IMAGE)' '$(DOMAIN)' '$(PORT)' '$(API_SERVER)' '$(TOKEN)' '$(ORG)' '$(CLUSTER_ID)'
	@echo "Configuration file written to swarmconfig.py..."

build: config
	docker build -t $(IMAGE) .

run: build
	docker run --name=inception --rm -ti \
		-p $(PORT):$(PORT) \
		$(IMAGE)

push: build
	docker push $(IMAGE)

pull:
	docker pull $(IMAGE)

deploy: push
	swarm up
	@echo "Use http://$(DOMAIN)/$(ENV)/hook on Docker Hub's hook to deploy a service."

update: push
	swarm update $(SERVICE)/flask

clean:
	rm swarm-api.json swarm.json swarmconfig.py
