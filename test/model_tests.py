#!/usr/bin/python2.4
# -*- coding: utf-8 -*
#
#
"""Datastore model tests for Event-o-Manager"""

__author__ = 'rodolpho@google.com (Rodolpho Eckhardt)'

import model
import unittest


class EventTest(unittest.TestCase):
  def testSimplePutAndGet(self):
    event = model.Event(
        name='TestEvent',
        description='This is a simple test event.\nThis is a multiline text.',
        slots=10
    )
    event.put()
    query = model.Event.gql('WHERE name = :1', 'TestEvent')
    results = query.fetch(1)
    verify_event = results[0]
    self.assertEquals(event.name, verify_event.name)
    self.assertEquals(event.description, verify_event.description)
    self.assertEquals(event.slots, verify_event.slots)
    self.assertEquals(event.key(), verify_event.key())
    event.delete()

  def testAddSubscription(self):
    event = model.Event(
        name='TestEvent',
        description='This is a test event.',
        slots=1
    )
    event.put()
    subscription = model.Subscription()
    event.add_subscription(subscription)
    self.assertEquals(subscription.event.key(), event.key())
    subscription.delete()
    event.delete()

  def testGetSubscriptions(self):
    event = model.Event(
        name='TestEvent',
        description='This is a test event.',
        slots=1
    )
    event.put()
    subscription = model.Subscription(
        name='TestSubscription',
        email='test@gmail.com'
    )
    event.add_subscription(subscription)
    self.assertEquals(subscription.key(), 
                      event.get_all_subscriptions()[0].key())
    subscription.delete()
    event.delete()

  def testSlotsLimit(self):
    event = model.Event(
        name='TestEvent',
        description='This is a test event.',
        slots=1
    )
    event.put()
    subscription = model.Subscription(
        name='TestSubscription',
        email='test@gmail.com'
    )
    event.add_subscription(subscription)
    second_subscription = model.Subscription(
        name='SecondSubscription',
        email='error@gmail.com',
    )
    self.assertRaises(model.SlotLimitException,
                      event.add_subscription,
                      second_subscription)
    subscription.delete()
    event.delete()

        
class SubscriptionTest(unittest.TestCase):
  def testSimplePutAndGet(self):
    event = model.Event(
        name='TestEvent',
        description='Simple test description.',
        slots=10
    )
    event.put()
    subscription = model.Subscription(
        name='TestSubscription',
        email='test@gmail.com',
        event=event
    )
    subscription.put()
    query = model.Subscription.gql('WHERE email = :1', 'test@gmail.com')
    results = query.fetch(1)
    verify_subscription = results[0]
    self.assertEquals(subscription.name, verify_subscription.name)
    self.assertEquals(subscription.email, verify_subscription.email)
    self.assertEquals(subscription.key(), verify_subscription.key())
    subscription.delete()
    event.delete()
