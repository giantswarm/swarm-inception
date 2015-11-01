import requests
import json

def getdefjson(org=None, repo=None, branch=None, filename=None):

	message = "ok"
	definition = {}

	url = "https://%s/%s/%s/%s/%s" % (
		"raw.githubusercontent.com",
		org,
		repo,
		branch,
		filename
	)

	try:
		# fetch the response
		result = requests.get(
			url
		)

		# did we get a 404?
		if result.status_code == 404:
			message = "404"
			data = "not found"
		else:	
			data = json.loads(result.text)

	except Exception as ex:
		data = "error"
		message = "caught exception: %s" % ex

	# return some json
	return {'result': data, 'response': message}