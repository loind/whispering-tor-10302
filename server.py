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
	print("User read: %s" % request.query)

	imgPath = "res/images/a.jpg"
	fp = open(imgPath, "rb")

	bytes = fp.read()
	bottle.response.set_header('Content-type', 'image/png')
	print(len(bytes))
	fp.close()
	return bytes


if __name__ == '__main__':
	bottle.run(application=APP)
