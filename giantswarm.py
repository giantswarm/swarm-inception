import requests, json, time

# get service status
def swarm_status(auth, definition):

	message = "ok"
	status = ""
	headers = {
		'Authorization': 'giantswarm %s' % auth['token']
	}

	# grab the service name
	# what is this, coinbase?
	service = definition['definition']['name']

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
	
		# did we get a 40x response?
		# why is a 'resource not found' not a 404?
		if result.status_code >= 400:
			message = "404"
			data = "not found"
		else:	
			data = json.loads(result.text)['data']
	
	except Exception as ex:
		data = "error"
		message = "caught exception: %s" % ex

	# return some json
	return {'result': data, 'response': message}

# create a service
def swarm_create(auth, definition):

	message = "ok"
	data = ""
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
		data = "error"
		message = "caught exception: %s" % ex

	# return some json
	return {'result': data, 'response': message}

def swarm_start(auth, definition):

	message = "ok"
	data = ""
	headers = {
		'Authorization': 'giantswarm %s' % auth['token'],
		'content-type': 'application/json'
	}

	try:
		# call the create service method
		# POST /v1/org/{org}/env/{env}/service/{service}/start
		url = "https://%s/v1/org/%s/env/%s/service/%s/start" % (
			auth['server'],
			auth['org'],
			auth['env'],
			definition['definition']['name']
		)

		# fetch the response
		result = requests.post(
			url,
			headers=headers
		)
	
		data = json.loads(result.text)

	except Exception as ex:
		data = "error"
		message = "caught exception: %s" % ex
		print message

	# return some json
	return {'result': data, 'response': message}

def swarm_update(auth, definition, repository):

	message = "ok"
	status = ""
	headers = {
		'Authorization': 'giantswarm %s' % auth['token'],
		'content-type': 'application/json'
	}

	# loop over the components
	for key in definition['definition']['components']:
		if repository == definition['definition']['components'][key]['image']:
			# do an update of this component
			try:
				# call the create service method
				# POST /v1/org/{org}/env/{env}/service/{service}/start
				url = "https://%s/v1/org/%s/env/%s/service/%s/component/update" % (
					auth['server'],
					auth['org'],
					auth['env'],
					definition['definition']['name']
				)
				print key

				# set the component to the key and version to latest
				data = {
					"component": key,
					"version": "latest"
				}

				# fetch the response
				result = requests.post(
					url,
					data=json.dumps(data),
					headers=headers
				)
			
				data = json.loads(result.text)
				print data

			except Exception as ex:
				data = "error"
				message = "caught exception: %s" % ex
				print message

	# return some json
	return {'result': data, 'response': message}

def swarm_deploy(auth, definition):
	# do a swarm create
	create = swarm_create(auth, definition)

	if create['response'] == "ok":
		# give it a few seconds to create it
		time.sleep(4)

		# do a swarm start
		return swarm_start(auth, definition) 
	
	return create


