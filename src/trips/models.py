import os
from django.contrib.auth import get_user_model
from django.db import models
import random

#gives filename's extension
def get_filename_ext(filepath):
	base_name = os.path.basename(filepath)
	name, ext= os.path.splitext(base_name)
	return name, ext

def upload_image_path(instance, filename):
	# print(instance)
	# print(filename)
	#generating a new file name to avoid any issues using a random number as the name of the file
	new_filename = random.randint(1,39102089312)
	name, ext=get_filename_ext(filename)
	final_filename='{new_filename}{ext}'.format(new_filename=new_filename, ext=ext)
	print(new_filename)
	print(final_filename)
	return "trips/{new_filename}/{final_filename}".format(
		new_filename=new_filename,
		final_filename=final_filename
		)

User=get_user_model()
class Place(models.Model):
	cityname	=	models.CharField(max_length=50)
	countryname	=	models.CharField(max_length=50)
	userinfo	=	models.ForeignKey(User, on_delete=models.CASCADE)
	image=models.ImageField(upload_to=upload_image_path, null=True, blank=True)

	def __str__(self):
		return '%s %s' % (self.cityname, self.userinfo.username)

