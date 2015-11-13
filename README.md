## Swarm Inception
Swarm Inception can be used to implement continuous deployments for any Giant Swarm service. Builds are conducted via Docker Hub using Github webhooks. When the build is complete, Docker Hub will call this service's webhooks, which in turn triggers a deployment or update of the image's service being built by Dockerhub.

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
Start by heading over to [the swarm-flask-hello repo](https://github.com/giantswarm/swarm-flask-hello) and **fork it** into your Github account. Make sure you leave the repository public!

There are detailed [instructions](https://github.com/giantswarm/swarm-flask-helloworld/blob/master/README.md#flask-helloworld) on the repository's `README.md` file you may follow. The basics are covered here for review. 

Start by verifying you have built and checked in the `swarm-api.json` file for the `swarm-flask-hello` repo:

```
$ cd swarm-flask-hello # ensure this is your forked copy

$ make config
rm -f swarm-api.json swarm.json
##########################################################
Definition files written...
Check swarm-api.json into your repo before deployment...
##########################################################

$ git add swarm-api.json

$ git commit -m 'config file'
[master 743c7aa] config file
 1 file changed, 18 insertions(+)
 create mode 100644 swarm-api.json

$ git push
Counting objects: 4, done.
Delta compression using up to 4 threads.
Compressing objects: 100% (3/3), done.
Writing objects: 100% (3/3), 424 bytes | 0 bytes/s, done.
Total 3 (delta 1), reused 0 (delta 0)
To https://github.com/bant/swarm-flask-hello.git
   077eddf..743c7aa  master -> master
```

You are now ready to connect this repository to your Docker Hub account.

#### Create Automated Build on Docker Hub
Start by creating an account on [Docker Hub](https://hub.docker.com/) if you don't have one, and then logging into your account.

Click on the `Create` pulldown on the top left of Docker Hub and then click on `Create Automated Build`. If you haven't linked a Github account yet, you will need to do so before continuing with this step. Ensure you give Docker Hub read *and* write access to your Github account.

Select or search for the `swarm-flask-hello` repository in the list Docker Hub displays. Once you've selected the repository, you'll be presented with the `Automated Build` page:

![](https://raw.githubusercontent.com/giantswarm/swarm-inception/master/assets/setupbuild.png)

As shown in the screenshot, you will need to add a snippet of JSON to the `short descriptionn` for the build repo. The reason for this is because Docker Hub won't pass on the Github repository information in the POST hook call we're going to set up in a few minutes.

Here's a sample of the JSON you need to paste in:

```
{"github": {"org": "bant", "repo": "python-flask-hello", "branch": "master"} }
```

Substitute your Github username for `bant` in the example above and then click on the `Create` button at the bottom of the page to create the new Docker Hub repository build.

**Note:** If you only gave Docker Hub read access to your Github account, you will need to create a build trigger URL. Click on `Build Settings` under the new repo and then click on `Activate` toward the bottom to create a URL to use trigger the build. You will need to paste this URL into the Github repository's webhooks by clicking on `Settings` and `Webhooks & services` on the Github repository you cloned earlier.

#### Trigger a Build
On the `Build Settings` tab on the new Docker Hub repo, click on the orange `Trigger a Build` button to the left. This will schedule a build using the Github repository's Dockerfile.

You can check on the status of the build by clicking on the `Build Details` tab at the top:

![](https://raw.githubusercontent.com/giantswarm/swarm-inception/master/assets/setupbuild.png)

After a few minutes the build should complete successfully.

#### Start Swarm Inception
While the test build is running, you can start the Swarm Inception service in your Giant Swarm account. Check the repository out, switch to the directory, and begin the deployment process:

```
$ git clone https://github.com/giantswarm/swarm-inception.git
Cloning into 'swarm-inception'...
remote: Counting objects: 81, done.
remote: Compressing objects: 100% (39/39), done.
remote: Total 81 (delta 34), reused 78 (delta 31), pack-reused 0
Unpacking objects: 100% (81/81), done.
Checking connectivity... done.

$ cd swarm-inception/

$ make deploy
Configuration file written to swarmconfig.py...
docker build -t registry.giantswarm.io/kord/inception .
Sending build context to Docker daemon 501.8 kB
...<snip>
```

**Note:** The Swarm Inception service will build and push a Docker image from your local machine to Giant Swarm's repository. ls



