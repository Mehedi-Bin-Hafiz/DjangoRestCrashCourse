
from rest_framework.response import Response

def error_404(request,exception):
    message = "this url is not found"
    data = {"message":message, "statusCode":404}

    return Response(data)

def error_500(request):
    message = "logical error is happened"
    data = {"message":message,"statusCode":500}
    return Response(data)
