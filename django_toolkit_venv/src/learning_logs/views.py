from django.shortcuts import render # import render function to render resopnses based on data from views
from .models import Topic # import topic model from the models file
# Create your views here.

def index(request):
    """Learning Log Home Page"""
    # render function has two arguments - request from a url and a template 
    # it uses to build the page
    return render(request, 'learning_logs/index.html')

def topics(request):
    """Learning Log Topics Page"""
    # The topics page needs to retrieve data from the database
    # I ask the database for Topic objects sorted by the date added
    topics = Topic.objects.order_by('date_added')

    # Then I define a dictionary with the name context with key topics and value as the set of topics
    context = {'topics':topics}

    # Then render function is returned to build the page, this time called with context
    # Passing context is necessary when building a page that uses data
    return render(request, 'learning_logs/topics.html', context)

def topic(request, topic_id):
    """Individual topic page."""
    # First get the topic by its id
    # This is the same command as in Django shell
    topic = Topic.objects.get(id = topic_id)

    # Then get entries associated with the topic and order according to date added
    # - tells the order to be reversed (most recent first)
    entries = topic.entry_set.order_by('-date_added')

    # Finally store everything in context dictionary
    context = {'topic':topic, 'entries': entries}
    return render(request, 'learning_logs/topic.html', context)