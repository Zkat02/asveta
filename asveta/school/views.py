from django.shortcuts import render

def index(request):
    return render(request, 'school/index.html')

def tutors(request):
    return render(request, 'school/for_tutors.html')

def blog(request):
    return render(request, 'school/blog.html')

def info(request):
    return render(request, 'school/info.html')

def recording(request):
    return render(request, 'school/recording.html')




