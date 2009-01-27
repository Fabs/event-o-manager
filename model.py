from google.appengine.ext import db

class Event(db.Model):
    name = db.StringProperty()
    description = db.StringProperty(multiline=True)
    slots = db.IntegerProperty()
    
    def get_all_subscriptions(self):
        subscriptions = Subscription.gql("WHERE event = :1",self.key()).fetch(1000)
        return subscriptions
    
class Subscription(db.Model):
    name = db.StringProperty()
    email = db.EmailProperty()
    event = db.ReferenceProperty(Event)
    

