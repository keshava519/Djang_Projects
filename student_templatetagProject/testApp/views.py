from django.shortcuts import render
import datetime

# Create your views here.
def studentinfo(request):
    date=datetime.datetime.now()
    name='Keshava'
    rollno=11792292
    branch='Mechanical Engineering'
    college='SVU'

    my_dict={'date':date,'name':name,'rollno':rollno,'branch':branch,'college':college}

    return render(request,'testApp/student.html',context=my_dict)
