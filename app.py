import bottle
from bottle import default_app, request, route, response, get

bottle.debug(True)

@route('/<filename:path>')
def send_static(filename):
    return static_file(filename, root=".")

@get('/')
def index():
	print('abc')
	return "Hello"

@route('/images')
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


run(default_app(), host='0.0.0.0', port=8080)
# bottle.run(host='0.0.0.0', port=8080)