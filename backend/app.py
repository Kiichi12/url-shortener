from flask import Flask
from flask_cors import CORS
from routes.auth_routes import auth
from routes.url_routes import url
import os

app = Flask(__name__)
CORS(app)

app.register_blueprint(auth, url_prefix='/api/auth')
app.register_blueprint(url, url_prefix='/api/url')
@app.route("/")
if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))  # Use PORT environment variable or default to 5000
    app.run(host='0.0.0.0', port=port)
