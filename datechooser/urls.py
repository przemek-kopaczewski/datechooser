from django.urls import path
from datechooser.views import index, create_event

urlpatterns = [
    path('', index, name='index'),
    path('create-event/', create_event, name="create_event"),
]
