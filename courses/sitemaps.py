from django.contrib import sitemaps 
from django.urls import reverse

class VideosSitemap(sitemaps.Sitemap):
    changefreq = "daily"
    priority = 0.1

    def items(self):
        return ["courses:videos"]

    def location(self, item):
        return reverse(item)
    