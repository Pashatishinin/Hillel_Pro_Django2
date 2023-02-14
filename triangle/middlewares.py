from datetime import datetime
from .models import LoggerModel


class LogMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):

        response = self.get_response(request)

        return response


    def process_view(self, request, view_func, view_args, view_kwargs):
        if "admin" in request.path:
            pass
        else:
            print("VIEW FUNC", view_func.__name__)
            print("VIEW ARGS", view_args)
            print("VIEW KWARGS", view_kwargs)
            dictionary = {"PATH": request.path, 'METHOD': request.META["REQUEST_METHOD"], "GET": request.GET,
                          "POST": request.POST, "OS": request.headers['sec-ch-ua-platform'],
                          "HOST": request.headers['HOST']}
            print(dictionary)
            LoggerModel.objects.bulk_create([LoggerModel(path=request.path, method=request.META["REQUEST_METHOD"],
                                                         body=request.POST, host=request.headers['HOST'],
                                                         os=request.headers['sec-ch-ua-platform'],
                                                         data=dictionary, timestamp=datetime.now())])
