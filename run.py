import sys
sys.path.append('.')
from app import app

app.run(host=None,port=8099,debug = True)