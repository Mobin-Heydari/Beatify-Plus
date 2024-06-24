from rest_framework import pagination
from rest_framework.views import Response



class CategoryPagination(pagination.PageNumberPagination):
    page_size = 12
    page_size_query_param = 'page_size'
    def get_paginated_response(self, data):
        return Response({
            'links': {
                'next': self.get_next_link(),
                'previous': self.get_previous_link()
            },
            'count': self.page.paginator.count,
            'results': data
        }
    )
        