from django.shortcuts import render
from .models import car
from .forms import carform , UserRegistrationForm
# from django.shortcuts import get
from django.shortcuts import get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login

# Create your views here.
def index(request):
    return render(request,'index.html')

def car_list(request):
    cars = car.objects.all().order_by('-created_at')
    return render(request,'car_list.html',{'cars':cars})

@login_required
def create_listing(request):
    if request.method=="POST":
        form = carform(request.POST, request.FILES)
        if form.is_valid():
            cars1 = form.save(commit = False)
            cars1.user = request.user
            cars1.save()
            return redirect('car_list')
    else:
        form = carform()
    return render(request,'car_form.html',{'form':form})

@login_required    
def edit_listing(request, car_id):
    cars1 = get_object_or_404(car,pk = car_id,user = request.user)
    if request.method== 'POST':
        form = carform(request.POST,request.FILES,instance = cars1)
        if form.is_valid():
            cars1 = form.save(commit = False)
            cars1.user = request.user
            cars1.save()
            return redirect('car_list')
    
    else:
        form = carform(instance = cars1)
    return render(request,'car_form.html',{'form':form})

@login_required
def delete_listing(request, car_id):
    cars1 = get_object_or_404(car, pk = car_id, user = request.user)
    if request.method == 'POST':
        cars1.delete()
        return redirect('car_list')
    return render(request, 'car_conf_delete.html', {'car':cars1})

def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit = False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            login(request, user)
            return redirect('car_list')
    else:
        form = UserRegistrationForm()
    return render(request, 'registration/register.html', {'form':form})