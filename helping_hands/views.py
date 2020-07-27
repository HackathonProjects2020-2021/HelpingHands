import pyrebase

from django.shortcuts import render, redirect
from django.contrib import auth
from pyrebase import pyrebase
from collections import OrderedDict
from django.contrib.auth.decorators import login_required
from django.template.defaulttags import register


from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse



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
  email = request.POST.get('email')
  passw = request.POST.get("password")

  try:
    user=fireauth.sign_in_with_email_and_password(email,passw)
    print("hello world")
    session_id = user['idToken']
    request.session['sid'] = str(session_id)
    uid = user['localId']
    request.session['uid'] = uid
    request.session.modified = True
  except Exception as e:
    print(e)
    message = "Invalid Credentials"
    return render(request,"login.html",{"msg":message})
  return render(request, "dashboard.html",{"e":email})



def logout(request):
	auth.logout(request)
	return render(request, 'login.html')

def signup(request):
  if request.method == 'POST':
    try:
      fullname = request.POST['fullname']
      email = request.POST['email']
      password = request.POST['password']
      city = request.POST['city']
      state = request.POST['state']

      user = fireauth.create_user_with_email_and_password(email, password)
      uid = user['localId']

      data = {
        'uid': uid,
        'fullname': fullname,
        'email':email,
        'state': state,
        'city': city,

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
    jemployeremail = request.POST['employeremail']
    jdesc = request.POST['description']
    phone = request.POST['phone']
    hrate = request.POST['hourly_rate']


    data = {
      'jobName': jname, 
      'employer': jauthor,
      'phone': phone,
      'description': jdesc,
      'hourly_rate': hrate,
      'employeruid': request.session.get('uid'),
      'employeremail':jemployeremail,
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
  marvel = OrderedDict()
  all_jobs = database.child('jobsCreated').get()
  uid = request.session.get('uid')
  
  for job in all_jobs.each():
    dic[job.key()] = job.val()

  return render(request, 'jobList.html', {"dic":dic})




def profileNew(request):
  if (request.session.get('sid')):
      #data = {}
      print(1)
      uid = request.session.get('uid')
      print(uid)
      print("\nUser", uid, "landed to their own profile.\n")
      profile =  database.child("users").child(uid).get().val()
      myjobs =  database.child("users").child(uid).child("applications").get().val()
      deletelist = {}
      if myjobs:
        for key in myjobs:
          deletelist[key] = "/delete/"+key.replace(" ", "%20")
      print(deletelist)
      return render(request, 'profileNew.html', {'profile': profile, 'myjobs': myjobs, 'deletelist': deletelist})
  else:
    return redirect('/login/')


def updateprofile(request):
  if request.method == 'POST':
    fullname = request.POST['fullname']
    email = request.POST['email']
    city = request.POST['city']
    state = request.POST['state']
    uid = request.session.get('uid')

    data = {
      'fullname': fullname, 
      'email': email,
      'city': city,
      'state': state,
      'uid': uid,
    }

    print(data)
    database.child("users").child(uid).set(data)
  return redirect('/profile/')


def publicprofile(request, name):
  profile = database.child('users').child(name).get().val()
  return render(request, 'publicprofile.html', {'profile': profile})


def job(request, name):
  job = database.child('jobsCreated').child(name).get().val()
  action = '/apply/'+job['jobName'].replace(" ", "%20")
  #if (request.session.get('sid')):
  return render(request, 'job.html', {'job': job, 'action':action})
  

def apply(request, name):
  try:
    uid = request.session.get('uid')
    receiver = database.child("jobsCreated").child(name).child('employeremail').get().val()
    applicant_email = database.child("users").child(uid).child("email").get().val()
    applicant = database.child("users").child(uid).child('fullname').get().val()
    sendemail(receiver, applicant, applicant_email)
    print(receiver, applicant, applicant_email)
    database.child("users").child(uid).child("applications").child(name).set(name)
  except Exception as e:
      print(f'\n\n\n{e}\n\n\n')
      return redirect("/login/")
  return redirect(f"/job/{name}")

def sendemail(receiver, applicant, applicant_email):
    import smtplib, ssl

    port = 465

    password = ",ReGsrPx)<+y$9u/"

    message = f"""\
    Subject: HelpingHands Application

    {applicant} applied for the job you posted!
    Confirm or reject the application by reaching out to {applicant_email}

    """
    
    context = ssl.create_default_context()

    with smtplib.SMTP_SSL("smtp.gmail.com", port, context = context) as server:
        server.login('helpinghands1729@gmail.com', password)
        
        server.sendmail("helpinghands1729@gmail.com",receiver,message)


def delete(request, name):
  try:
    uid = request.session.get('uid')
    database.child("users").child(uid).child("applications").child(name).remove()
  except:
    return redirect('/login/')
  return redirect("/profile")


def contact(request):
    return render(request, 'contact.html')


