from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from datetime import datetime
from calendar import monthrange

class CustomPagination(PageNumberPagination):
    page_size = 60
    page_size_query_param = 'page_size'
    max_page_size = 60

        

    def get_paginated_response(self, data):
        month = self.request.query_params.get("month",str(datetime.now().date().month))
        year =  self.request.query_params.get("year",str(datetime.now().date().year))
        days  = monthrange(year=int(year),month= int(month))[1]

        constantDuration = [year+"-"+month.zfill(2)+"-"+str(i).zfill(2) for i in range(1,days+1)]
        print(month,year,days,len(constantDuration))

        dataL = [d["day"] for d in data]
        customData = []
        for date in constantDuration:
            if date in dataL:
                item = data[dataL.index(date)]
            else:
                item =  {
                    "id": 0,
                    "user": None,
                    "is_active": False,
                    "day": date,
                    "startTime": "",
                    "endTime": "",
                    "duration": "",
                    "dateTime": "",
                    "transport": 0,
                    "notes": ""
                    }
            customData.append(item)

        return Response({
            'links': {
                'next': self.get_next_link(),
                'previous': self.get_previous_link()
            },
            'count': self.page.paginator.count,
            'page_size': self.page_size,
            'results': customData,
            
        })