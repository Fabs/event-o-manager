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

        
