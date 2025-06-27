from django.db import models
from django.contrib.auth.models import User
from django.contrib.admin.options import ModelAdmin

# Create your models here.


Blood_Group = [
			('A+', "A+"),
			('A-', "A-"),
			('B+', "B+"),
			('B-', "B-"),
			('AB+', "AB+"),
			('AB- ', "AB-"),
			('O+', "O+"),
			('O- ', "O-"),
	]

gender = [
				('Male', "Male"),
				('Female', "Female"),
				('Other', "Other")
		]



domicile = [
				
				('Andaman and Nicobar Islands', "Andaman and Nicobar Islands"),
                ('Andhra Pradesh', "Andhra Pradesh"),
                ('Arunachal Pradesh', "Arunanchal Pradesh"),
                ('Assam', "Assam "),
                ('Bihar', "Bihar"),
                ('Chhattisgarh', "Chhattisgarh"),
                ('Chandigarh', "Chandigarh"),
                ('Dadra and Nagar Haveli', "Dadra and Nagar Haveli"),
                ('Daman and Diu', "Daman and Diu"),
                ('Delhi', "Delhi"),
                ('Goa', "Goa"),
                ('Gujrat', "Gujrat"),
                ('Haryana', "Haryana"),
                ('Himanchal Pradesh', "Himanchal Pradesh"),
                ('Jammu & Kashmir', "Jammu & Kashmir"),
                ('Jharkhand', "Jharkhand"),
                ('Karnataka', "Karnataka"),
                ('Kerela', "Kerela"),
                ('Ladakh', "Ladakh"),
                ('Lakshadweep', "Lakshadweep"),
                ('Madhya Pradesh', "Madhya Pradesh "),
                ('Maharastra', "Maharastra "),
                ('Manipur', "Manipur"),
                ('Meghalaya', "Meghalaya"),
                ('Mizoram', "Mizoram"),
                ('Nagaland', "Nagaland"),
                ('Odisha', " Odisha"),
                ('Punjab', " Punjab"),
                ('Puducherry', "Puducherry"),
                ('Rajasthan', "Rajasthan"),
                ('Sikkim', "Sikkim"),
                ('Tamil Naidu', "Tamil Naidu"),
                ('Telangana', "Telangana"),
                ('Tripura', "Tripura"),
                ('Uttar Pradesh', "Uttar Pradesh"),
                ('Uttarakhand', "Uttarakhand"),
                ('West Bengal', "West Bengal"),

		]


class Profile(models.Model):
	user = models.OneToOneField(User , on_delete = models.CASCADE) #user
	image = models.ImageField(default = 'default.png' , upload_to = 'profiles_pics' , null=True , blank=True , help_text='Upload Your Picture') # student profile pic 
	signature_image = models.ImageField( upload_to = 'sign_pics', null=True , blank=True , help_text='Upload Your signature image') # student signature pic
	domicile = models.CharField(max_length = 30 , choices=domicile, null=True , blank=True , help_text='Choose Your Domicile')
	company_name = models.CharField(max_length = 100 , help_text='Enter Company/Shop/Business Name' , null = True , blank=True )
	gender = models.CharField(max_length = 10 , choices=gender, null=True , blank=True , help_text='Choose Your Gender')
	nationality = models.CharField(max_length = 50 , null=True , blank=True , help_text='Proud To Say Indian')
	mobile = models.CharField(max_length=10, null = True , blank = True , help_text='Enter Your Mobile number')
	house_no = models.CharField(max_length = 250, null = True , blank = True , help_text='Enter House / Flat Number / Colony / Ward No. ')
	address = models.CharField(max_length = 250, null = True , blank = True , help_text='Enter Your Address Details')
	city = models.CharField(max_length = 200, null = True , blank = True , help_text='Enter Your City')
	state = models.CharField(max_length = 200, null = True , blank = True , help_text='Enter Your State')
	postal_code = models.CharField(max_length = 6 , null = True , blank = True , help_text='Enter Your Postal Code ** PIN Code')
	blood_group = models.CharField(max_length = 5 , choices = Blood_Group , null = True , blank = True , help_text='Choose Your Blood Group')
	skill =  models.CharField(max_length = 250 , null = True , blank = True , help_text='About Your Skills - Things you do greatly')




	def __str__(self):
		return f'{self.user.username} Profile'
