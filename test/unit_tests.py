import unittest
import logging
from google.appengine.ext import db
import model

class SuccessFailError(unittest.TestCase):

    def setUp(self):
        logging.info('In setUp()')
        
    def tearDown(self):
        logging.info('In tearDown()')

    def test_success(self):
        logging.info('Running test_success()')
        self.assertTrue(True)

    def test_failure(self):
        logging.info('Running test_failure()')
        self.assertTrue(False)
        
    def test_error(self):
        logging.info('Running test_error()')
        raise Exception('expected exception')


class EventTest(unittest.TestCase):

  def setUp(self):
    # Populate test entities.
    event = model.Event()
    self.setup_key = entity.put()

  def tearDown(self):
    # There is no need to delete test entities.
    pass

  def testShouldPass(self):
    pass
