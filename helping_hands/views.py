import pyrebase

from django.shortcuts import render, redirect
from django.contrib import auth
from pyrebase import pyrebase

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
      # country = request.POST['country']
      user = fireauth.create_user_with_email_and_password(email, password)
      uid = user['localId']
      # empty fridge initially
      data = {
        'uid': uid,
        'name': name, 
        'username': username,
        'address1':address1,
        'city':city,
				'state':state,
        'zip_code':zip_code,
        'phone': phone, 
        # 'country':country
      }
      
      database.child("users").child(uid).set(data)
      return redirect('login')
    except Exception as e:
      message = "Unable to create account. Please Try again"
      print(e, message)
      return render(request, 'signup.html', {'msg': message})
  else:
    return render(request, 'signup.html')

