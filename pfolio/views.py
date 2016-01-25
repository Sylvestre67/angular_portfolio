from django.shortcuts import render,render_to_response,RequestContext
from django.http import HttpResponse,JsonResponse
from django.views.generic import TemplateView,View
from django.core import serializers
from django.core.mail import send_mail,EmailMultiAlternatives
from django.template.loader import render_to_string
from django.utils.html import strip_tags

from pfolio import models

# Create your views here.
class HomePageView(TemplateView):
    template_name = 'home.html'

class APIPortfolioPosts(View):

    def get(self, request, *args, **kwargs):
        portfolioPosts = serializers.serialize('json',models.portfolioPost.objects.all())
        return JsonResponse(portfolioPosts, safe=False)

class APIblogPosts(View):

    def get(self, request, *args, **kwargs):
        blogPosts = serializers.serialize('json', models.blogPost.objects.all())
        return JsonResponse(blogPosts, safe=False)

class APIBlogPostUnique(View):

    def get(self,request,*args, **kwargs):
        blog_post_pk = kwargs['blog_post_pk']
        blogPost = serializers.serialize('json',models.blogPost.objects.filter(pk=blog_post_pk))
        return JsonResponse(blogPost, safe=False)

class APIPfolioPostUnique(View):

    def get(self,request,*args, **kwargs):
        pfolio_post_pk = kwargs['pfolio_post_pk']
        pfolioPost = serializers.serialize('json',models.portfolioPost.objects.filter(pk=pfolio_post_pk))
        return JsonResponse(pfolioPost, safe=False)

class APIContactUsForm(View):

    def post(self,request,*args, **kwargs):

        subject = request.POST['subject']
        from_email = 'website@sylwebd.com'
        email_to = ['sylvestre@sylwebd.com']

        email_context = {
            'message' : request.POST['message'],
            'subject' : request.POST['subject'],
            'from' : request.POST['from']
        }

        html_content = render_to_string('emails/contact_us_email.html', email_context)
        text_content = strip_tags(html_content)

        msg = EmailMultiAlternatives(subject, text_content, from_email, email_to)
        msg.attach_alternative(html_content, "text/html")
        msg.send()

        if request.POST['copy_me']:
            msg = EmailMultiAlternatives(subject, text_content, from_email, [request.POST['from']])
            msg.attach_alternative(html_content, "text/html")
            msg.send()

        return JsonResponse({'message':'Thank you for your message. I\'ll be in touch soon.'})
