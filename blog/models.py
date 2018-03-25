from django.db import models


from django.core.urlresolvers import reverse
class Category(models.Model):
 name = models.CharField (max_length = 160)
 slug =  models.SlugField(max_length = 160,unique=True)
 date = models.DateTimeField()
 class meta :
    ordering = ('name',)
    verbose_name = 'category'
    verbose_name_plural = 'categories'
 def get_absolute_url(self ):
        
      return "/blog/Category/%s" % self.slug   
 def __str__(self):
    return self.name
 def __unicode__(self):
    return self.name

class Post(models.Model):
  title = models.CharField (max_length = 160)
  body = models.TextField()
  date = models.DateTimeField()
  author =  models.CharField (max_length = 160)
  description = models.TextField(max_length = 160)
  keywords = models.TextField()
  category = models.ForeignKey(Category)
  slug =  models.SlugField(max_length = 160,unique=True)
  img_url = models.URLField()
  short_blog_snippet=  models.CharField(max_length = 15)
  absolute_url = models.CharField(max_length=400, blank=True, editable=False)

  def __str__(self):
    
    return self.title
  
  def get_absolute_url(self ):
        
     return "/blog/%s" % self.slug
  def __unicode__(self):
    return self.title




