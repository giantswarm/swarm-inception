from flask import Flask, request, jsonify, render_template
from subprocess import call

import json
import requests

from giantswarm import swarm_auth, swarm_status, swarm_create, swarm_update, swarm_deploy
from github import getdefjson
import swarmconfig

app = Flask(__name__)

@app.route('/')
def index():
	auth = swarmconfig.auth

	# grab this user's info
	info = swarm_auth(auth)

	if info['result'] == "ok":
		return("service is up")
	else:
		return(info['response'])

# main route
@app.route('/<org>/<env>/hook', methods=['GET', 'POST'])
def hook(org=None, env=None):
	# patch the config
	auth = swarmconfig.auth
	auth['env'] = env
	auth['org'] = org

	# load the json POST content
	try:
		content = request.get_json()
	except Exception as e:
		message = "an error occured: %s" % e
		print message

		return jsonify({'response': message})

	# load the repo name, e.g. kordinator/helloworld
	try:
		repository = content['repository']['repo_name']
	except:
		message = "docker POST doesn't have repo_name"

		return jsonify({'response': message})

	# using short description to figure out the github
	# repo for service. it's beyond conception why docker 
	# doesn't return this info with the webhook call
	try: 
		description = json.loads(
			content['repository']['description']
		)
		github = description['github']
	except:
		# bail if we don't have any github info
		message = "short description must contain github JSON info"
		return jsonify({'response': message})

	# get the repository's swarm-api.json definition from github
	definition = getdefjson(
		github['org'],
		github['repo'],
		github['branch'],
		"swarm-api.json"
	)

	print definition
	# look and see if we found the definition on github
	if definition['response'] == "ok":
		# remove return wrapper
		definition = definition['result'] 
	else:
		return jsonify({'response': "fail"})

	# check if the service is running on Giant Swarm
	status = swarm_status(auth, definition)
	print status
	if status['response'] == "ok":
		# toggle behavior on status
		if status['result']['status'] == "up":
			# do an update on the image's component
			print "updating component..."
			swarm_update(auth, definition, repository)
		else:
			print "service is in an unknown state...exiting"

	elif status['response'] == "404":
		# service not running, so deploy
		print "deploying service..."
		print swarm_deploy(auth, definition)

	return jsonify({'response': "ok"})


# finally, our entrypoint...
if __name__ == "__main__":
	app.run(host="0.0.0.0", debug=True)
