#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
import webapp2
from google.appengine.api import mail
import logging

class MainHandler(webapp2.RequestHandler):
    def get(self):
        self.response.write('Hello world!')
    
    def post(self):
        user_address = self.request.get("email_address")
        
        to_address = "sgwooduk@gmail.com"        
        sender_address = "sgwooduk@gmail.com"
        subject = "ONABORA_ROBOT_SAY: email address received"
        body = """
                Dear Stephen,
                    I collected another email address:
                    
                    %s
                    
                    What is your bidding my master..?
                    """ % (user_address)
        logging.info("email_address=%s : %s --> %s"%(user_address,sender_address, to_address))
        mail.send_mail(sender_address, to_address, subject, body)

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
