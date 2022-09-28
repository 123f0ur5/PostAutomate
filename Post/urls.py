from django.urls import path
from .views import create_post, list_view, list_post, manage_view, view_facebook

urlpatterns = [
    path('create/', create_post, name='create'),
    path('teste/', view_facebook, name='teste'),
    path('scheduled/', list_post, name='scheduled'),
    path('manage/', manage_view, name='manage'),
    path('list/<int:my_id>', list_view),
]