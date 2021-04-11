import os

# Logger Configuration
LOG_LEVEL = 'INFO'

# Webserver Configuration
WEB_HOST = '0.0.0.0'
WEB_PORT = 8080
WEB_DEBUG = False
WEB_USER = os.environ.get('username', 'admin')
WEB_PASSW = '12345'
WEB_LOG = 'calender.log'

# Web Security
# Setting this to True will return all responses with security headers.
WEB_SECURITY = True
WEB_SEC_HEADERS = {
  'CSP':"default-src *; style-src 'self' 'unsafe-inline'; script-src 'self' 'unsafe-inline' 'unsafe-eval'",
  'CTO':'nosniff',
  'XSS':'1; mode=block',
  'XFO':'DENY',
  'RP':'no-referrer',
  'Server':'calender'
}

# Maximum allowed attempts before banning the remote origin
MAX_LOGIN_ATTEMPTS = 5

# Redis Configuration
# This should not be set to anything else except localhost unless you want to do a multi-node deployment.
RDS_HOST = '127.0.0.1'
RDS_PORT = 6379
RDS_PASSW = None

# Scan Configuration
USER_AGENT = 'calender'


