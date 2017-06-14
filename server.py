import bottle

APP = bottle.default_app()

bottle.debug(True)

@APP.route('/')
def index():
	return '<p>Hello</p>'

@APP.route('/index.html')
def index():
	bottle.response.content_type = 'text/html'
	return bottle.static_file('index.html', '.')
  
@APP.route('/images')
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


if __name__ == '__main__':
	bottle.run(application=APP)
