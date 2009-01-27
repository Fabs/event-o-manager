import unittest
import model

class EventTest(unittest.TestCase):

  def setUp(self):
    self.event = model.Event()

  def tearDown(self):
    pass

  def testShouldPass(self):
    pass
    
  def testGetSubscriptions(self):
    subscription = model.Subscription()
    subscription.name = "Teste"
    subscription.email = "teste@gmail.com"
    self.event.put()
    subscription.event = self.event
    subscription.put()
    assert subscription.key() == self.event.get_all_subscriptions()[0].key()
    
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
