# account info
USERNAME = $(shell swarm user)
TOKEN = $(shell cat ~/.swarm/token)
ENV = $(shell swarm env)
ORG = $(shell swarm env | cut -d'/' -f1)
API_SERVER = api.giantswarm.io

# service info
SERVICE = inception
REGISTRY = registry.giantswarm.io
IMAGE = $(REGISTRY)/$(ORG)/$(SERVICE)
DOMAIN = inception-$(USERNAME).gigantic.io
PORT = 5000
DEV_DOMAIN = $(shell boot2docker ip):$(PORT)

config:
	@ ./config.sh '$(SERVICE)' '$(IMAGE)' '$(DOMAIN)' '$(PORT)' '$(API_SERVER)' '$(TOKEN)'
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

clean:
	rm swarm-api.json swarm.json swarmconfig.py