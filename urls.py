from django.urls import path

from .views import HomePageView, AboutPageView, IndexPageView, ContactPageView

urlpatterns = [
    path('about/', AboutPageView.as_view(), name='about'),
    path('', HomePageView.as_view(), name='home'),
    path('index/', IndexPageView.as_view(), name='index'),
    path('contact/', ContactPageView.as_view(), name='contact'),
    path('index/', IndexPageView.as_view(), name='main-section'),
    path('index/', IndexPageView.as_view(), name='about-me'),
    path('index/', IndexPageView.as_view(), name='services'),
    path('index/', IndexPageView.as_view(), name='clients'),
    path('index/', IndexPageView.as_view(), name='portfolio'),
    path('index/', IndexPageView.as_view(), name='blog'),
    path('index/', IndexPageView.as_view(), name='partners'),
]
