from rest_framework import pagination
from rest_framework.views import Response


#  Profile pagination class
class ProfilePagination(pagination.PageNumberPagination):
    # Page max size 
    page_size = 15
    # Page size query param
    page_size_query_param = 'page_size'
    # Paginated response method
    def get_paginated_response(self, data):
        # Returning data + nex & previuos links for user
        return Response({
            'links': {
                'next': self.get_next_link(),
                'previous': self.get_previous_link()
            },
            # Paginator pages count 
            'count': self.page.paginator.count,
            'results': data
        })
        