from flask import request, jsonify
from config import create_app
from models import db, Episode, Guest, Appearance

app = create_app()