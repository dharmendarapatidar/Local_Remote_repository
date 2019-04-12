from django.shortcuts import render
from .models import HomeModel, CommentModel
from django.http import HttpResponse
from datetime import datetime
import datetime as dt
import random
li = []
li1 = []
import re

def firstPage(request):
    return render(request, 'firstpage.html')


# Registration View in This fun() I have written validation for user given details
# USer_id and registration number are Auto create fields

def registerview(request):
    if request.method == "POST":
        date = request.POST.get('date')
        time = request.POST.get('time')
        fname = request.POST.get('fname')
        lname = request.POST.get('lname')
        mobile = request.POST.get('mobile')
        if (re.findall("^[9|8|7|6]", mobile)) == "9" or '8' or '7' or "6":
            if len(mobile) >= 10:
                mobile = mobile
            else:
                msg = 'Invalid Contact number'
                typo = 'Registration'
                return render(request, 'registration.html', {'msg1': msg, 'type': typo})
        cont_code = request.POST.get('countryCode')
        qualification = request.POST.get('qualification')
        gender = request.POST.get('gender')
        email = request.POST.get('email')
        password = request.POST.get('password')
        refrence = request.POST.get('refrence')
        all_data = HomeModel.objects.all()
        reg = None
        for s in all_data:
            reg = s.Reg_No
            if reg == None:
                reg = 1000
            else:
                reg += 1
        user_id = random.randint(1111111, 9999999)
        course = request.POST.get('course')
        comment = request.POST.get('comment')
        valid_email = HomeModel.objects.filter(Email=email)
        if not valid_email:
            sav = HomeModel(Reg_No=reg, Date=date, Time=time, First_Name=fname,
                            Last_Name=lname, Mobile=mobile, Country_Code=cont_code,
                            Gender=gender, Email=email, Qualification=qualification,
                            Refrence=refrence, User_Id=user_id, Password=password)
            sav.save()
            comm = CommentModel(Comments=comment, Course_Opted=course, Email=email, home_id=reg)
            comm.save()
            typo = "Thanks"
            dit = {'RegNo': reg, 'UserId': user_id, 'name': fname, 'type': typo}
            return render(request, 'details_of_class.html', context=dit)
        else:
            typo = 'Registration'
            msg = 'This Email id has been taken already so please enter new email id !!!    '
            return render(request, 'registration.html', {'msg': msg, 'type': typo})
    date = datetime.today()
    date = date.time()
    typo = "Registration"
    return render(request, 'registration.html', {'date': date, 'type': typo})


#This login view  here I have created user id as a username
def loginView(request):
    if request.method == "POST":
        user = request.POST.get('userid')
        password = request.POST.get('password')
        details = HomeModel.objects.filter(User_Id=user)
        if details:
            for s in details:
                if s.Password == password:
                    #### Session Creation done here only
                    request.session['username']= user
                    typo = "Filtered"
                    return render(request, 'login.html', {'details': details, 'type': typo})
                else:
                    typo = "loginpage"
                    msg = "Password is not matching with The given User ID"
                    return render(request, 'login.html', {'msg': msg, 'type': typo})
        else:
            typo = "loginpage"
            msg = 'Please enter Valid User Id Number'
            return render(request, 'login.html',{'msg': msg, 'type': typo})
    typo = "loginpage"
    return render(request, 'login.html', {'type': typo})


dict1 = {}


