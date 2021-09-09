from django.shortcuts import render
from .forms import NewMessageForm
from .models import comments
from django.shortcuts import get_object_or_404, render, redirect
# Create your views here.

def index(request):
    context={
        'posts':comments.objects.all()
    }
    return render(request, 'home/index.html',context)

def service(request):
    return render(request, 'home/service.html')

def about(request):
    return render(request, 'home/about.html')

def profile(request):
    return render(request, 'home/profile.html')

def contacts(request):
    if request.method == 'POST':
        form = NewMessageForm(request.POST)
        print("in the comment save 1")
        if form.is_valid():
            print("in the comment save 2")
            data = form.save(commit=False)
            # data.post = post
			# data.username = user
            data.save()
            return redirect('contacts')
    else:
        form = NewMessageForm()
	
    # return render(request,'blog/single_blog.html', {'post':post, 'form':form})
    return render(request, 'home/contacts.html')