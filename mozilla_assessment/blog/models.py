from django.db import models
from django.contrib.auth.models import User # access default user account
from datetime import datetime # remember to always import the inside of date time
from django.urls import reverse # Reverse from the data and get the URL
# Create your models here.

#Blog object for database
class Blog(models.Model):

    title = models.CharField(max_length=100) # CharField supports small to medium strings
    author = models.ForeignKey(Author, on_delete=models.CASCADE) # will auto delete related objects author is deleted
    post_date = models.DateTimeField(default=datetime.date.today(), editable=False)
    content = models.TextField(max_length=2000, help_text="What's on your mind?")

    def __str__(self):
    	return "%s" % (self.title)


    def get_absolute_url(self):
    	# must define a view called 'Blog-Detail'
    	return reverse('blogs.views.blog-detail' ,args=[str(self.id)])

class Author(models.Model):

	first_name = models.CharField(max_length=20)
	last_name = models.Charfield(max_length=20)
	biography = models.TextField(max_length=500, help_text="Once upon a time...")


    def __str__(self):
    	return "%s, %s" % (self.first_name, self.last_name)

class Comment(models.Model):

	user_that_posted = models.ForeignKey(User, on_delete=models.CASCADE)
	blog_containing_comment = models.ForeignKey(Blog, on_delete=models.CASCADE)
	comment = models.TextField(max_length=200, help_text='Comment..')
	post_date = models.DateTimeField(default=datetime.date.today(), editable=False)