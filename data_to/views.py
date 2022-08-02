from django.shortcuts import render

from data_to.models import Information
# Create your views here.
def index(request):
    if request.method=="POST":
        databaseData=Information()
        name=request.POST.get('name')
        city=request.POST.get('age')
        age=request.POST.get('city')
        
        databaseData.name=name
        databaseData.age=age
        databaseData.city=city
        databaseData.save()
        temp=22
    return render(request, 'index.html')  
def view(request):
    data= Information.objects.all()
    return render(request,'view.html',{'data':data})