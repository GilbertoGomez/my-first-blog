from django.shortcuts import render,get_object_or_404,redirect
from django.utils import timezone
from .models import Post
from .forms import PostForm
from django.contrib.auth import authenticate, login
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib import auth
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render
from django.db.models import Q
import json
# Create your views here.

def busqueda(request):
	posts = Post.objects.all()
	query = request.GET.get("b");
	#if query.is_ajax():
		#query = request.GET.get("q");
		#posts_list = Post.objects.filter(nombre__startswith= request.GET['nombre'] ).values('nombre', 'id')
	if query:
		posts = posts.filter(
			Q(title__icontains=query)|
			Q(text__icontains=query)|
			Q(author__username__contains=query)
			).distinct()
	return posts

def index(request):
	return render(request, 'blog/index.html')

def post_list(request):
	posts = Post.objects.all()
	posts = busqueda(request)
	paginator = Paginator(posts, 5)
	page = request.GET.get('page')
	try:
		posts = paginator.page(page)
	except PageNotAnInteger:
		posts = paginator.page(1)
	except EmptyPage:
		posts = paginator.page(paginator.num_pages)
	return render(request, 'blog/post_list.html', {'posts':posts})

def post_detail(request,pk):
	post = get_object_or_404(Post,pk=pk)
	return render(request, 'blog/post_detail.html', {'post':post})

@login_required(login_url="/accounts/login/")
def post_new(request):
	if request.method == "POST":
		form = PostForm(request.POST)
		if form.is_valid():		
			post = form.save(commit=False)
			post.author = request.user
			post.published_date = timezone.now()
			post.save()
			return HttpResponseRedirect("/")
	else:
		form = PostForm()
	return render(request, 'blog/post_edit.html', {'form': form})

def login(request):
	next = request.GET.get('next','/')
	if request.method == "POST":
		username = request.POST.get['username']
		password = request.POST.get['password']
		user = authenticate(username=username, password=password)
		if user is not None:
			if user.is_active:
				login(request, user)
				return HttpResponseRedirect(next)
				# Redirect to a success page.
			else:
				# Return a 'disabled account' error message
				HttpResponse("no");
		else:
			HttpResponseRedirect(settings.LOGIN_URL)
	return render(request, 'admin/login.html', {'home': home})