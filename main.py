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
import random

page_header = """
<!DOCTYPE html>
<html>
<head>
    <title>Fortune Title</title>
</head>
<body>
    <h1>Ara's Fortune Cookie App First Title</h1>
"""

page_footer = """
</body>
</html>
"""

#chooses a random fortune
def getRandomFortune():
    fortunes = ["You're going to live!", "Sorry, you're going to die.", "Try again"]
    index = random.randint(0,2)
    return fortunes[index]

class MainHandler(webapp2.RequestHandler):
    def get(self):

        fortune = getRandomFortune()
        fortune_paragraph = "<p> Your fortune is: " + fortune + "</p>\n"

        lucky_number = random.randint(1,100)
        number_sentence = "Your lucky number is: " + str(lucky_number)
        number_paragraph = "<p>" + number_sentence + "</p>\n"

        try_again = "<a href='.'>Another cookie please</a>"

        content = page_header + fortune_paragraph + number_paragraph + try_again
        self.response.write(content + page_footer)

class LoginHandler(webapp2.RequestHandler):
    def get(self):
        header = "<h1>Please Log In...you can't... but thanks for trying</h1>"
        lucky_number = random.randint(1,100)
        number_sentence = "You're lucky number is: " + str(lucky_number)
        number_paragraph = "<p>" + number_sentence + "</p>"
        self.response.write(header + number_paragraph)


routes = [('/', MainHandler),
          ('/login', LoginHandler)]
app = webapp2.WSGIApplication(routes, debug=True)
