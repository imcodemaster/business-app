from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse 
from django.utils import timezone
from django.db.models import Avg, Count, Min, Sum
# Create your models here.



items = [
                ('Build Business Presence', "Build Business Presence"),
                ('StartPlus+', "StartPlus+"),
				('E-Books', "E-Books"),
                ('Digital-X for Business', "Digital-X for Business"),
                ('Be Digital for School', "Be Digital for School"),
                ('Learnincreation Business Profile', "Learnincreation Business Profile"),
                ('Digital Marketing ', "Digital Marketing"),
				('Marketing	Content	Design', "Marketing	Content	Design"),
                ('Social Media Marketing', "Social Media Marketing"),
				('Create Learnincreation Shop', "Create Learnincreation Shop"), 
        ]

class Ticket(models.Model):
	subject = models.CharField(max_length = 100, null= True , blank = True)
	message = models.TextField(null= True , blank = True)
	published = models.DateTimeField(auto_now_add = True)
	author = models.ForeignKey(User, on_delete=models.CASCADE)
	
	class Meta:
		ordering = ['-published']
		
	def __str__(self):
		return self.subject

#post from neer to user feed
class Post(models.Model):
	subject = models.CharField(max_length = 500)
	about = models.CharField(max_length = 250, null= True , blank = True) #remove null when go to deploy	
	published = models.DateTimeField(default = timezone.now)
	image = models.FileField(upload_to ='media' , null= True , blank = True)	
	content = models.TextField( null= True , blank = True)
	content_addition = models.TextField( null= True , blank = True)
	highlight = models.CharField( max_length = 500, null= True , blank = True)
	#favourites = models.ManyToManyField(User, related_name='favourite', default=None, blank=True)
	likes = models.ManyToManyField(User, related_name='like', default=None, blank=True)
	#like_count = models.BigIntegerField(default='0')		

	def total_likes(self):
		return self.likes.count()



	def __str__(self):
		return self.subject


	@property
	def mediaURL(self):
		try : 
			url = self.image.url
		except : 
			url = ''
		return url 



class PostComment(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	post = models.ForeignKey(Post, related_name='postcomment' ,  on_delete=models.CASCADE)
	comment_content = models.TextField( null= True , blank = True)
	published = models.DateTimeField(default = timezone.now)




	def __str__(self):
		return self.user.username 

class order_list(models.Model):
	user 		= models.ForeignKey(User, on_delete= models.CASCADE)
	date 		= models.DateTimeField()
	item = models.CharField( max_length = 50 , choices=items , null=True , blank=True)
	company = models.CharField( max_length = 100 , null=True , blank=True)
	status = models.TextField( null= True , blank = True)
	description = models.TextField( null= True , blank = True)
	payment = models.TextField( null= True , blank = True)
	wallet = models.TextField( null= True , blank = True)
	
	

	def __str__(self):
		return self.user.username  


class myorder(models.Model):
	item = models.CharField( max_length = 50 , choices=items , null=True , blank=True)
	mobile = models.CharField(max_length = 10)
	message = models.TextField()
	company = models.CharField(max_length = 100 , null=True , blank = True)
	first_name = models.CharField(max_length = 100 , null=True , blank = True)
	second_name = models.CharField(max_length = 100 , null=True , blank = True)
	date = models.DateTimeField( help_text = "Enter Date month/date/year")

	def __str__(self):
		return self.first_name 
