from django.test import TestCase
import unittest
from blog.models import Author, Blog


# Create your tests here.

class AuthorModelTest(TestCase):

    """
    Test verifies whether a string representation is returned when calling
    model methods for Author and Blog.
    """
    @classmethod
    def setUpTestData(cls):
    # Set up data for the whole TestCase
        cls.author = Author.objects.create(first_name='Bob', last_name='Builder', biography='Can he fix it')


    #Check if first name saves properly
    def test_author_first_name(self):
        first_name =self.author.first_name # get the author's first name
        self.assertEquals(first_name, 'Bob')

    #Check if last name saves properly
    def test_author_last_name(self):
    	last_name = self.author.last_name
    	self.assertEquals(last_name, 'Builder')
    
    #Check if biography saves properly
    def test_author_biography_value(self):
    	biography = self.author.biography
    	self.assertEquals(biography, 'Can he fix it')

    #Check if max_values for biography are enforced 
    def test_author_first_name_max_value_enforced(self):
    	first_name = self.author._meta.get_field('first_name').max_length # gets max length field option
    	self.assertEquals(first_name, 20)

    def test_author_last_name_max_value_enforced(self):
    	last_name = self.author._meta.get_field('last_name').max_length
    	self.assertEquals(last_name, 20)

    def test_author_last_name_max_value_enforced(self):
        biography = self.author._meta.get_field('biography').max_length
        self.assertEquals(biography, 500)

    def test_author_string_method_equal_to_first_name_last_name(self):
        # author_name = ''"%s, %s"% (self.author.first_name, self.author.last_name)''
        # NOTE THIS CAREFULLY:
        # when you call the actual 'model object' the __str__ that is set in the models.py 
        # page determines what the string representation of the WHOLE object is called
        self.assertEquals(str(self.author), 'Bob, Builder')


class BlogModelTest(TestCase):

    """
    This method tests the blog model
    """

    @classmethod
    def setUpTestData(cls):
    # Set up data for the whole TestCase

        #first author
        #cls.author = Author.objects.create(first_name='Eric', last_name='Cartmen', biography='suck my balls kyle')


        #second blog
        cls.blog = Blog.objects.create(title='Prepare for tech wars in March', 
	        author=Author.objects.create(first_name='Eric', last_name='Cartmen', 
	        biography='suck my balls kyle') , 
	        content='Holy shit this is the best new product!')

    def test_author_related_to_blog(self):
        self.assertEquals(str(self.blog.author), 'Eric, Cartmen')


    def test_blog_string_method_equal_to_title(self):
        print('title method executing...')
        self.assertEquals(str(self.blog), 'Prepare for tech wars in March')

    #Test that the correct url is reversed and returned
    def test_blog_get_absolute_url_returns_the_correct_url_path(self):
        self.assertEquals(str(self.blog.get_absolute_url()), '/blog/blogdetail/1')