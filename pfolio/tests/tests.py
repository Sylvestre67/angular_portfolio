from django.test import TestCase
from django.core import mail
from django.core.urlresolvers import reverse
from pfolio import models
import pdb

class ViewTest(TestCase):

    def test_home_page_views(self):
        response = self.client.get(reverse('home'))
        self.assertContains(response,'Sylvestre\'s coding adventures')

class APITest(TestCase):

    def test_serve_all_blog_posts(self):
        models.blogPost.objects.create(title = 'Blog_1',content='Lorem ipsum dolor sit amet, consectetur adipiscing elit. '
                                                         'Pellentesque sed blandit quam. Vestibulum sit amet sapien id enim varius '
                                                         'venenatis sed et turpis. Suspendisse at nisi id felis tristique vestibulum vitae '
                                                         'quis velit. Morbi efficitur viverra ipsum, sit amet ornare urna accumsan eu. '
                                                         'Class aptent taciti sociosqu ad litora torquent per conubia nostra, per inceptos '
                                                         'himenaeos. Vestibulum vitae sapien non velit interdum lacinia. Aenean quis '
                                                         'fermentum ex. Lorem ipsum dolor sit amet, consectetur adipiscing elit. '
                                                         'Duis imperdiet nibh in finibus sagittis_1.')
        models.blogPost.objects.create(title = 'Blog_2',content='Lorem ipsum dolor sit amet, consectetur adipiscing elit. '
                                                         'Pellentesque sed blandit quam. Vestibulum sit amet sapien id enim varius '
                                                         'venenatis sed et turpis. Suspendisse at nisi id felis tristique vestibulum vitae '
                                                         'quis velit. Morbi efficitur viverra ipsum, sit amet ornare urna accumsan eu. '
                                                         'Class aptent taciti sociosqu ad litora torquent per conubia nostra, per inceptos '
                                                         'himenaeos. Vestibulum vitae sapien non velit interdum lacinia. Aenean quis '
                                                         'fermentum ex. Lorem ipsum dolor sit amet, consectetur adipiscing elit. '
                                                         'Duis imperdiet nibh in finibus sagittis_2.')

        response = self.client.get(reverse('APIblogPosts'))

        self.assertEqual(models.blogPost.objects.count(),2)

        self.assertContains(response,'Blog_1')
        self.assertContains(response,'finibus sagittis_1')
        self.assertContains(response,'Blog_2')
        self.assertContains(response,'finibus sagittis_2')

    def test_serve_all_portfolio_posts(self):
        models.portfolioPost.objects.create(title = 'Portfolio_1',content='Lorem ipsum dolor sit amet, consectetur adipiscing elit. '
                                                         'Pellentesque sed blandit quam. Vestibulum sit amet sapien id enim varius '
                                                         'venenatis sed et turpis. Suspendisse at nisi id felis tristique vestibulum vitae '
                                                         'quis velit. Morbi efficitur viverra ipsum, sit amet ornare urna accumsan eu. '
                                                         'Class aptent taciti sociosqu ad litora torquent per conubia nostra, per inceptos '
                                                         'himenaeos. Vestibulum vitae sapien non velit interdum lacinia. Aenean quis '
                                                         'fermentum ex. Lorem ipsum dolor sit amet, consectetur adipiscing elit. '
                                                         'Duis imperdiet nibh in Portfolio sagittis_1.')
        models.portfolioPost.objects.create(title = 'Portfolio_2',content='Lorem ipsum dolor sit amet, consectetur adipiscing elit. '
                                                         'Pellentesque sed blandit quam. Vestibulum sit amet sapien id enim varius '
                                                         'venenatis sed et turpis. Suspendisse at nisi id felis tristique vestibulum vitae '
                                                         'quis velit. Morbi efficitur viverra ipsum, sit amet ornare urna accumsan eu. '
                                                         'Class aptent taciti sociosqu ad litora torquent per conubia nostra, per inceptos '
                                                         'himenaeos. Vestibulum vitae sapien non velit interdum lacinia. Aenean quis '
                                                         'fermentum ex. Lorem ipsum dolor sit amet, consectetur adipiscing elit. '
                                                         'Duis imperdiet nibh in Portfolio sagittis_2.')
        models.portfolioPost.objects.create(title = 'Portfolio_3',content='Lorem ipsum dolor sit amet, consectetur adipiscing elit. '
                                                         'Pellentesque sed blandit quam. Vestibulum sit amet sapien id enim varius '
                                                         'venenatis sed et turpis. Suspendisse at nisi id felis tristique vestibulum vitae '
                                                         'quis velit. Morbi efficitur viverra ipsum, sit amet ornare urna accumsan eu. '
                                                         'Class aptent taciti sociosqu ad litora torquent per conubia nostra, per inceptos '
                                                         'himenaeos. Vestibulum vitae sapien non velit interdum lacinia. Aenean quis '
                                                         'fermentum ex. Lorem ipsum dolor sit amet, consectetur adipiscing elit. '
                                                         'Duis imperdiet nibh in Portfolio sagittis_3.')

        response = self.client.get(reverse('APIPortfolioPosts'))

        self.assertEqual(models.portfolioPost.objects.count(),3)

        self.assertContains(response,'Portfolio_1')
        self.assertContains(response,'Portfolio sagittis_1')
        self.assertContains(response,'Portfolio_2')
        self.assertContains(response,'Portfolio sagittis_2')
        self.assertContains(response,'Portfolio_3')
        self.assertContains(response,'Portfolio sagittis_3')

    def test_serve_unique_blog_post(self):
        models.blogPost.objects.create(title = 'Blog_xx',content='Lorem ipsum dolor sit amet, consectetur adipiscing elit. '
                                                         'Pellentesque sed blandit quam. Vestibulum sit amet sapien id enim varius '
                                                         'venenatis sed et turpis. Suspendisse at nisi id felis tristique vestibulum vitae '
                                                         'quis velit. Morbi efficitur viverra ipsum, sit amet ornare urna accumsan eu. '
                                                         'Class aptent taciti sociosqu ad litora torquent per conubia nostra, per inceptos '
                                                         'himenaeos. Vestibulum vitae sapien non velit interdum lacinia. Aenean quis '
                                                         'fermentum ex. Lorem ipsum dolor sit amet, consectetur adipiscing elit. '
                                                         'Duis imperdiet nibh in Portfolio sagittis_xx.')

        blog_post = models.blogPost.objects.get(title = 'Blog_xx')

        response = self.client.get(reverse('APIBlogPostUnique', kwargs={'blog_post_pk': blog_post.pk}))

        self.assertContains(response,blog_post.content)
        self.assertContains(response,blog_post.title)

    def test_serve_unique_portfolio_post(self):
        models.portfolioPost.objects.create(title = 'Portfolio_xx',content='Lorem ipsum dolor sit amet, consectetur adipiscing elit. '
                                                         'Pellentesque sed blandit quam. Vestibulum sit amet sapien id enim varius '
                                                         'venenatis sed et turpis. Suspendisse at nisi id felis tristique vestibulum vitae '
                                                         'quis velit. Morbi efficitur viverra ipsum, sit amet ornare urna accumsan eu. '
                                                         'Class aptent taciti sociosqu ad litora torquent per conubia nostra, per inceptos '
                                                         'himenaeos. Vestibulum vitae sapien non velit interdum lacinia. Aenean quis '
                                                         'fermentum ex. Lorem ipsum dolor sit amet, consectetur adipiscing elit. '
                                                         'Duis imperdiet nibh in Portfolio sagittis_xx.')

        pfolio_post = models.portfolioPost.objects.get(title = 'Portfolio_xx')

        response = self.client.get(reverse('APIPfolioPostUnique', kwargs={'pfolio_post_pk': pfolio_post.pk}))

        self.assertContains(response,pfolio_post.content)
        self.assertContains(response,pfolio_post.title)

    def test_process_contact_us_form(self):
        form_dict = {'subject': '1231212332222222222222222', 'from':'123@mail.com','message':'123',
                'copy_me':'true','csrfmiddlewaretoken':'95emZLtlW6CsOkbSX8kCDXG8B1ey0DrO'}

        response = self.client.post(reverse('APIContactUsForm'),form_dict)

        #Test that request is successfull
        self.assertEqual(response.status_code,200)

        # Test that one message has been sent.
        self.assertEqual(len(mail.outbox), 2)

        # Verify that the subject of the first message is correct.
        self.assertEqual(mail.outbox[0].subject, '1231212332222222222222222')
