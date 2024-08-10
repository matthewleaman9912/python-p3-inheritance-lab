#!/usr/bin/env python

from user import User

import random

class Teacher(User):
    def teach(self):
        return self.knowledge[random.randint(0,7)]
    