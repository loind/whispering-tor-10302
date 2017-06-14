#!/usr/bin/env python
from bottle import *

app = application = default_app()

def start_xloyalty_main_services():
	# app.merge(social_app)
	# httpserver.serve(app, host = '0.0.0.0', port = '8080')
	run(app, host = '0.0.0.0', port = '8080')

@app.route('/images')
def root_index():
	return getImage()

def getImage():
	# image_buffer = BytesIO()
	# pi_camera.capture(image_buffer, format='png') # This works without a problem

	imgPath = "res/images/a.jpg"
	fp = open(imgPath, "rb")

	bytes = fp.read()
	response.set_header('Content-type', 'image/png')
	print(len(bytes))
	fp.close()
	return bytes

# getImage()
start_xloyalty_main_services()