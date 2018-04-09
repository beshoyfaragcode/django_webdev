from django.contrib.syndication.views import Feed
from blog.models import Post,Category
from django.urls import reverse
from django.utils.feedgenerator import Atom1Feed

class RssSiteNewsFeed(Feed):
    title =" title"
    link = "/blog"
    description = "description"

    def items(self):
        return Post.objects.order_by('date')

    def item_title(self, item): 
        return Post.title

    def item_description(self, item):
        return Post.description

    def item_link(self, item):
        return reverse('post', args=[Post.slug])

    def link(self, obj):
        return Post.get_absolute_url()

class AtomSiteNewsFeed(RssSiteNewsFeed):
    feed_type = Atom1Feed
    subtitle = RssSiteNewsFeed.description