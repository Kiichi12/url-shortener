from flask import Blueprint, request, jsonify
import random
import string
from .database import db

url = Blueprint('url', __name__)

def generate_short_code():
    return ''.join(random.choices(string.ascii_letters + string.digits, k=6))

@url.route('/shorten', methods=['POST'])
def shorten_url():
    data = request.json
    original_url = data.get('url')

    short_code = generate_short_code()
    db.urls.insert_one({"original_url": original_url, "short_code": short_code})

    return jsonify({"short_url": f"http://localhost:5000/{short_code}"}), 201