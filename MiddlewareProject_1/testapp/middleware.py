class ExcutionFlowMiddleware(object):
    def __init__(self,get_response):
        self.get_response=get_response

    def __call__(self,request):
        print('This line is added at pre-processing request')
        response=self.get_response(request)
        print('This line is added at Post-Processing request')
        return response


from django.http import HttpResponse
class AppMaintenanceMiddleware(object):
    def __init__(self,get_response):
        self.get_response=get_response

    def __call__(self,request):
        response=self.get_response(request)
        return HttpResponse('<h1>APP is under Maintenance please try after Two days!!!</h1>')

class ErrorMessageMiddleware(object):
    def __init__(self,get_response):
        self.get_response=get_response

    def __call__(self,request):
        response=self.get_response(request)
        return response

    def process_exception(self,request,exception):
        s1='<h1>We are facing some Technical problem would you try after some time...</h1>'
        s2='<h2>Raised Exception:{}</h2>'.format(exception.__class__.__name__)
        s3='<h2>Raised Message:{}</h2>'.format(exception)
        return  HttpResponse(s1+s2+s3)


class FirstMiddleware(object):
    def __init__(self,get_response):
        self.get_response=get_response

    def __call__(self,request):
        print('This line printed by FirstMiddleware at pre-processing of request')
        response=self.get_response(request)
        print('This line printed by FirstMiddleware at post-processing of request')
        return response

class SecondMiddleware(object):
    def __init__(self,get_response):
        self.get_response=get_response

    def __call__(self,request):
        print('This line printed by SecondMiddleware at pre-processing of request')
        response=self.get_response(request)
        print('This line printed by SecondMiddleware at post-processing of request')
        return response

class ThirdMiddleware(object):
    def __init__(self,get_response):
        self.get_response=get_response

    def __call__(self,request):
        print('This line printed by ThirdMiddleware at pre-processing of request')
        response=self.get_response(request)
        print('This line printed by ThirdMiddleware at post-processing of request')
        return response
