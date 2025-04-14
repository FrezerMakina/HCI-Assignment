from django.shortcuts import render
from .models import Student
from django.views.generic import ListView

# Create your views here.
class PostView(ListView):
    model = Student
    template_name = "Board/index.html"
    context_object_name = "student"

