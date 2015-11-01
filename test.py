import requests
import json

headers = {
	'content-type': 'application/json'
}

url = "http://192.168.59.103:5000/kord/dev/hook"
data = {
	'repository': {
		'repo_name': 'kordless/python-flask-helloworld',
		'repo_url': 'https://registry.hub.docker.com/u/kordless/python-flask-helloworld/'
		'description': {
			"github": {
				"org": "kordless",
				"repo": "python-flask-helloworld"
			}
		}
	}
}

# fetch the response
result = requests.post(
	url,
	data=json.dumps(data),
	headers=headers
)

print result