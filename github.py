import requests
import json

def getdeployjson(respository=None, branch=None, filename=None):

	message = "ok"
	config = {}

	url = "https://%s/%s/%s/%s" % (
		"raw.githubusercontent.com",
		respository,
		branch,
		filename
	)

	try:
		# fetch the response
		result = requests.get(
			url
		)

		config = json.loads(result.text)

	except Exception as ex:
		config = "error"
		message = "caught exception: %s" % ex

	# return some json
	return {'config': config, 'response': message}