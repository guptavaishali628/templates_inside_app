from django.shortcuts import render
from django.http import JsonResponse

# Create your views here.
def student(request):
    data={"Name" : "vaishali", "age" : 19, "qualification" : "BCA"}
    return JsonResponse(data) #JsonResponse=return data in key value pair

    
def registration(request):
    return render(request,'home.html')