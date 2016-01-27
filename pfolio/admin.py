from django.contrib import admin
from pfolio import models as mymodels

class blogPostAdmin(admin.ModelAdmin):
    date_hierarchy = 'created_on'
    list_display = ('title', 'created_on', 'excerpt')

    class Media:
        js = [
            '/static/grappelli/tinymce/jscripts/tiny_mce/tiny_mce.js',
            '/static/js/admin.js',
        ]


class portfolioPostAdmin(admin.ModelAdmin):
    date_hierarchy = 'created_on'
    list_display = ('title', 'created_on','excerpt')

    class Media:
        js = [
            '/static/grappelli/tinymce/jscripts/tiny_mce/tiny_mce.js',
            '/static/js/admin.js',
        ]

admin.site.register(mymodels.blogPost, blogPostAdmin)
admin.site.register(mymodels.portfolioPost, portfolioPostAdmin)
