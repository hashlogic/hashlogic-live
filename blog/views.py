from django.shortcuts import render
from .models import Post
from django.views.generic import DetailView
from .forms import NewCommentForm
from django.shortcuts import get_object_or_404, render, redirect
# Create your views here.

def blog(request):
    context={
        'posts':Post.objects.all()
    }
    return render(request,'blog/blog.html',context)

# class PostDetailView(DetailView):
#     model = Post

def single_blog(request,pk):
    post = get_object_or_404(Post, pk=pk)
	# user = request.user
	# is_liked =  Like.objects.filter(user=user, post=post)
    print("in the comment save 0")
    if request.method == 'POST':
        form = NewCommentForm(request.POST)
        print("in the comment save 1")
        if form.is_valid():
            print("in the comment save 2")
            data = form.save(commit=False)
            data.post = post
			# data.username = user
            data.save()
            return redirect('single_blog', pk=pk)
    else:
        form = NewCommentForm()
	
    return render(request,'blog/single_blog.html', {'post':post, 'form':form})