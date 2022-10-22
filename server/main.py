from app import flask_app
import settings
import settings.flask

if __name__ == '__main__':
    flask_app.app.run(host=settings.flask.HOST_URL, port=8080)
