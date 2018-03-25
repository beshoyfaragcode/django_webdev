from django.shortcuts import render,get_object_or_404
from blog.models import Post,Category


def categorylist (request,category_slug):
    categories = Category.objects.all()
    post = Post.objects.all()
    if category_slug:
      category = get_object_or_404(Category,slug = category_slug)
      post = Post.objects.filter(category = category)
      template = 'blog/category/listcategory.html'
      context = {'categories': categories,'post':post,'category':category}
    return render (request,template,context)
    
 

def blog(request):
 return render(request,'beshoy website/blog.html')
