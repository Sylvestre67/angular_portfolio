from django.db import models
from django.contrib.sitemaps import Sitemap
from django.utils.text import slugify

class blogPost(models.Model):
    title = models.CharField(max_length=256)
    slug = models.CharField(max_length=256)
    excerpt = models.CharField(max_length=1000,null=True,blank=True)
    content = models.TextField()
    image = models.ImageField(upload_to='blog', null=True, blank=True)
    created_on = models.DateField(auto_now_add=True)

    def __unicode__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(blogPost, self).save(*args, **kwargs)


class portfolioPost(models.Model):
    title = models.CharField(max_length=256)
    slug = models.CharField(max_length=256)
    excerpt = models.CharField(max_length=1000,null=True,blank=True)
    content = models.TextField(null=True,blank=True)
    image = models.ImageField(upload_to='portfolio',null=True)
    created_on = models.DateTimeField(auto_now_add = True)
    modified_on = models.DateTimeField(auto_now = True,null=True)

class blogPostSitemap(Sitemap):
    changefreq = "never"
    priority = 0.5

    def items(self):
        return blogPost.objects.all()

    def lastmod(self, obj):
        return obj.modified_on

class portfolioPostSitemap(Sitemap):
    changefreq = "never"
    priority = 0.5

    def items(self):
        return portfolioPost.objects.all()

    def lastmod(self, obj):
        return obj.modified_on