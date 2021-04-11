import config
import os

from core.redis   import rds
#from core.workers import start_workers

from version import VERSION
from flask   import Flask
from datetime import datetime

# Import Blueprints
from views.view_index      import index
from views.view_login      import login
from views.view_logout     import logout
from views.view_calender   import calender


app = Flask(__name__)

# Initialize Blueprints
app.register_blueprint(index)
app.register_blueprint(login)
app.register_blueprint(logout)
app.register_blueprint(calender)

app.config.update(
  SESSION_COOKIE_SAMESITE='Strict',
)
app.secret_key = os.urandom(24)

# Set Security Headers
@app.after_request
def add_security_headers(resp):
  if config.WEB_SECURITY:
    resp.headers['Content-Security-Policy'] = config.WEB_SEC_HEADERS['CSP']
    resp.headers['X-Content-Type-Options'] = config.WEB_SEC_HEADERS['CTO']
    resp.headers['X-XSS-Protection'] = config.WEB_SEC_HEADERS['XSS']
    resp.headers['X-Frame-Options'] = config.WEB_SEC_HEADERS['XFO']
    resp.headers['Referrer-Policy'] = config.WEB_SEC_HEADERS['RP']
    resp.headers['Server'] = config.WEB_SEC_HEADERS['Server']
  return resp  


@app.context_processor
def show_version():
  return dict(version=VERSION)

if __name__ == '__main__':  
  #rds.initialize()
  #start_workers()
  app.run(debug = True, 
          host  = config.WEB_HOST, 
          port  = config.WEB_PORT,
          threaded=True,
          use_evalex=False)
