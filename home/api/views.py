# ------------ DATABASE -------------#
from databaseManager import DatabaseManager
from rest_framework.response import Response

from rest_framework.decorators import api_view
@api_view(['GET','POST'])
def getSchema(request):
    db = DatabaseManager()
    if request.method == 'POST':
        return Response({"results": request.data})
    return Response({"results": db.getDataSchema()})
