from django.shortcuts import render,redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.sitemaps import Sitemap
from blog.models import Post,Category
def index (request):
 return render(request,'beshoy website/home.html')
def about (request):
 return render(request,'beshoy website/about.html')
def main (request):
 return render(request,'beshoy website/home.html')
def school (request):
 return render(request,'beshoy website/myschool.html')
def life (request):
 return render(request,'beshoy website/mylif.html')
def todo(request):
 return render(request,'beshoy website/todo.html')
def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('/home.html/')
    else:
        form = UserCreationForm()
    return render(request, 'beshoy website/signuppage.html', {'form': form})

class BlogSitemap(Sitemap):
    changefreq = "daily"
    priority = 1.0

    def items(self):
        return Post.objects.all()

    def lastmod(self, obj):
        return obj.date
class CategorySitemap(Sitemap):
    changefreq = "daily"
    priority = 1.0

    def items(self):
        return Category.objects.all()

    def lastmod(self, obj):
        return obj.date


