import unittest
import model

class EventTest(unittest.TestCase):

  def setUp(self):
    self.event = model.Event()
    self.event.put()

  def tearDown(self):
    del self.event

  def testShouldPass(self):
    pass
    
  def testGetSubscriptions(self):
    subscription = model.Subscription()
    subscription.name = "Teste"
    subscription.email = "teste@gmail.com"
    self.event.add_subscription(subscription)
    assert subscription.key() == self.event.get_all_subscriptions()[0].key()
    
  def testAddSubscription(self):
    self.event.slots = 1
    subscription1 = model.Subscription()
    self.event.add_subscription(subscription1)
    assert subscription1.event.key() == self.event.key()
    
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
