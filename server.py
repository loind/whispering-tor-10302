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
	try:
		print("User read: %s" % request.query.userid)
	except Exception as e:
		pass

	imgPath = "res/images/a.jpg"
	fp = open(imgPath, "rb")

	bytes = fp.read()
	response.set_header('Content-type', 'image/png')
	print(len(bytes))
	fp.close()
	return bytes

@APP.route('/1.0' + '/callbacks/fb', methods=['GET', 'POST'])
def facebook_callback():
	print(request.json)
	pass


if __name__ == '__main__':
	run(application=APP)