## Swarm Inception
Swarm Inception can be used to implement continuous deployments for any Giant Swarm service, but it's also a good reference document for doing continuous deployments with [Docker Hub's](https://hub.docker.com) builder service. Builds are conducted via  using [Github webhooks](https://developer.github.com/webhooks/) and when the build completes Docker Hub will call this service's webhook handler, which in turn triggers a deployment or update of the image built by Dockerhub onto Giant Swarm's public cloud.

Swarm Inception does not provide continuous integration tests. If you would like to do continuous integration builds with tests, you may want to check out [Wercker's CI/CD service](http://wercker.com/).

### Prerequisites
At a minimum you will need the following to launch this guide's services:

* A Github [account](https://github.com).
* A Giant Swarm [account](https://giantswarm.io/request-invite/).
* A Docker Hub [account](https://hub.docker.com).

### Video Walkthrough
Here's another fine video guide by your's truly. Look for the kick.

[![](https://raw.githubusercontent.com/giantswarm/swarm-inception/master/assets/video.png)](https://vimeo.com/146725428)

### Getting Started
This project should take you about 10 minutes to run through. We'll start by forking the sample repo, setting up a Docker Hub account and then configuring it to build the repo.

#### Start Swarm Inception
You need to start the Swarm Inception service in your Giant Swarm account first. Check the repository out, switch to the directory, and begin the deployment process:

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
Creating 'inception' in the 'kord/dev' environment…
Service created successfully!
Starting service 'inception'…
Waiting for 'inception' to get started…
Service 'inception' is up.
You can see all components using this command:

    swarm status inception

Use http://inception-bant.gigantic.io/bant/dev/hook on Docker Hub's hook to deploy a service.
```

**Note:** The Swarm Inception service will build and push a Docker image from your local machine to Giant Swarm's repository.

#### Fork the Sample Service Repo
Next, head over to [the swarm-flask-hello repo](https://github.com/giantswarm/swarm-flask-hello) and **fork it** into your Github account. Make sure you leave the repository public!

There are detailed [instructions](https://github.com/giantswarm/swarm-flask-helloworld/blob/master/README.md#flask-helloworld) on the repository's `README.md` file you may follow. The basics are covered here for review, and require you have cloned your own fork of repo locally. 

Verify you have built and checked in the `swarm-api.json` file for the `swarm-flask-hello` repo as directed in the [instructions](https://github.com/giantswarm/swarm-flask-helloworld/blob/master/README.md#flask-helloworld):

```
$ cd swarm-flask-hello
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

#### Create an Automated Build on Docker Hub
Create an account on [Docker Hub](https://hub.docker.com/) if you don't have one, and then login.

Click on the `Create` pulldown on the top left of Docker Hub and then click on `Create Automated Build`. If you haven't linked a Github account yet, you will need to do so before continuing with this step. Ensure you give Docker Hub *read and write* access to your Github account.

Once you've added an account, you'll be shown a list of organizations and repos.

![](https://raw.githubusercontent.com/giantswarm/swarm-inception/master/assets/listrepo.png)

Select or search for the `swarm-flask-hello` repository in the list Docker Hub displays. Once you've selected the repository, you'll be presented with the `Automated Build` page:

![](https://raw.githubusercontent.com/giantswarm/swarm-inception/master/assets/build.png)

As shown in the screenshot, you will need to add a snippet of JSON to the `short descriptionn` for the build repo. The reason for this is because Docker Hub won't pass on the Github repository information in the POST hook call we're going to set up in a few minutes.

Here's a sample of the JSON you need to paste in:

```
{"github": {"org": "bant", "repo": "swarm-flask-hello", "branch": "master"} }
```

Substitute your *Github username* for `bant` in the example above and then click on the `Create` button at the bottom of the page to create the new Docker Hub repository build.

**Note:** If you only gave Docker Hub read access to your Github account, you will need to create a build trigger URL. Click on `Build Settings` under the new repo and then click on `Activate` toward the bottom to create a URL to use trigger the build. You will need to paste this URL into the Github repository's webhooks by clicking on `Settings` and `Webhooks & services` on the Github repository you cloned earlier.

#### Create a Webhook to the Inception Service
Finally, click on the `webhooks` tab in the Docker repo and then click on the `Add Webhook` button to create a new webhook. You'll use the following URL format for the URL:

```
http://inception-<username>.gigantic.io/<org>/<env>/hook
```

Change the `<username>`, `<org>` and `<env>` entries above to whatever was output by the launch of the Inception service above.

![](https://raw.githubusercontent.com/giantswarm/swarm-inception/master/assets/hook.png)

Name the webhook something like `dev deployment` and then click on `Add URL` to finish adding the webhook URL.

#### Do a Commit to the Flask Hello Project
Builds and deploys for the `swarm-flask-hello` project occur when you do code pushes to the `master` branch of your newly forked `swarm-flask-hello` repo. To trigger the build, navigate back to the project's repo in your Github account and edit the `index.html` file in the `templates` directory to look something like this:

```
<!doctype html>
<title>Hello from Barcelona!</title>
{% if name %}
  <h1>Hello {{ name }}!</h1>
{% else %}
  <h1>Hello Bants!</h1>
{% endif %}
```

![lama lama ding dong](https://raw.githubusercontent.com/giantswarm/swarm-inception/master/assets/edit.png)

When you are done editing the file, click on the `commit changes` button at the bottom. Docker Hub will start building your image within 10 minutes or so. When it is done, it will call the `swarm-inception` service you started in the previous section, or update it if it was already running.

### Access the New Service
To access the newly built `swarm-flask-hello` service, you will use the following URL format:

```
http://sample-<username>.gigantic.io/
```

Keep in mind if you do subsequent commits to your directory, Docker will do a build of the image and then call an `update` on your Giant Swarm service!

![beachboys](https://raw.githubusercontent.com/giantswarm/swarm-inception/master/assets/barcelona.jpg)

From Barcelona with Love,

Kord
