import sys
sys.path.append('.')
from app import app

app.run(host='0.0.0.0',port=8099,debug = True)