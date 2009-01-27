from google.appengine.ext import db

class Event(db.Model):
    name = db.StringProperty()
    description = db.StringProperty(multiline=True)
    slots = db.IntegerProperty()
    
class Subscription(db.Model):
    name = db.StringProperty()
    email = db.EmailProperty()
    event = db.ReferenceProperty(Event)
    

