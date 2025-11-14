def handler(request, response):
    response.status_code = 200
    response.set_body({"message": "Test route working!"})
