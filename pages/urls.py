from django.urls import path
from . import views
from django.conf import settings
from django.contrib.staticfiles.urls import static, staticfiles_urlpatterns


urlpatterns = [
    path('',views.home, name='home'),
    path('about/',views.about, name='about'),
    path('services/',views.services, name='services'),
    path('contact/',views.contact, name='contact'),
]
urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
