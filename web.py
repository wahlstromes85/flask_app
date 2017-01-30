from flask import Flask, render_template, request
import yelpapi
import os
app = Flask(__name__)

@app.route("/")
def index():
	location = request.values.get('location')
	term = request.values.get('term')
	business = None
	if location:
		business = yelpapi.get_businesses(location, term)
	return render_template('index.html',
		business=business)

if __name__ == "__main__":
	port = int(os.environ.get("PORT", 5000))
	app.run(host="0.0.0.0", port=port)