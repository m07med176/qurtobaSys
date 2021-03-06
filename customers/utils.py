from rest_framework.views import exception_handler

def getMessage(data):
    for i in data.keys():
        return data[i][0]
def custom_exception_handler(exc, context):
    # Call REST framework's default exception handler first,
    # to get the standard error response.
    response = exception_handler(exc, context)

    try:
        if response is not None and response.status_code == 404:
            response.data = {  
                "message": "عفواً يوجد مشكله فى السيرفر",  
                "status":  False,  
            }

        if response.status_code == 400:
            response.data = {  
                "message": str(getMessage(exc.detail)) ,  
                "status":  False,  
            }
    except Exception as e:
        return response
    return response