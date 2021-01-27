from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,'newsApp/index.html')

def moviesinfo(request):
    head_msg='2021 Upcoming Movies in Telugu'
    msg1='RRR Directed by SS Rajamouli'
    msg2='Krack Directed by Gopichand Malineni'
    msg3='RED Directed by Kishore Tirumala and Produced by Krishna Chaitanya .'

    my_dict={'head_msg':head_msg,'msg1':msg1,'msg2':msg2,'msg3':msg3}
    return render(request,'newsApp/news.html',context=my_dict)

def sportsinfo(request):
    head_msg='Team India’s complete cricketing schedule for 2021'
    msg1='Australia vs India – January'
    msg2='England tour of India – February to March'
    msg3='IPL 2021 – April to May.'

    my_dict={'head_msg':head_msg,'msg1':msg1,'msg2':msg2,'msg3':msg3}
    return render(request,'newsApp/news.html',context=my_dict)

def politicsinfo(request):
    head_msg='Upcoming Elections in India in 2021'
    msg1='Assam-24 May, 2016 - 23 May, 2021'
    msg2='Kerala-25 May, 2016 - 24 May, 2021'
    msg3='Tamil Nadu-23 May, 2016 - 22 May, 2021'

    my_dict={'head_msg':head_msg,'msg1':msg1,'msg2':msg2,'msg3':msg3}
    return render(request,'newsApp/news.html',context=my_dict)
