from django.shortcuts import render

def index(request):
    # logger.debug("index")
    return render(request, 'school/index.html')