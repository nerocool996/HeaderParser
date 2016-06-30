from flask import Flask, render_template, request, redirect, url_for,flash, jsonify,make_response
from datetime import date,timedelta
app = Flask(__name__)


@app.route('/')
def mainpage():
	return jsonify({"ipaddress":request.remote_addr,"language":request.headers.get("Accept-Language"),"Operating System":request.user_agent.platform})



        

##if __name__ == '__main__':
app.secret_key = 'super_secret_key'
app.debug = True
##	app.run(host = '0.0.0.0', port = 5000)
