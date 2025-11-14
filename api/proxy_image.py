import requests
from io import BytesIO
import base64

def handler(request, response):
    url = request.query.get("url")

    if not url:
        response.status_code = 400
        return response.set_body("Missing URL")

    try:
        img = requests.get(url, timeout=10).content
        b64 = base64.b64encode(img).decode("utf-8")
        response.status_code = 200
        response.set_body({"image": b64})
    except:
        response.status_code = 500
        response.set_body("Error loading image")
