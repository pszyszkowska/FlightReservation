from django.urls import path
from django.views.generic import TemplateView
import other.views

urlpatterns = [
    path("about/", TemplateView.as_view(template_name='about.html'), name="about"),
    path("contact/", TemplateView.as_view(template_name='contact.html'), name="contact"),
    path("contactform/", TemplateView.as_view(template_name='contactform.html'), name="contactform"),
    path("funfacts/", TemplateView.as_view(template_name='funfacts.html'), name="funfacts"),
    path("submitted/", other.views.submitted, name="submitted"),
]
