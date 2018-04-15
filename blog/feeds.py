from django.contrib.syndication.views import Feed
from blog.models import Post,Category
from django.urls import reverse
from django.utils.feedgenerator import Atom1Feed

class RssSiteNewsFeed(Feed):
   title = "Posts for bedjango starter"
   link = "/feeds/"
   description = "Updates on changes and additions to posts published in the starter."

   def items(self):
       return Post.objects.order_by('date')[:5]

   def item_title(self, item):
       return Post.title

   def item_description(self, item):
       return Post.description


   

class AtomSiteNewsFeed(RssSiteNewsFeed):
    feed_type = Atom1Feed
    subtitle = RssSiteNewsFeed.description