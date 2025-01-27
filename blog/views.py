from django.shortcuts import HttpResponse

# Create your views here.
def my_blog(request):
   return HttpResponse("Hello, Blog!")