from django.shortcuts import render
import datetime

# Create your views here.
def temp_view(request):
    date=datetime.datetime.now()
    my_dict={'date_msg':date}
    return render(request,'templateApp/wish.html',context=my_dict)
