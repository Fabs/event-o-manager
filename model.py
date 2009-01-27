from google.appengine.ext import db

class Event(db.Model):
    name = db.StringProperty()
    description = db.StringProperty(multiline=True)
    slots = db.IntegerProperty()
    date = db.DateTimeProperty(auto_now_add=True)
    
    def get_all_subscriptions(self):
        subscriptions = Subscription.gql("WHERE event = :1",self.key()).fetch(1000)
        return subscriptions
        
    def get_all_enrolled(self):
        subscriptions = Subscription.gql("WHERE event = :1 ORDER date",self.key())fetch(self.slots)
        return subscriptions
        
    def get_all_waiting(self):
        subscriptions = Subscription.gql("WHERE event = :1 ORDER date",self.key()).fetch(1000, self.slots)
        return subscriptions
        
    def add_subscription(self, subscription):
        if Subscription.gql("WHERE event = :1 and email = :2", self.key(), subscription.email).count() > 0:
            raise AlreadySubscribedException, "This e-mail is already subscribed. If you didn't subscribe, wait for the validation to expire"
        subscription.event = self
        subscription.put()
        
    def count_subscriptions(self):
        num_subscriptions = Subscription.gql("WHERE event = :1",self.key()).count()
        return num_subscriptions
        
        
        
class Subscription(db.Model):
    name = db.StringProperty()
    email = db.EmailProperty()
    event = db.ReferenceProperty(Event)
    
    
class AlreadySubscribedException(Exception):
    pass
    

