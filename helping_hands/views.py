import pyrebase

from django.shortcuts import render, redirect
from django.contrib import auth
from pyrebase import pyrebase
from collections import OrderedDict
from django.contrib.auth.decorators import login_required
from django.template.defaulttags import register


from .forms import ContactForm
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse


firebase_api = open('firebase_api.txt')


config = {
	'apiKey': "AIzaSyCUztdaEWSS7v4yM4SUKDFGSV3uF45qGGU",
  'authDomain': "helpinghands-5794f.firebaseapp.com",
  'databaseURL': "https://helpinghands-5794f.firebaseio.com",
  'projectId': "helpinghands-5794f",
  'storageBucket': "helpinghands-5794f.appspot.com",
  'messagingSenderId': "146248547154",
  'appId': "1:146248547154:web:f6c63cb1fb469708ce988b",
  'measurementId': "G-51YN95B6QV"
}

firebase = pyrebase.initialize_app(config)
fireauth = firebase.auth()
database = firebase.database()
storage = firebase.storage()


def home(request):
	return render(request, 'home.html')

def login(request):
	return render(request, 'login.html')


def dashboard(request):
  if request.method == 'POST': 
    try:
      email = request.POST['email']
      password = request.POST['password']

      user = fireauth.sign_in_with_email_and_password(email, password)
    except Exception as e:
      message = "Invalid Credentials"
      print(e)
      return render(request, 'login.html', {'msg': message})

    print("Login Successful!", user['idToken'][:10])
    session_id = user['idToken']
    request.session['uid'] = str(session_id)
    return render(request, 'dashboard.html')
  else:
    print(request.session.get('uid'))
    return render(request, 'login.html')


def logout(request):
	auth.logout(request)
	return render(request, 'login.html')

global uid
def signup(request):
  if request.method == 'POST':
    try:
      name = request.POST['name']
      phone = request.POST['phone']
      username = request.POST['username']
      email = request.POST['email']
      password = request.POST['password']
      address1 = request.POST['address1']
      city = request.POST['city']
      state = request.POST['state']
      zip_code = request.POST['zip_code']
      user = fireauth.create_user_with_email_and_password(email, password)
      # empty fridge initially
      uid = user['localId']
      data = {
        'uid': uid,
        'name': name, 
        'username': username,
        'address1':address1,
        'city':city,
				'state':state,
        'zip_code':zip_code,
        'phone': phone, 
      }
      
      database.child("users").child(uid).set(data)
      return redirect('login')
    except Exception as e:
      message = "Unable to create account. Please Try again"
      print(e, message)
      return render(request, 'signup.html', {'msg': message})
  else:
    return render(request, 'signup.html')

def publishJob(request): 
  if request.method == 'POST':
    jname = request.POST['jobName']
    jauthor = request.POST['employer']
    jdesc = request.POST['description']
    phone = request.POST['phone']
    hrate = request.POST['hourly_rate']


    data = {
      'jobName': jname, 
      'employer': jauthor,
      'phone': phone,
      'description': jdesc,
      'hourly_rate': hrate,
    }

    print(data)
    database.child("jobsCreated").child(jname).set(data)
    return render(request, 'dashboard.html')


...
@register.filter
def get_item(dictionary, key):
    return dictionary.get(key)

def jobList(request):
	dic = OrderedDict()
	all_recipes = database.child('jobsCreated').get()
	uid = request.session.get('uid')
	
	for recipe in all_recipes.each():
		dic[recipe.key()] = recipe.val()
	return render(request, 'jobList.html', {"dic":dic})


#@login_required
def profile(request, name):
	'''
	data = {}
	try:
		#uid = request.session.get('localId')
		print(uid)
		userinfo = database.child('users').child(uid).get()
		
		for info in userinfo.each():
			data[info.key()] = info.val()

	except Exception as e:
		print(e)
		# print("hello")

		pass
	return render(request, 'profile.html', {"data":data})
	'''
	profile = database.child('users').child(name).get().val()
	return render(request, 'profile.html', {'profile': profile})

def job(request, name):
  job = database.child('jobsCreated').child(name).get().val()
  return render(request, 'job.html', {'job': job})

def contact_form(request):
    form = ContactForm()
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = f'Message from {form.cleaned_data["name"]}'
            message = form.cleaned_data["message"]
            sender = form.cleaned_data["email"]
            recipients = ['tsaicharan03@gmail.com']
            try:
                send_mail(subject, message, sender, recipients, fail_silently=True)
            except BadHeaderError:
                return HttpResponse('Invalid header found')
            return HttpResponse('Success...Your email has been sent')
    return render(request, 'contact.html', {'form': form})