from django.urls import path, include
from .views import SignUpView, loginView


urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup'),
    path('login/', loginView,  name='login'),
    path('auth/', include('social_django.urls', namespace='social')),
]
