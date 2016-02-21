__author__ = 'Sylvestre'
from django.conf.urls import url
from pfolio import views

urlpatterns = [

    url(r'^$',views.HomePageView.as_view(),name='home'),

    ###### API URL ######
    url(r'^api/portfolioPosts/$',views.APIPortfolioPosts.as_view(),name='APIPortfolioPosts'),
    url(r'^api/blogPosts/$',views.APIblogPosts.as_view(),name='APIblogPosts'),
    url(r'^api/blogPosts/(?P<blog_post_slug>[\w-]+)/$',views.APIBlogPostUnique.as_view(),name='APIBlogPostUnique'),
    url(r'^api/pfolioPosts/(?P<pfolio_post_slug>[\w-]+)/$',views.APIPfolioPostUnique.as_view(),name='APIPfolioPostUnique'),
    url(r'^api/contactUsForm/$',views.APIContactUsForm.as_view(),name='APIContactUsForm'),

]

