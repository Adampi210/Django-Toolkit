from django.db import models # models module is already imported 0

# For the learning logs there will be a few models (classes)

# The first class is the topic (the notes will have different topics so this is to put them in proper places)

class Topic(models.Model): # inherit from the Model class (included in Django, provides basic model functionality)
    # A topic of the notes
    
    # attributes:
    text = models.CharField(max_length = 200) # title of a topic -> text is a CharField = a piece of data made up of characters to store short strings
    date_added = models.DateTimeField(auto_now_add = True) # date_added is a DateTimeField = a piece of data recording a date and time.\
    # The argument inside tells Django to automatically set this attribute to the current date and time when a new topic is created
    # For more kinds of fields that can be used in a model see: https://docs.djangoproject.com/en/4.0/ref/models/fields/

    def __str__(self):
        return self.text

# Each topic will have several entries
class Entry(models.Model): # As before Entry inherits from Model class

    topic = models.ForeignKey(Topic, on_delete = models.CASCADE) # topic attribute is a ForeignKey instance
    # which means it is a reference to another record in the database (in this case to topic)
    # It is used to create a relationship within the data (each entry is related to one topic)
    # This works because each topic has an ID associated to it (a key), so an entry can be linked to that ID
    # on_delete = models.CASCADE makes it so that when a Topic is deleted all Entries associated with it will also be deleted

    text = models.TextField() # Text field to put the notes in
    date_added = models.TimeField(auto_now_add = True) # stores when Entry was added

    # class Meta holds extra information for managing a model
    # here it sets the plural name to entries (not Entrys)
    class Meta:
        verbose_name_plural = 'entries'
    
    # return a string representation of an entry
    def __str__(self):
        str_len = len(self.text)
        if(str_len <= 50):
            return self.text
        else:
            str_to_return = self.text[:50] + '...'# return only first 50 characters
            return str_to_return
