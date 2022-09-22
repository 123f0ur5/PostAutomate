from django.shortcuts import render
from .forms import PostForm
from .models import Post
from django.contrib.auth.decorators import login_required

#Create your views here.
@login_required
def create_post(request):
	if request.method == 'POST':
		post = PostForm(request.POST, request.FILES)
		if post.is_valid():
			post = post.save(commit=False)
			post.user = request.user
			post.save()
			post = PostForm()
	else:
		post = PostForm()
	return render(request, "create_post.html", {'my_post' : post})

@login_required
def manage_view(request):
	return render(request, "manage_accounts.html")

@login_required
def list_post(request):
	queryset = Post.objects.filter(user=request.user)
	return render(request, "list_all.html", {'post_list' : queryset})

@login_required
def list_view(request, my_id):
	req_user = request.user
	post = Post.objects.get(id=my_id)
	context = {
		'post' : post,
		'req_user' : req_user,
	}

	return render(request, "list.html", context)	