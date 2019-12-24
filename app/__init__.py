from flask import Flask
import sys
sys.path.append('.')

app = Flask(__name__)
from app import views