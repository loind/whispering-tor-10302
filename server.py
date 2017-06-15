from bottle import *

APP = default_app()

@APP.route('/')
def index():
	return '<p>Hello</p>'

@APP.route('/index.html')
def index():
	response.content_type = 'text/html'
	return static_file('index.html', '.')
  
@APP.route('/images')
def getImage():
	print("User read: %s" % request.query)

	imgPath = "res/images/a.jpg"
	fp = open(imgPath, "rb")

	bytes = fp.read()
	response.set_header('Content-type', 'image/png')
	print(len(bytes))
	fp.close()
	return bytes


if __name__ == '__main__':
	run(application=APP)
