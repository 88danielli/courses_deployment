from django.shortcuts import render, redirect
# from . import models
from . import models
# Create your views here.
def index(request):
    courses = models.Course.objects.all()
    context = {
        'courses': courses
    }
    return render(request, 'courses_app/index.html', context)

def add_course(request):
    models.Course.objects.create(course_name = request.POST['name'], description = request.POST['description'])
    return redirect('/')

def delete(request, id):
    courses_list = models.Course.objects.filter(id=id)
    course = courses_list[0]
    context = {
        'course' : course
    }
    if request.method == "GET":
        return render(request, 'courses_app/delete.html', context)
    course.delete()
    return redirect('/')
