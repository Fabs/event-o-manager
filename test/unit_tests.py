import unittest
import model

class EventTest(unittest.TestCase):

  def setUp(self):
    self.event = model.Event()

  def tearDown(self):
    pass

  def testShouldPass(self):
    pass
    
class SubscriptionTest(unittest.TestCase):

  def setUp(self):
    self.subscription = model.Subscription()

  def tearDown(self):
    pass

  def testShouldPass(self):
    pass
    
  def testShouldCreateSubscription(self):
    self.subscription.name = "Teste"
    self.subscription.email = "teste@gmail.com"
    event = model.Event()
    event.put()
    self.subscription.event = event
    self.subscription.put()
