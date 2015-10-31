# account info
USERNAME = $(shell swarm user)
TOKEN = $(shell cat ~/.swarm/token)
ENV = $(shell swarm env)

# service info
SERVICE = inception
REGISTRY = registry.giantswarm.io
IMAGE = $(REGISTRY)/$(USERNAME)/$(SERVICE)
DOMAIN = inception-api-$(USERNAME).gigantic.io
PORT = 5000
DEV_DOMAIN = $(shell boot2docker ip):$(PORT)

token:
	@echo "token='$(TOKEN)'" > token.py
	@echo "Token file created at token.py..."

build: token
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
	@echo "Use http://$(DOMAIN)/hubhook/ on Docker Hub's hook to deploy a service."

clean:
	rm swarm-api.json swarm.json token.py