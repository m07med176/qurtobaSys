from rest_framework.views import exception_handler

def custom_exception_handler(exc, context):
    # Call REST framework's default exception handler first,
    # to get the standard error response.
    response = exception_handler(exc, context)

    if response is not None and response.status_code == 404:
        response.data = {  
            "message": "عفواً يوجد مشكله فى السيرفر",  
            "status":  False,  
        }

    if response.status_code == 400:
        response.data = {  
            "message": str(exc.detail['name'][0]) ,  
            "status":  False,  
        }
    return response