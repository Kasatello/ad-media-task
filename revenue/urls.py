from django.urls import path

from .views import RevenueStatisticAPIView


urlpatterns = [
    path(
        "statistic",
        RevenueStatisticAPIView.as_view(),
        name="revenue-statistic-spend"
    )
]
