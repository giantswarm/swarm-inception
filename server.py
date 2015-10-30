from flask import Flask, render_template

app = Flask(__name__)

# main route
@app.route('/hubhook/')
def hook():
	try:
		return render_template('hook.html', name=name)
	except Exception as e:
		print "an error occured: %s" % e

# finally, our entrypoint...
if __name__ == "__main__":
	app.run(host="0.0.0.0", debug=False)