from rest_framework import pagination
from rest_framework.views import Response

# Define a custom pagination class called BeatPagination
class BeatPagination(pagination.PageNumberPagination):
    # Set the default page size to 12
    page_size = 12
    
    # Allow the client to specify a custom page size using the 'page_size' query parameter
    page_size_query_param = 'page_size'
    
    # Override the get_paginated_response method to customize the pagination response
    def get_paginated_response(self, data):
        # Create a response object with the following structure:
        # {
        #     'links': {
        #         'next': <next page URL>,
        #         'previous': <previous page URL>
        #     },
        #     'count': <total number of items>,
        #     'results': <paginated data>
        # }
        return Response(
            {
                # Links to the next and previous pages
                'links': {
                    'next': self.get_next_link(),
                    'previous': self.get_previous_link()
                },
                # Total number of items in the dataset
                'count': self.page.paginator.count,
                # The paginated data
                'results': data
            }
        )