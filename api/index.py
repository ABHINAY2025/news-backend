from app import app as application  # import your Flask app

def handler(request, response):
    return application(request, response)
