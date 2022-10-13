import email
from multiprocessing import context
import os
from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import user_passes_test

from student_auth_app.models import course_tbl, staff_tbl, student_tbl

# Create your views here.
def home(request):
    return render(request,'main_home.html')


def signup(request):
    return render(request,'sign_up.html')

def loginpage(request):
    return render(request,'login_page.html')  

def add_staff(request):
    if request.method=='POST':
        fname=request.POST.get('fname')
        lname=request.POST.get('lname')
        address=request.POST.get('add')
        email=request.POST.get('email')
        username=request.POST.get('uname')
        pwd=request.POST.get('pswd')
        con_pwd=request.POST.get('cpswd')
        gender=request.POST.get('gender')
        mobile=request.POST.get('mob')
        if request.FILES.get('file') is not None:
            image=request.FILES['file']
        else:
            image="/static/image/none.png"
        if con_pwd==pwd:
            if User.objects.filter(username=username).exists():
                messages.info(request,'This username is already taken')
                return redirect('signup')
            elif User.objects.filter(email=email).exists():
                messages.info(request,'This email is already taken')
                return redirect('signup')
            else:
                staff_user=User.objects.create_user(first_name=fname,last_name=lname,email=email,username=username,password=pwd)
                staff_user.save()
                u=User.objects.get(id=staff_user.id)
                staff=staff_tbl(staff_address=address,gender=gender,staff_phone=mobile,image=image,staff=u)
                staff.save()
                return redirect('loginpage')
        else:
            messages.info(request, 'Password doesnt match!!!!!!!')
            print("Password is not Matching.. ") 
            return redirect('signup')
    else:
        return render(request,'sign_up.html')

def user_login(request):
    if request.method=='POST':
        username=request.POST['uname']
        password=request.POST['pswd']
        user1=auth.authenticate(username=username,password=password)
        if user1 is not None:
            if user1.is_staff:
                auth.login(request,user1)
                return redirect('admin_home')
            else:
                auth.login(request, user1)
                messages.info(request, f'Welcome {username}')
                return redirect('staff_home')
        else:
            messages.info(request, 'Invalid Username or Password. Try Again.')
            return redirect('loginpage')
    else:
        return redirect('loginpage')

@login_required(login_url='user_login')
@user_passes_test(lambda u: u.is_superuser,login_url='user_login')
def admin_home(request):
    return render(request,'admin/admin_home.html')

@login_required(login_url='user_login')
def staff_home(request):
    return render(request,'staff/staff_home.html')

@login_required(login_url='user_login')
def course_load(request):
    # uid = User.objects.get(id=request.session["uid"])
    return render(request,'admin/add_course.html')


@login_required(login_url='user_login')
def add_course(request):
    if request.method=='POST':
        cors=request.POST['course']
        cfee=request.POST['cfee']
        print(cors)
        crs=course_tbl()
        crs.course_name=cors
        crs.fee=cfee
        crs.save()
        print("hii")
        return redirect('admin_home')


@login_required(login_url='user_login')
def add_stud(request):
    courses=course_tbl.objects.all()
    context={'courses':courses}
    return render(request,'admin/add_student.html',context)

@login_required(login_url='user_login')
def add_student(request):
    if request.method=='POST':
        sname=request.POST['sname']
        address=request.POST['add']
        age=request.POST['age']
        jdate=request.POST['jdate']
        sel1 = request.POST['sel']
        course1=course_tbl.objects.get(id=sel1)
        mob=request.POST['mob']
        std=student_tbl(student_name=sname,
                    address=address,
                    age=age,
                    joining_date=jdate,
                    course=course1,
                    phone_number=mob)
        std.save()
        messages.info(request, f'{sname} is successfully added')
        return redirect('add_stud')


@login_required(login_url='user_login')
@user_passes_test(lambda u: u.is_superuser,login_url='user_login')
def ad_show_students(request):
    std=student_tbl.objects.all()
    return render(request,'admin/show_student.html',{'std':std})

@login_required(login_url='user_login')

# @allowed_users(allowed_roles=['staff_tbl'])
def st_show_students(request):
    std1=student_tbl.objects.all()
    return render(request,'staff/st_show_student.html',{'std1':std1})

@login_required(login_url='user_login')
def view_staff(request):
    std=staff_tbl.objects.all()
    return render(request,'admin/show_staff.html',{'std':std}) 

@login_required(login_url='user_login')
def edit_page(request,pk):
    stud1=student_tbl.objects.get(id=pk)
    courses=course_tbl.objects.all()
    return render(request,'admin/edit_student.html',{'stud_info':stud1,'cou':courses})

def edit_stud(request,pk):
    if request.method=='POST':
        stud=student_tbl.objects.get(id=pk)
        stud.student_name=request.POST.get('sname')
        stud.address=request.POST.get('add')
        stud.age=request.POST.get('age')
        stud.joining_date=request.POST.get('jdate')
        stud.phone_number=request.POST.get('mob')
        c_id=request.POST.get('cname')
        cor=course_tbl.objects.get(id=c_id)
        stud.course=cor 
        stud.save()
        return redirect('ad_show_students')
    return render(request,'edit_student.html')

@login_required(login_url='user_login')
def delete1(request,pk):
    stud1=student_tbl.objects.get(id=pk)
    stud1.delete()
    return redirect('ad_show_students')

@login_required(login_url='user_login')
def delete_staff(request,pk):
    stud1=staff_tbl.objects.filter(id=pk)
    stud1.delete()
    return redirect('view_staff')

@login_required(login_url='user_login')
def edit_staff(request):
    staff1=staff_tbl.objects.get(staff=request.user)
    context={'st':staff1}
    return render(request,'staff/edit_profile.html',context)

@login_required(login_url='user_login')
def edit_profile(request,pk):
    if request.method=='POST':
        staf=staff_tbl.objects.get(id=pk)
        staf.staff.first_name=request.POST.get('fname')
        staf.staff.last_name=request.POST.get('lname')
        staf.staff_address=request.POST.get('add')
        staf.staff.email=request.POST.get('email')
        staf.staff.username=request.POST.get('uname')
        staf.gender=request.POST.get('gender')
        staf.staff_phone=request.POST.get('mob')
        if request.FILES.get('file') is not None:
            if not staf.image == "/static/image/none.png":
                os.remove(staf.image.path)
                staf.image = request.FILES['file']
            else:
                staf.image = request.FILES['file']  
        staf.staff.save()          
        staf.save()
        return redirect('view_profile')
    return render(request,'staff/edit_profile.html')


@login_required(login_url='user_login')
def view_profile(request):
    user1 = staff_tbl.objects.filter(staff=request.user)
    context = { 'user1': user1 }
    return render(request,'staff/view_profile.html',context)

@login_required(login_url='login')
def logout(request):
	auth.logout(request)
	return redirect('home')