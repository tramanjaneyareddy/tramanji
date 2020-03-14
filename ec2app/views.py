from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def m1(request):

   return render(request,'aws.html')