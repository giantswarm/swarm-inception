## Swarm Inception
Swarm Inception can be used to implement continuous deployments for any Giant Swarm service. Builds are conducted via Docker Hub using Github webhooks. When the build is complete, Docker Hub will call this service's webhooks, which in turn triggers a deployment or update of the service.

Swarm Inception does not provide continuous integration tests. If you would like to do continuous integration builds with tests, you may want to check out [Wercker's CI/CD service](http://wercker.com/).

### Prerequisites
At a minimum you will need the following to launch this guide's services:

* A Github [account](https://github.com).
* A Giant Swarm [account](https://giantswarm.io/request-invite/).
* A Docker Hub [account](https://hub.docker.com).

### Video Walkthrough
Here's another fine video guide by your's truly. Look for the kick.

[![](https://raw.githubusercontent.com/giantswarm/swarm-wercker/master/static/video.png)](https://vimeo.com/134043502)

### Getting Started
This project should take you about 10 minutes to run through. We'll start by forking the sample repo, setting up a Docker Hub account and then configuring it to build the repo.

#### Fork the Repo
Start by heading over to [this repository](https://github.com/giantswarm/swarm-inception) and then fork it into your Github account. Make sure you leave the repository public!

![](https://raw.githubusercontent.com/giantswarm/swarm-flask-helloworld/master/assets/fork.png)

[Follow the instructions](https://github.com/giantswarm/swarm-flask-helloworld/blob/master/README.md#flask-helloworld) in the `README.md` file on the repo, then come back here when you are done.

#### Create Automated Build on Docker Hub
{"github": {"org": "kordless", "repo": "python-flask-helloworld", "branch": "master"} }
