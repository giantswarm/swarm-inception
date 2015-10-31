import requests, json

# get service status
def swarm_status(auth, service):

	message = "ok"
	status = ""
	headers = {
		'Authorization': 'giantswarm %s' % auth['token']
	}

	try:
		# call the list applications method
		# GET /v1/org/{org}/env/{env}/app/
		url = "https://%s/v1/org/%s/env/%s/service/%s/status" % (
			auth['server'],
			auth['org'],
			auth['env'],
			service
		)

		# fetch the response
		result = requests.get(
			url,
			headers=headers
		)
	
		data = json.loads(result.text)['data']

		# pull status
		status = data['status']
	
	except Exception as ex:
		status = "error"
		message = "caught exception: %s" % ex

	# return some json
	return {'status': str(status), 'response': message}

# create a service
def swarm_create(auth, definition):

	message = "ok"
	status = ""
	headers = {
		'Authorization': 'giantswarm %s' % auth['token'],
		'content-type': 'application/json'
	}

	try:
		# call the create service method
		# POST /v1/org/{org}/env/{env}/service/
		url = "https://%s/v1/org/%s/env/%s/service/" % (
			auth['server'],
			auth['org'],
			auth['env']
		)

		# fetch the response
		result = requests.post(
			url,
			data=json.dumps(definition),
			headers=headers
		)
	
		data = json.loads(result.text)

	except Exception as ex:
		status = "error"
		message = "caught exception: %s" % ex

	# return some json
	return {'result': data, 'response': message}


# get an instance's stats
def swarm_stats(auth, org, instance):

	stats = {}
	message = "ok"
	headers = {
		'Authorization': 'giantswarm %s' % auth['token']
	}

	try:
		# call the instance stats
		# GET /v1/org/{org}/instance/{instance}/stats
		url = "https://%s/v1/org/%s/instance/%s/stats" % (
			auth['server'],
			org,
			instance
		)
		
		# fetch the response
		result = requests.get(url, headers=headers)
		data = json.loads(result.text)
		stats = data['data']

	except Exception as ex:
		message = "caught exception: %s" % ex

	# return some json
	return {'stats': stats, 'response': message}