from bottle import *

ACCESS_CONTROL_ALLOW_ORIGIN = '*'
ACCESS_CONTROL_ALLOW_METHODS = 'PUT, GET, POST, DELETE, OPTIONS'
ACCESS_CONTROL_ALLOW_HEADERS = 'access-control-allow-headers,access-control-allow-methods,access-control-allow-origin,Authorization,content-type'
ACCESS_CONTROL_EXPOSE_HEADERS = 'Authorization'

APP = default_app()

@APP.hook('after_request')
def hook():
	response.headers['Access-Control-Allow-Origin'] = ACCESS_CONTROL_ALLOW_ORIGIN
	response.headers['Access-Control-Allow-Methods'] = ACCESS_CONTROL_ALLOW_METHODS
	response.headers['Access-Control-Allow-Headers'] = ACCESS_CONTROL_ALLOW_HEADERS
	response.headers['Access-Control-Expose-Headers'] = ACCESS_CONTROL_EXPOSE_HEADERS

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

@APP.route('/1.0' + '/callbacks/fb', ['GET', 'POST'])
def facebook_callback():
	print(request.json)
	if request.method == 'GET':
		return request.query['hub.challenge']
	verify_token = "mobio"
	return verify_token


if __name__ == '__main__':
	run(application=APP, host = '0.0.0.0', port = '8080')
