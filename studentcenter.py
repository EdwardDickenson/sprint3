# Library imports
import webapp2
import jinja2
import os
import time
import datetime
import calendar
import unittest

from google.appengine.ext import ndb
from google.appengine.ext import testbed

# Project imports
from user import *
from util import *
from question import *

class StudentCenter(webapp2.RequestHandler):
    def get(self):
        uNm = getAccount(self.request.cookies.get("CurrentUser"))

        template = JINJA_ENVIRONMENT.get_template('Html/stdc.html')
        QL = list(Question.query())
        LL = list(Lecture.query())
        
        template_values = {
            "uNm" : uNm,
            "QL" : QL,
            "LL": LL
        }

        self.response.write(template.render(template_values))

    def post(self):
        question = Question()
        question.owner= self.request.cookies.get("CurrentUser")
        question.topic = self.request.get("topic")
        question.content = self.request.get("content")
        question.lec = self.request.get("class")
        question.time = datetime.datetime.now()
        question.answered = False
        question.message=[]
        
        lecture = self.request.get("lecture")

        question.put()
        self.redirect("/studentcenter" + "?quest" + self.request.get("Quest"))
