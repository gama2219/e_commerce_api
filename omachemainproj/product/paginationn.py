from rest_framework.pagination import PageNumberPagination

class fetch_pagination(PageNumberPagination):
    page_size=25
    page_query_param='page'
    max_page_size=100