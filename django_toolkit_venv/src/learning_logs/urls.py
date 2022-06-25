# Define URLs for learnning_logs
from django.urls import path # import path function -> it is needed when mapping URLs to views
from . import views # import the views module (dot tells python it is in the same directory as urls.py)

app_name = 'learning_logs' # this variable helps Django distinguish this urls.py from other urls.py files

# urlpatterns is a list of individual pages that can be requested from the learning_logs app
urlpatterns = [
    # Home page
    path('', views.index, name = 'index'), # URL pattern is a call to path function
    # empty string "" matches the base URL
    # views.index specifies to call index function in views.py
    # name = 'index' specifies a name for a URL pattern so that I can refer to it in other sections of the code
    # index is the agreed upon name for the home page
    
    # Page with all the topics
    path('topics/', views.topics, name = 'topics'),

    # Detail page for a single topic
    # The <int:topic_id> tells Django to look for URLs that have /topic after base url and then
    # It matches an integer betwee // and stores it in an argument called topic_id
    # Example: /topics/1/
    path('topics/<int:topic_id>/', views.topic, name = 'topic'),
]