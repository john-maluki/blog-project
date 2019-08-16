from django.urls import path
from . import views as search_views


urlpatterns = [
    path('search/', search_views.search, name='search'),
 ]  # + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
