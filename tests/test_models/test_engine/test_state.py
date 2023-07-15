#!/usr/bin/python3
""" test State """
import unittest
import pep8
from models.state import State

class State_testing(unittest.TestCase):
    """ check BaseModel class"""

    def testpep8(self):
        """ test codestyle """
        pepstylecode = pep8.StyleGuide(quiet=True)
        path_user = 'models/state.py'
        result = pepstylecode.check_files([path_user])
        self.assertEqual(result.total_errors, 0,
                         "if found code style error")
