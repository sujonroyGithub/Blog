from .forms import SignUpForm,LoginForm, PostForm
from django.shortcuts import render,HttpResponseRedirect
from django.contrib import messages
from datetime import datetime
from django.contrib.auth import authenticate , login, logout
from.models import Blog_Post, Contact
from django.contrib.auth.models import Group
# Create your views here.
def home(request):
    posts = Blog_Post.objects.all()
    return render(request, 'blog/home.html' , {'posts' : posts} )
def about(request):
    return render(request, 'blog/about.html' )
def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        address = request.POST.get('address')
        desc = request.POST.get('desc')
        
        
        contact = Contact(name=name,email=email,address=address,desc=desc,date=datetime.today())
        contact.save()
        
        messages.success(request, ' Your Information Has been Sent Sucessfully..')
      
    return render(request, 'blog/contact.html' )
def dashboard(request):
   if request.user.is_authenticated:
        
    posts= Blog_Post.objects.all()
    user = request.user
    full_name=user.get_full_name()
    gps = user.groups.all()
    return render(request, 'blog/dashboard.html',{'posts':posts , 'full_name':full_name, 'groups':gps} )
   else:
     return  HttpResponseRedirect("/login/")
def user_singup(request):
  
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            messages.success(request,"Congratulations! You have become a auther.")
            user=form.save()
            group = Group.objects.get(name = 'Author')
            user.groups.add(group)
    else:
    
     form =SignUpForm()
    return render(request, 'blog/singup.html', {'form' : form} )
def user_logout(request):
    logout(request)
    return HttpResponseRedirect("/")
def user_login(request):
    if not  request.user.is_authenticated:
        
     if request.method == "POST":
        form = LoginForm(request=request, data = request.POST)
        if form.is_valid():
            uname = form.cleaned_data['username']
            upass = form.cleaned_data['password']
            user = authenticate(username=uname , password=upass)
            if user is not None:
                login(request, user)
                messages.success(request,"Logged in Successfully!!")
                return HttpResponseRedirect('/dashboard/')
     else:

      form =LoginForm()
     return render(request, 'blog/login.html',{'form' : form} )
    else:
     return HttpResponseRedirect("/dashboard/")

def add_post(request):
    if request.user.is_authenticated:
        if request.method =="POST":
         form = PostForm(request.POST)
         if form.is_valid():
            title = form.cleaned_data['title']
            desc = form.cleaned_data['desc']
            pst = Blog_Post(title= title, desc=desc)
            pst.save()
            form = PostForm()
        else:
            form = PostForm()
        return render(request, 'blog/add_post.html', {'form':form})
    else:
        return HttpResponseRedirect("/login/")
def update_post(request, id):
    if request.user.is_authenticated:
        if request.method =="POST":
            pi = Blog_Post.objects.get(pk=id)
            form = PostForm(request.POST, instance=pi)
            if form.is_valid():
                form.save()
        else:
            pi = Blog_Post.objects.get(pk=id)
            form = PostForm(instance=pi)
        return render(request, 'blog/update_post.html', {'form':form})
    else:
        return HttpResponseRedirect("/login/")
def delete_post(request , id):
    if request.user.is_authenticated:
        if request.method =="POST":
            pi = Blog_Post.objects.get(pk=id)
            pi.delete()
        return HttpResponseRedirect("/dashboard/")
    else:
        return HttpResponseRedirect("/login/")
    
    


     