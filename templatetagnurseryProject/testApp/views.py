from django.shortcuts import render
import datetime

# Create your views here.
def datetimeinfo(request):
    date=datetime.datetime.now()
    h=int(date.strftime('%H'))
    name='Keshava'
    if h<12:
        msg='Very Good Morning'
    elif h<16:
        msg='Very Good AfterNoon'
    elif h<21:
        msg='Very Good Evening'
    else:
        msg='Very Good Night'

    my_dict={'date':date,'guest':name,'msg':msg}
    return render(request,'testApp/hello.html',context=my_dict)
