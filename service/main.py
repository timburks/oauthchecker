#!/usr/bin/env python

import hashlib, re, sys
from google.appengine.ext import webapp
from google.appengine.ext.webapp import util
from google.appengine.api import users
from google.appengine.api import oauth

class OAuthHandler(webapp.RequestHandler):
	def get(self):
            try:
	        self.response.out.write(oauth.get_oauth_consumer_key())
	        self.response.out.write("\n")           
	        self.response.out.write(oauth.get_current_user().nickname())
	        self.response.out.write("\n")           
            except oauth.InvalidOAuthParametersError:
                self.response.out.write("Invalid OAuth parameters.\n")
            except oauth.InvalidOAuthTokenError:
                self.response.out.write("Invalid OAuth token.\n")
            except e:
                self.response.out.write("Nothing to see here.\n")

def main():
    application = webapp.WSGIApplication([('/', OAuthHandler)], debug=True)
    util.run_wsgi_app(application)

if __name__ == '__main__':
    main()
