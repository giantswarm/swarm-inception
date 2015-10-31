from flask import Flask, request, render_template
from subprocess import call

import json
import requests

from giantswarm import swarm_status, swarm_create
from github import getdeployjson
import swarmconfig

app = Flask(__name__)

# main route
@app.route('/<org>/<env>/hook', methods=['GET', 'POST'])
def hook(org=None, env=None):
	try:
		try:
			content = request.get_json()
		except Exception as e:
			print e
			content = {}

		# we assume master on the fetch given docker 
		# won't tell us what branch they are hooking
		# also, they rename github repos to 'repo_name'
		branch = "master"
		print content
		repository = content['repository']['repo_name']
		
		# tempted to use this for aux json
		# description = content['repository']['description']

		# get the repository's swarm-api.json file
		deploy = getdeployjson(
			repository,
			branch,
			"swarm-api.json"
		)

		# bail out if we failed
		if deploy['response'] == "ok":
			deploy = deploy['config'] # remove return wrapper
		else:
			return render_template('fail.html')

		# patch the config
		auth = swarmconfig.auth
		auth['env'] = env
		auth['org'] = org

		# grab the service name
		service = deploy['name']

		# check if the service is running
		status = swarm_status(auth, service)

		return render_template('hook.html', content=content)
	
	except Exception as e:
		print "an error occured: %s" % e
		return "error: %s" % e

# finally, our entrypoint...
if __name__ == "__main__":
	app.run(host="0.0.0.0", debug=True)