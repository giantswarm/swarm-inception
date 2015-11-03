## Swarm Inception
Swarm Inception can be used to implement continuous deployments for any Giant Swarm service. Builds are conducted via Docker Hub using Github webhooks. When the build is complete, Docker Hub will call this service's webhooks, which in turn triggers a deployment or update of the service.

Swarm Inception does not provide continuous integration tests. If you would like to do continuous integration builds with tests, you may want to check out [Wercker's CI/CD service](http://wercker.com/).

### Prerequisites
At a minimum you will need the following to launch this guide's services:

* A Github [account](https://github.com).
* A Giant Swarm [account](https://giantswarm.io/request-invite/).
* A Docker Hub [account](https://hub.docker.com).
