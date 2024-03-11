from django.shortcuts import render, redirect
from django.contrib import messages
from twilio.rest import Client
from .forms import LoginForm
import random


TWILIO_ACCOUNT_SID = 'ACd0f1a220b1e06eb087310439f2c0cd66'
TWILIO_AUTH_TOKEN = '97549da49e73a886fba0b4734f1c68be'
TWILIO_PHONE_NUMBER = '+18587790145'


client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)

def login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            mobile_number = form.cleaned_data['mobile_number']
            request.session['mobile_number'] = mobile_number  # Store mobile number in session
            otp = send_otp(mobile_number)
            request.session['otp'] = otp  # Store OTP in session
            return redirect('verify_otp')
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})

def send_otp(mobile_number):
    otp = str(random.randint(100000, 999999))
    message = client.messages.create(
        body=f'Dear User, Please use the following One Time Password (OTP): {otp}. Do not share this OTP with anyone',
        from_=TWILIO_PHONE_NUMBER,
        to=mobile_number
    )
    return otp

def verify_otp(request):
    if request.method == 'POST':
        otp_entered = request.POST.get('otp', '')
        otp_sent = request.session.get('otp', '')
        if otp_entered == otp_sent:
            return render(request,'interface.html')
        else:
            messages.error(request, "Invalid OTP. Please try again.")
    return render(request, 'verify_otp.html')

