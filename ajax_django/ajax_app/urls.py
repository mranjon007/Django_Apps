from django.urls import path, include
from .views import *


urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup'),
    path('ajax/validate_username/', validate_username, name='validate-username'),
]
