from flask import Flask
from flask_cors import CORS
from routes.auth_routes import auth
from routes.url_routes import url

app = Flask(__name__)
CORS(app)

app.register_blueprint(auth, url_prefix='/api/auth')
app.register_blueprint(url, url_prefix='/api/url')

if __name__ == '__main__':
    app.run(debug=True)