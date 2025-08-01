from django.shortcuts import render,redirect
from .models import LostItem, FoundItem
from .forms import LostItemForm, FoundItemForm

# Create your views here.

def lost_view(request):
    if request.method == 'POST':
        form = LostItemForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = LostItemForm()
    return render(request, 'items/lost_form.html',{'form':form})

def found_view(request):
    if request.method == 'POST':
        form = FoundItemForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')  
    else:
        form = FoundItemForm() 
    return render(request, 'items/lost_form.html',{'form':form})             