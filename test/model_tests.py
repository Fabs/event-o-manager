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

        
