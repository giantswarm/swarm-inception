from flask import Flask, request, render_template
from giantswarm import status, create, start, stop
import json
import token

app = Flask(__name__)

# main route
@app.route('/<org>/<workspace>/hook', methods=['GET', 'POST'])
def hook(org=None, workspace=None):
	try:
		content = request.get_json()
		
		return render_template('hook.html', content=content)
	except Exception as e:
		print "an error occured: %s" % e
		return "error: %s" % e

# finally, our entrypoint...
if __name__ == "__main__":
	app.run(host="0.0.0.0", debug=True)