def student_details(request):
    if request.method == "POST":
        from_date = request.POST.get('fdate')
        to_date = request.POST.get('tdate')
        # here i am converting user given date to iso date

        from_date = dt.date(int(from_date[0:4]), int(from_date[5:7]), int(from_date[8:10]))
        to_date = dt.date(int(to_date[0:4]), int(to_date[5:7]), int(to_date[8:10]))  # date converted successfully
        all_details = HomeModel.objects.all()
        date_list = []
        for obj in all_details:
            date_list.append(obj.Date)
        valid_date_list_f_db = []
        sendable_date = []
        sendable_reg = []
        for date_obj in date_list:
            if (date_obj >= from_date) and (date_obj <= to_date):
                date = HomeModel.objects.filter(Date=date_obj)
                valid_date_list_f_db.append(date)
        course_list = []
        for v_r_obj in valid_date_list_f_db:
            data = HomeModel.objects.filter(Reg_No=v_r_obj)
            sendable_reg.append(data)
        sendable_reg2 = []
        A = []
        for a in sendable_reg:
            for b in a:
                if b.Reg_No in A:
                    print(b.Reg_No)
                course = request.POST.get('course')
                c = CommentModel.objects.filter(home_id=b.Reg_No, Course_Opted=course)
                if not c:
                    pass
                else:
                    data = HomeModel.objects.filter(Reg_No=b.Reg_No)
                    A.append(b.Reg_No)
            course_list.append(data)

        print('length of the course List', len(course_list))
        print(course_list)
        return render(request, 'displayonly.html', {'data': course_list})

#113














        # sendable_data1 = []
        # for reg in valid_date_list:
        #     sendable_reg.append(reg)
        # print('sendable regs',sendable_reg)
        # print('length of send_able reg', len(sendable_reg))
        # for v_d_obj in valid_date_list:
        #     d = HomeModel.objects.filter(Date=v_d_obj)
        #     sendable_data1.append(d)
        # print('length of s',len(sendable_data1))
        # return render(request, 'displayonly.html', {'data': sendable_date})
        #



















        # for obj in all_details:
        #     li.append(obj.Date)
        # for d1 in li:
        #     if d1 >= from_date and d1 <= to_date:
        #         li1.append(d1)
        # print("list 1", li1)
        # valid_list = []
        # for obj1 in li1:
        #     for obj1 in (HomeModel.objects.filter(Date=obj1)):
        #         course = request.POST.get('course')
        #         valid = CommentModel.objects.filter(home_id=s, Course_Opted=course)
        #         if valid:
        #             typo = "Details"
        #             valid_list.append(valid)
        # print('valid list', valid_list)
        # for d in valid_list:
        #     print(d)
        #     return render(request, 'student_details.html', {'valid_details': d})
    return render(request, 'student_details.html')


def comment_history(request):
    if request.method == "POST":
        user_id = request.POST.get('uid')
        reg_no = request.POST.get('regno')
        email = request.POST.get('email')
        course = request.POST.get('course')
        all_details = HomeModel.objects.filter(User_Id=user_id, Reg_No=reg_no, Email=email)
        if not all_details:
            msg = '<h1>Details are not matching please check the given values</h1>'
            return render(request, 'comment_details.html', {'msg': msg})
        else:
            print('3')
            typo = "Comment"
            comm = CommentModel.objects.filter(home_id=reg_no, Course_Opted=course)
            return render(request, 'comment_details.html', {'detail': all_details, 'cdtails': comm, 'type': typo})
    type = "Review"
    return render(request, 'comment_details.html', {'type': type})


def allCommentsView(request):
    type = "AllComments"
    email1 = request.POST.get('email')
    comm = CommentModel.objects.filter(Email=email1)
    return render(request, 'comment_details.html', {'comments': comm, 'type':type})


def only_details(request):
    return render(request, 'details_of_class.html')


def note_save_view(request):
    name = request.POST.get('note')
    name = len(str(name))
    if name < 200:
        return HttpResponse("Length Must be 200")
    try:
        user = request.session['token']
    except:
        token = 'Session Log Out To be continue u have to again login thank you'
        return render(request, 'firstpage.html', {'token': token})
    else:
        user_checked = HomeModel.objects.get(User_Id=user)
        typo = 'Note Saved'
        return render(request, 'login.html', {"user": user_checked, 'type':typo})



def session_log_out(request):
    try:
        request.session.get_expiry_age()
        del request.session['username']
    except:
        token = 'Session Log Out  To be continue u have to again log in thank you'
        return render(request, 'firstpage.html', {'token':token})

    else:
        token = "Thanks for Visit here "
        return render(request, 'firstpage.html',{'token':token})


