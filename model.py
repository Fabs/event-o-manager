from google.appengine.ext import db

class Event(db.Model):
    name = db.StringProperty()
    description = db.StringProperty(multiline=True)
    slots = db.IntegerProperty()
    
    def get_all_subscriptions(self):
        subscriptions = Subscription.gql("WHERE event = :1",self.key()).fetch(1000)
        return subscriptions
        
    def add_subscription(self, subscription):
        if self.slots <= self.count_subscriptions():
            raise SlotLimitException, "No slot for you!"
        subscription.event = self
        subscription.put()
        
    def count_subscriptions(self):
        num_subscriptions = Subscription.gql("WHERE event = :1",self.key()).count()
        return num_subscriptions
        
        
        
class Subscription(db.Model):
    name = db.StringProperty()
    email = db.EmailProperty()
    event = db.ReferenceProperty(Event)
    
    
class SlotLimitException(Exception):
    pass
    

