from django.db import models
from django.conf import settings
import pymongo
import datetime

_COLLECTION_NAME = getattr(settings, 'COLLECTION_NAME', 'logowl')

class LogOwlModel(models.Model):
    '''
    >>> for log in db.logowl.find({'ObjectName':'Genre', 'id': 7}):
    ...     print log
    ... 
    {u'ObjectName': u'Genre', u'title': u'Dub', u'Timestamp': datetime.datetime(2011, 5, 1, 21, 59, 33, 778000), u'id': 7, u'_id': ObjectId('4dbdd7c59601e41e96000004'), u'slug': u'dub'}
    {u'ObjectName': u'Genre', u'title': u'Nsdasdpaddas', u'Timestamp': datetime.datetime(2011, 5, 1, 22, 1, 35, 66000), u'id': 7, u'_id': ObjectId('4dbdd83f9601e41e9600001d'), u'slug': u'dub'}
    {u'ObjectName': u'Genre', u'title': u'Folk Metal', u'Timestamp': datetime.datetime(2011, 5, 1, 22, 1, 51, 480000), u'id': 7, u'_id': ObjectId('4dbdd84f9601e41e9600001e'), u'slug': u'folk-metal'}
    {u'ObjectName': u'Genre', u'title': u'M\xfasica Folcl\xf3rica', u'Timestamp': datetime.datetime(2011, 5, 1, 22, 2, 6, 947000), u'id': 7, u'_id': ObjectId('4dbdd85e9601e41e9600001f'), u'slug': u'folclorica'}
    {u'ObjectName': u'Genre', u'title': u'Folk', u'Timestamp': datetime.datetime(2011, 5, 1, 22, 2, 14, 165000), u'id': 7, u'_id': ObjectId('4dbdd8669601e41e96000020'), u'slug': u'folk'}

    '''

    connection = database = logowl = None
    
    class Meta:
        abstract = True

    def save(self, *args, **kwargs):
        
        
        super(LogOwlModel, self).save(*args, **kwargs)

        print "The LogOwl acting..."
        self.LogOwl(*args, **kwargs)

    def prepareCollection(self):
        self.connection = pymongo.Connection("localhost", 27017)
        self.database = self.connection.database
        self.logowl = self.database.logowl

    def LogOwl(self, *args, **kwargs):
        self.prepareCollection()

        log = {
            'Timestamp': datetime.datetime.utcnow(),
            'ObjectName': self._meta.object_name,
        }
        for x in self._meta._fields():
            log.update({x.name : self.serializable_value(x.name)})
        
        self.logowl.save(log)
