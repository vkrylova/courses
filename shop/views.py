from django.shortcuts import render
from django.http import HttpResponse
from .models import Category, Course


def index(request):
    courses = Course.objects.all()
    return render(request, 'courses.html', context={'courses': courses})