import requests
import json

headers = {
	'content-type': 'application/json'
}

url = "http://inception-kord.gigantic.io/kord/dev/hook"
data = {
	'repository': {
		'repo_name': 'kordinator/python-flask-hello',
		'repo_url': 'https://registry.hub.docker.com/u/kordinator/swarm-flask-hello/',
		'description': ' \
		{ \
			"github": { \
				"org": "kordless", \
				"repo": "swarm-flask-hello", \
				"branch": "master" \
			} \
		} \
		'
	}
}

# fetch the response
result = requests.post(
	url,
	data=json.dumps(data),
	headers=headers
)

print result.text