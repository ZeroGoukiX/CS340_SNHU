from pymongo import MongoClient
from bson.objectid import ObjectId

class AnimalShelter(object):
    """ CRUD operations for Animal collection in MongoDB """

    def __init__(self, accuser, Dakota123):
            # Initializing the MongoClient. This helps to 
            # access the MongoDB databases and collections. 
            # Init connect to mongodb without authentication
            #self.client = MongoClient('mongodb://%s:%s@localhost:52210')
            self.client = MongoClient('mongodb://%s:%s@localhost:52210' % (accuser, Dakota123))
            self.database = self.client['AAC']
            
    def create(self, data):
        if data is not None:
            self.database.animals.insert(data)
            return True
        else:
            raise Exception("Nothing to save, because data parameter is empty")

    def read_all(self, data):
        cursor = self.database.animals.find(data, {'_id':False} )
        return cursor
        
    def read(self, data):
        return self.database.animals.find_one(data) ## returns only one document as a python dictionary
                                            
    def update(self, data, dataUpdate):
        if data is not None:
            self.database.animals.update(data,dataUpdate) #data should be in dictionary
        else:
            raise Exception("Nothing to save, because data parameter is empty")
    
    def delete(self, data):
        if data is not None:
            self.database.animals.remove(data) #data should be in dictionary
        else:
            raise Exception("Nothing to save, because data parameter is empty")  
                                            
                                            
                                            
                                            
                                            