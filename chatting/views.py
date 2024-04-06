import json
from django.http import JsonResponse
from django.shortcuts import get_object_or_404, render, redirect
from django.contrib import messages
from twilio.rest import Client
from .forms import LoginForm,Adminlogin
from .models import admin2,message,user,feedback
import random
from django.db.models import Q
    

TWILIO_ACCOUNT_SID = 'ACbe29c08c22bcde0bb83d9132389edf27'
TWILIO_AUTH_TOKEN = '3c256500e95f556fd668bc9ef7ad85e0'
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
        otp_entered = request.POST.get('otp')
        otp_sent = request.session.get('otp')
        if otp_entered == otp_sent:
            return redirect('set_profile_users')
        else:
            messages.error(request, "Invalid OTP. Please try again.")
    mobile_number = request.session.get('mobile_number')
    return render(request, 'login.html',{'mobile_number': mobile_number})

# For Profile set up
def set_profile_users(request):
    mobile_number = request.session.get('mobile_number')
    obj_exists = user.objects.filter(phoneno=mobile_number).exists()

    if obj_exists :
        profile = get_object_or_404(user,phoneno=mobile_number)
    else :
        profile = user(phoneno = mobile_number)
        profile.save()
    
    profile = user.objects.get(phoneno=mobile_number)
    return render(request,'interface.html',{'profile' : profile })


# For verify admin
def verify_admin(request):
    all_rows = admin2.objects.all()
    uname = request.session.get('username')
    psw = request.session.get('password')

    for row in all_rows:
        if row.username == uname and row.password == psw :
            return redirect(set_admin)
        else:
            messages.error(request,"Invalid Username Or Password. Please try again.")

    return render(request, 'login.html',{'username': uname,'password': psw})

# Admin setup
def set_admin(request):
    unm = request.session.get('username')
    psw = request.session.get('password')

    admin = admin2.objects.get(username=unm,password=psw)

    return render(request,'admin.html',{'admin':admin})

# For logout activities
def logout_view(request):
    # log out actions
    return redirect('login')


# for get messages
def get_messages(request, user_id , user2_id):
    messages = message.objects.filter(    # Fetch messages associated with the user
        (Q(uid1=user_id) & Q(uid2=user2_id)) | (Q(uid2=user_id) & Q(uid1=user2_id))
     ).order_by('pk')
    
    u = user.objects.get(pk=user_id)

    message_list = [{'content': message.message ,
                     'align' : 'left' if message.uid1==u else 'right'
                     } for message in messages]
    return JsonResponse({'messages': message_list})


# for saving new messages
def save_messages(request):
    user_id = request.POST.get('sender')
    user2_id = request.POST.get('reciever')
    message_text = request.POST.get('text')

    obj1 = user.objects.filter(pk=user_id).first()
    obj2 = user.objects.filter(pk=user2_id).first()
    
    msg = message.objects.create(uid1=obj1,uid2=obj2,message=message_text)

    return JsonResponse({'success': True})


# for get users 
def get_users(request):
    user_id = request.POST.get('user')
    msg1 = message.objects.filter(uid1=user_id)
    msg2 = message.objects.filter(uid2=user_id)
    userlist = []

    for raw in msg1 :
        if not any(u.uid==raw.uid2.uid for u in userlist):
            u = user.objects.filter(uid=raw.uid2.uid).first()
            userlist.append(u)

    for raw in msg2 :
        if not any(u.uid==raw.uid1.uid for u in userlist):
            u = user.objects.filter(uid=raw.uid1.uid).first()
            userlist.append(u)

    user_list = [{'uid1': user_id,'uid2': user.uid,'name': user.uname,'photo': user.pphoto.url,'about':user.about} for user in userlist]
    return JsonResponse({'users': user_list})

    
# for search user
def search_user(request):
    name = request.POST.get('uname')
    uid1 = request.POST.get('uid')
    u = user.objects.get(pk=uid1)
    list_json = request.POST.get('userlist')
    list = json.loads(list_json)
    users = user.objects.filter(uname=name).exclude(uid__in=list)
    users_data = []
    if users.exists() and u.uname != name:
        users_data = [{'uid1':uid1,'uid2':user.uid, 'photo':user.pphoto.url , 'name': user.uname, 'about':user.about} for user in users]
    else :
        users_data = [{'validity':False}]
    return JsonResponse({'users': users_data})


# for profile page
def profile_view(request):
    profile_id = request.GET.get('profile_id')
    profile = user.objects.get(pk=profile_id)
    return render(request,'profile.html',{'profile':profile})


# for profile updation
def update_profile(request):
    uid = request.POST.get('userid')
    nm = request.POST.get('name')
    about = request.POST.get('about')
    photo = request.FILES.get('photo')

    uid=int(uid)
    profile = user.objects.get(pk=uid)
    profile.uname = nm
    profile.about = about
    if photo :
        profile.pphoto = photo
    profile.save()

    return redirect(set_profile_users)

# delete account
def delete_account(request):
    profile_id = int(request.GET.get('profile_id'))
    u = user.objects.get(pk=profile_id)
    u.delete()
    return redirect(login)


# save feedback
def save_feedback(request):
    text = request.POST.get('text')
    sender = int(request.POST.get('sender'))

    obj = user.objects.filter(pk=sender).first()

    fback = feedback.objects.create(uid1=obj,feedbackmsg=text)

    return JsonResponse({'success': True})


# get feedbacks
def get_feedbacks(request):
    all_objs = feedback.objects.all()

    feedbacks = [{'message':feedback.feedbackmsg,'username':feedback.uid1.uname,'uid':feedback.uid1.uid} for feedback in all_objs]
    return JsonResponse({'feedbacks': feedbacks})


# save all messages
def save_all_message(request):
    adminid = request.POST.get('sender')
    msg = request.POST.get('text')
    
    users = user.objects.exclude(uid=adminid)

    admin = user.objects.filter(pk=adminid).first()

    for u in users :
        message.objects.create(uid1=admin,uid2=u,message=msg)

    return JsonResponse({'success': True})

    



    