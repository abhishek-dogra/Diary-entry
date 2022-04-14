from django.shortcuts import render
from django.http import HttpResponseRedirect

from .models import user, diaryEntry

from django.utils import timezone
from validate_email import validate_email
# Create your views here.
def homepage(request):
    if 'user_id' in request.session:
        cont=user.objects.get(id=request.session.get('user_id'))
        return render(request,"diary/all_names.html",{'cont':cont})
    return HttpResponseRedirect('/login')

def login_page(request):
    if 'user_id' in request.session:
        return HttpResponseRedirect('/')
    return render(request,"diary/login_page.html")

def register_page(request):
    return render(request,"diary/registration_page.html")

def check_reg(request):
    un=request.POST['username']
    em=request.POST['email']
    p1=request.POST['pass1']
    p2=request.POST['pass2']
    if(p1!=p2):
        return render(request,"diary/registration_page.html",{"passError":True})
    emc=user.objects.filter(email__iexact=em)
    if emc.exists():
        return render(request,"diary/registration_page.html",{"emailError1":True})
    is_valid = validate_email(em,verify=True)
    if is_valid==False:
        return render(request,"diary/registration_page.html",{"emailError2":True})
    user.objects.create(username=un,email=em,password=p1)
    return HttpResponseRedirect("/")

def check_log(request):
    ee=request.POST['email']
    pe=request.POST['pass']
    a=user.objects.filter(email__iexact=ee,password__iexact=pe)
    if a.exists() :
        v=a[0]
        request.session['user_id']=v.id
        request.session['user_name']=v.username
        return HttpResponseRedirect("/")
    else:
        return HttpResponseRedirect("/")

def make_entry(request):
    return render(request,"diary/make_entry.html")

def save_entry(request):
    dn=request.POST['dname']
    de=request.POST['dentry']
    tn=timezone.now()

    usah=user.objects.get(id=request.session.get('user_id'))

    a=diaryEntry.objects.create(user=usah,name=dn,dateTime=tn,entry=de)
    return HttpResponseRedirect('/')

def view_entry(request,qid):
    cont=user.objects.get(id=request.session.get('user_id')).entries.get(id=qid)
    return render(request,"diary/view_entry.html",{'cont':cont})

def logout(request):
    del request.session['user_id']
    return HttpResponseRedirect('/')

def edit_entry(request,qid):
    ent=user.objects.get(id=request.session.get('user_id')).entries.get(id=qid)
    return render(request,'diary/edit_entry.html',{'cont':ent})

def save_edits(request,qid):
    tbe=user.objects.get(id=request.session.get('user_id')).entries.get(id=qid)
    en=request.POST['ename']
    ee=request.POST['eentry']
    tbe.name=en
    tbe.entry=ee
    tbe.save()
    return HttpResponseRedirect("/")

def delete_entry(request,qid):
    tbd=user.objects.get(id=request.session.get('user_id')).entries.get(id=qid).delete()
    return HttpResponseRedirect('/')
