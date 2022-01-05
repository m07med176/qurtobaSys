from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from datetime import datetime
from calendar import monthrange


class CustomPagination(PageNumberPagination):
    page_size = 60
    page_size_query_param = 'page_size'
    max_page_size = 60
    month = datetime.now().date().month
    year = datetime.now().date().year
    days  = monthrange(year=year,month= month)[1]
    def get_paginated_response(self, data):
        return Response({
            'links': {
                'next': self.get_next_link(),
                'previous': self.get_previous_link()
            },
            'days':self.days,
            'count': self.page.paginator.count,
            'page_size': self.page_size,
            'results': data,
            
        })