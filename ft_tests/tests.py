__author__ = 'sylvestre'
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium import webdriver
from pfolio import models
import unittest
import re

def createModels(Model,numberOfModels):

    for i in range(0,numberOfModels,1):
        modelTitle = ('Blog_%s')%(i)
        modelContent = ('Lorem ipsum dolor sit amet, consectetur adipiscing elit. '
                       'Pellentesque sed blandit quam. Vestibulum sit amet sapien id enim varius '
                       'venenatis sed et turpis. Suspendisse at nisi id felis tristique vestibulum vitae '
                       'quis velit. Morbi efficitur viverra ipsum, sit amet ornare urna accumsan eu. '
                       'Class aptent taciti sociosqu ad litora torquent per conubia nostra, per inceptos '
                       'himenaeos. Vestibulum vitae sapien non velit interdum lacinia. Aenean quis '
                       'fermentum ex. Lorem ipsum dolor sit amet, consectetur adipiscing elit. '
                       'Duis imperdiet nibh in finibus sagittis_%s.')%(i)
        Model.objects.create(title = modelTitle,content=modelContent)

class NewVisitorTest(StaticLiveServerTestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()
        createModels(models.blogPost,5)
        createModels(models.portfolioPost,5)

    def tearDown(self):
        self.browser.quit()

    def test_can_access_the_homepage(self):

        driver = self.browser

        #Jimi wants to know a little bit more about my work. He heard about my blog and check it out.
        driver.get(self.live_server_url)

        #Jimi noticed the title of the page is "Sylvestre's coding adventures"
        self.assertIn('Sylvestre\'s coding adventures',self.browser.title)

        #He finds on the Left a navigation menu
        driver.find_element_by_id('side-navigation')

        #The home tab is active
        driver.find_element_by_css_selector('.side-nav > li:first-child.active')

        #On the right page of the home page, he noticed the about-me section
        driver.find_element_by_id('about-me')

        #He clicks on the blog section navigation
        blog_menu_link = driver.find_element_by_link_text("Blog")
        blog_menu_link.click()

        #The Blog tab is now active
        driver.find_element_by_css_selector('.side-nav > li:nth-child(2).active')

        #He sees the Blog-post-list section
        driver.find_element_by_id('my-blog')

        #with 5 blog posts
        count_of_blogPosts = self.browser.find_elements_by_css_selector('.blog-post-list > li')
        self.assertEqual(len(count_of_blogPosts),5)

        #Jimi then clicks on the title of the first blogPost
        blog_post = driver.find_element_by_css_selector('.blog-post-list > li > a')
        blog_post.click()

        #Jimi can now read the full blogPost
        driver.find_element_by_css_selector('.blog-content')
        driver.find_element_by_css_selector('.blog-content > h1')
        driver.find_element_by_css_selector('.blog-content > p')

        #He then clicks on the Portfolio section
        pfolio_menu_link = driver.find_element_by_link_text("Portfolio")
        pfolio_menu_link.click()

        #The blog tab is active
        driver.find_element_by_css_selector('.side-nav > li:nth-child(3).active')

        #He sees the Portfolio list section
        driver.find_element_by_id('my-portfolio')

        #He founds 5 portfolio posts
        count_of_portfolioPosts = self.browser.find_elements_by_css_selector('.portfolio-list > div')
        self.assertEqual(len(count_of_portfolioPosts),5)

        #Jimi then clicks on the title of the first portfolioPost
        pfolio_post = driver.find_element_by_css_selector('.portfolio-list > div > a')
        pfolio_post.click()

        #Jimi can now read the full portfolioPost
        driver.find_element_by_class_name('portfolio-content')

        page_content = driver.page_source
        text_found = re.search(r'Lorem ipsum dolor sit amet, consectetur adipiscing elit', page_content)
        self.assertNotEqual(text_found, None)

        #He then clicks on the Contact section
        contact_menu_link = driver.find_element_by_link_text("Contact")
        contact_menu_link.click()

        #The blog tab is active
        driver.find_element_by_css_selector('.side-nav > li:last-child.active')

        #He founds a contact form
        contact_form = driver.find_element_by_id('contact-form')

        #But does not see the Thank-you message
        driver.find_element_by_css_selector('#thank-you-submit.ng-hide')

        #He submits the form with a thoughtfull message
        from_field = driver.find_element_by_name('from')
        from_field.send_keys('sgug@outlook.com')

        subject_field = driver.find_element_by_name('subject')
        subject_field.send_keys('TESTING --- TESTING')

        message_field = driver.find_element_by_name('message')
        message_field.send_keys('Lorem ipsum dolor sit amet, consectetur adipiscing elit.'
                       'Pellentesque sed blandit quam. Vestibulum sit amet sapien id enim varius '
                       'venenatis sed et turpis. Suspendisse at nisi id felis tristique vestibulum vitae '
                       'quis velit. Morbi efficitur viverra ipsum, sit amet ornare urna accumsan eu. '
                       'Class aptent taciti sociosqu ad litora torquent per conubia nostra, per inceptos '
                       'himenaeos. Vestibulum vitae sapien non velit interdum lacinia. Aenean quis '
                       'fermentum ex. Lorem ipsum dolor sit amet, consectetur adipiscing elit. '
                       'Duis imperdiet nibh in finibus sagittis.')

        copy_me = driver.find_element_by_name('copy_me')
        copy_me.click()

        submit_button = driver.find_element_by_name('submit')
        submit_button.click()

        #He noticed an AJAX loader spinning in place of the form
        driver.find_element_by_css_selector('#ajax-loader')

        #He sees the thank-you message.
        driver.find_element_by_css_selector('#thank-you-submit')

        #Jimi goes back to the homepage
        driver.get(self.live_server_url)

        self.fail('************************ SUCESSS ******************************')
