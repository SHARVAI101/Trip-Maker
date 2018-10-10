from django.shortcuts import render
from django.http import HttpResponse, Http404
import os

from django.core.mail import send_mail
# import smtplib

from .models import Place,upload_image_path,get_filename_ext

import nltk
from nltk.tokenize import sent_tokenize, word_tokenize
import string

# Create your views here.
def trip_manager(request):
	# qs=Place.objects.all()
	qs=Place.objects.filter(userinfo=request.user)
	print(qs)

	context={
		"all_trips":qs
	}
	return render(request, "trips/trip_manager.html", context)
	# return HttpResponse("Hi")


def trip_detail(request, pk=None, *args, **kwargs):
	instance=Place.objects.get(pk=pk)
	if instance is None:
		raise Http404("Product not found")
	else:
		print("hi")

		# sendmail()
		send_email()

		context={
			'object':instance
		}
		return render(request, "trips/trip_detail.html", context)

#image uploading system
def handle_uploaded_file(file, filename, foldername):
    
    print("--here--")
    print(filename)

    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    MEDIA_ROOT = os.path.join(os.path.dirname(BASE_DIR), "static_cdn", "media_root")

    foldername= MEDIA_ROOT+'/trips/'+foldername
    if not os.path.exists(foldername):
    	print("not exists")
    	os.mkdir(foldername)

    with open(MEDIA_ROOT+'/'+filename, 'wb+') as destination:
        for chunk in file.chunks():
            destination.write(chunk)

def add_trip(request, *args, **kwargs):
	
	if request.method == "POST":
		print(request.POST)
		cityname=request.POST.get('cityname')
		countryname=request.POST.get('countryname')
		user=request.user

		# print(str(request.FILES['image']))

		image=upload_image_path(request,str(request.FILES['image']))

		print(image)

		folder_name, ext=get_filename_ext(image)

		print(folder_name)

		handle_uploaded_file(request.FILES['image'], image, folder_name)

		# image=upload_image_path(request,request.POST.get('image'))

		p=Place()
		p.cityname=cityname
		p.countryname=countryname
		p.userinfo=user
		p.image=image
		p.save()
		# p=Place(cityname=cityname,countryname=countryname,userinfo=user,image=image)
		# p.save()

	return render(request, "trips/add_trip.html")
	# return HttpResponse("Hi")

def send_email():

	send_mail(
	    'Django Email',
	    'Hi this is a django email',
	    'sharvai101@gmail.com',
	    ['anjali.chaudhari@somaiya.edu'],
	    fail_silently=False,
	)

# e-mail
# def sendmail():
#     content="mail test"
#     mail=smtplib.SMTP("smtp.gmail.com",587)
#     mail.ehlo()
#     mail.starttls()
#     mail.login("sharvai101@gmail.com","frederickthegreat101")
#     mail.sendmail("sharvai101@gmail.com","mihirshah050505@gmail.com",content)
#     mail.close()

# def nltk_calc():
	

def nltk(request):

	# EXAMPLE_TEXT = "Hello Mr. Smith, how are you doing today? The weather is great, and Python is awesome. The sky is pinkish-blue. You shouldn't eat cardboard."

	# text="Decide, the frontend team needs to make the website mobile reponsive decision end"

	BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
	MEDIA_ROOT = os.path.join(os.path.dirname(BASE_DIR), "static_cdn", "media_root")

	with open(MEDIA_ROOT+'/transcripts/transcript.txt', 'r') as myfile:
		text=myfile.read().replace('\n','')	

	# print(text)

	datas=word_tokenize(text)
	# print(datas)
	# print(datas[0])

	#print ([i for i, item in enumerate(datas) if item == 'Decide'])

	decision_string = str('')
	flag=False # to see if 'Decide' word was said

	for i in range(len(datas)):
		# print(datas[i]+","+str(flag))
		if datas[i].lower() == 'decide':
			flag=True	

		if flag==True and datas[i].lower() == 'decision' and datas[i+1].lower() == "end":
			# print("hie")
			flag=False
			decision_string=decision_string.strip(' ')

			print(decision_string)

			decision_string=str('')

		if flag==True :
			# i=i+1
			if datas[i] not in string.punctuation:
				decision_string = decision_string + ' ' + datas[i]
			else:
				decision_string = decision_string + datas[i]

		# table=str.maketrans("", "", decision_string.punctuation)
		# decision_string = decision_string.translate(table)

		

	context={
		'datas':datas
	}
	return render(request, "trips/nltk.html", context)
