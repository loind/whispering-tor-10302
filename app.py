import bottle
from bottle import default_app, request, route, response, get

bottle.debug(True)

@get('/')
def index():
	return ret

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

bottle.run(host='0.0.0.0', port=argv[1])