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