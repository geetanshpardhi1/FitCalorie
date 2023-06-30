from django.shortcuts import render,redirect
from .models import Food,Consume
from django.contrib.auth.models import User
# Create your views here.
def index(request):
   
    
    if request.method == "POST":
        
        foodconsume = request.POST['foodconsume']
        consume = Food.objects.get(name=foodconsume)
        user = request.user
        
        #saving data to consume model
        c = Consume(user=user,food_consumed=consume)
        c.save()
        food = Food.objects.all()
         
    else:
      
        food = Food.objects.all()
    consumed_food = Consume.objects.filter(user=request.user)
    return render(request,'myapp/index.html',{'foods':food,'consumed_food':consumed_food})

def delete_consume(request,id):
    consume = Consume.objects.get(id=id)
    if request.method == "POST":
        consume.delete()
        return redirect('/')
    
    else:
        return render(request,'myapp/delete.html')