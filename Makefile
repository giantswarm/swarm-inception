# service info
SERVICE = inception
REGISTRY = registry.giantswarm.io
USERNAME := $(shell swarm user)
IMAGE = $(REGISTRY)/$(USERNAME)/$(SERVICE)
DOMAIN=inception-api-$(USERNAME).gigantic.io
PORT=5000
DEV_DOMAIN=$(shell boot2docker ip):$(PORT)

build:
	docker build -t $(IMAGE) .

run: build
	docker run --name=inception --rm -ti \
		-p $(PORT):$(PORT) \
		$(IMAGE)

push: build
	docker push $(IMAGE)

pull:
	docker pull $(IMAGE)

config:
	./config.sh '$(SERVICE)' '$(IMAGE)' '$(DOMAIN)' '$(PORT)'

deploy: config push
	swarm up
	@echo "Use http://$(DOMAIN)/hubhook/ to push a service from Docker Hub."

clean:
	rm swarm-api.json swarm.json