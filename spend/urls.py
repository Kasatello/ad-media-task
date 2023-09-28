from django.urls import path

from .views import SpendStatisticAPIView


urlpatterns = [
    path(
        "statistic",
        SpendStatisticAPIView.as_view(),
        name="spend-statistic"
    )
]
