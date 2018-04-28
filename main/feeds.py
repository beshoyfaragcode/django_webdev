from django.contrib.syndication.views import Feed
from blog.models import Post
from django.utils.feedgenerator import Atom1Feed

class RssSiteNewsFeed(Feed):
    title = "blog rss "
    link = "/blog/rss/"
    description = "blog rss and atom feeds ."

    def items(self):
        return Post.objects.all().order_by("date")[:10]

    def item_title(self, item):
        return item.title

    def item_description(self, item):
        return item.description


class AtomSiteNewsFeed(RssSiteNewsFeed):
    feed_type = Atom1Feed
    subtitle = RssSiteNewsFeed.description