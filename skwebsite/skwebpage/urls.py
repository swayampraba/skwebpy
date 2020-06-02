from django.urls import path 
from . import views 

urlpatterns=[path('', views.index, name='index'),
             path("aboutus", views.aboutus, name="aboutus"),
             path("academy", views.academy, name="academy"),
             path("auditing", views.auditing, name="auditing"),
             path("solutions", views.solutions, name="solutions"),
             path("syservices", views.syservices, name="syservices"),
             path("blog", views.blog, name="blog"),
             path("gallery", views.gallery, name="gallery"),
             path("contact", views.contact, name="contact")
             ] 