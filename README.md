## Swarm Inception
Swarm Inception is a service which can be used to implement continuous deployments for any Giant Swarm service. Builds are conducted via Docker Hub using Github webhooks. When the build is complete, this service is called by Docker Hub's webhooks, which then triggers a deployment of the application to Giant Swarm.

Keep in mind that Swarm Inception does not provide continuous integration tests. If you would like to do continuous integration builds with tests, you may want to investigate the Swacker repository. Swacker uses Wercker's CI/CD service to build container images using stock images from Wercker.

### Prerequisites
