from django.shortcuts import render, redirect
from django.contrib import messages
from twilio.rest import Client
from .forms import LoginForm,Adminlogin
from .models import admin2
import random

# 'ACd0f1a220b1e06eb087310439f2c0cd66'
TWILIO_ACCOUNT_SID = 'ACbe29c08c22bcde0bb83d9132389edf27'
# '97549da49e73a886fba0b4734f1c68be'
TWILIO_AUTH_TOKEN = '5cc2fa9ffdd99d9c015c2e79f952064f'
# '+18587790145'
TWILIO_PHONE_NUMBER = '+14199494749'

# For Twilio Configuration
client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)


# For Login
def login(request):
    form_type = request.POST.get('form_type')
    if request.method == 'POST':
        if form_type == 'form2':
            form = LoginForm(request.POST)
            if form.is_valid():
                mobile_number = form.cleaned_data['mobile_number']
                request.session['mobile_number'] = mobile_number     # Store mobile number in session
                otp = send_otp(mobile_number)
                request.session['otp'] = otp  # Store OTP in session
                return redirect('verify_otp')
        else:
            form = Adminlogin(request.POST)
            if form.is_valid():
                username = form.cleaned_data['username']
                password = form.cleaned_data['password']
                request.session['username'] = username
                request.session['password'] = password
                return redirect('verify_admin')
    else:
        if form_type == 'form2':
            form = LoginForm()
        else:
            form = Adminlogin()
    return render(request, 'login.html', {'form': form})


# For send OTP
def send_otp(mobile_number):
    otp = str(random.randint(100000, 999999))
    message = client.messages.create(
        body=f'Dear User, Please use the following One Time Password (OTP): {otp}. Do not share this OTP with anyone',
        from_=TWILIO_PHONE_NUMBER,
        to=mobile_number
    )
    return otp

# For verify it
def verify_otp(request):
    if request.method == 'POST':
        otp_entered = request.POST.get('otp', '')
        otp_sent = request.session.get('otp', '')
        if otp_entered == otp_sent:
            return render(request,'interface.html')
        else:
            messages.error(request, "Invalid OTP. Please try again.")
    mobile_number = request.session.get('mobile_number', '')
    return render(request, 'login.html',{'mobile_number': mobile_number})


# For verify admin
def verify_admin(request):
    all_rows = admin2.objects.all()
    uname = request.POST.get('username','')
    psw = request.POST.get('password','')

    for row in all_rows:
        if row.username == uname and row.password == psw :
            return render(request,'admin.html')
        else:
            messages.error(request,"Invalid Username Or Password. Please try again.")

    un = request.session.get('username','')
    ps = request.session.get('password', '')
    return render(request, 'login.html',{'username': un,'password': ps})


# For logout activities
def logout_view(request):
    # log out actions
    return redirect('login')