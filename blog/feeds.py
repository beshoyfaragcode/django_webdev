from django.contrib.syndication.views import Feed
from blog.models import Post,Category
from django.urls import reverse
from django.utils.feedgenerator import Atom1Feed

class RssSiteNewsFeed(Feed):
    title = Post.title
    link =  Post.get_absolute_url
    description =  Post.description

    def items(self):
        return Post.objects.order_by('date')

    def title(self,items): 
        return Post.title

    def description(self, items):
        return Post.description

    def link(self,items):
        return  Post.get_absolute_url()

  

class AtomSiteNewsFeed(RssSiteNewsFeed):
    feed_type = Atom1Feed
    subtitle = RssSiteNewsFeed.description