import math
from collections import OrderedDict

from rest_framework import pagination
from rest_framework.response import Response


class CustomPagination(pagination.PageNumberPagination):
    page_size = 20
    page_size_query_param = "page_size"
    max_page_size = 20
    page_query_param = "page"

    def get_next_link(self):
        if not self.page.has_next():
            return None
        page_number = self.page.next_page_number()

        return page_number

    def get_previous_link(self):
        if not self.page.has_previous():
            return None
        page_number = self.page.previous_page_number()

        return page_number

    def get_paginated_response(self, data):
        return Response(
            OrderedDict(
                [
                    (
                        "last_page",
                        math.ceil(self.page.paginator.count / self.page_size),
                    ),
                    ("current_page", self.page.number),
                    ("next", self.get_next_link()),
                    ("previous", self.get_previous_link()),
                    ("count", self.page.paginator.count),
                    ("results", data),
                ]
            )
        )
