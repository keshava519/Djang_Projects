from django.shortcuts import render

# Create your views here.
def session_view(request):
    count=request.session.get('count',0)
    newcount=count+1
    request.session['count']=newcount
    response = render(request,'testapp/session.html',{'count':newcount})
    print(request.session.get_expiry_age())
    print(request.session.get_expiry_date())
    return response
