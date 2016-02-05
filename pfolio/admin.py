from django.contrib import admin
from pfolio import models as mymodels
from sg_portfolio.settings import STATIC_URL

class blogPostAdmin(admin.ModelAdmin):
    date_hierarchy = 'created_on'
    list_display = ('title', 'created_on', 'excerpt')

    class Media:
        js = [
            '%stinymce/tinymce.min.js' % STATIC_URL,
            '%sjs/admin.js' % STATIC_URL,
        ]


class portfolioPostAdmin(admin.ModelAdmin):
    date_hierarchy = 'created_on'
    list_display = ('title', 'created_on','excerpt')

    class Media:
        js = [
           '%stinymce/tinymce.min.js' % STATIC_URL,
            '%sjs/admin.js' % STATIC_URL,
        ]

admin.site.register(mymodels.blogPost, blogPostAdmin)
admin.site.register(mymodels.portfolioPost, portfolioPostAdmin)

