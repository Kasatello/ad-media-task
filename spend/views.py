from django.db.models import Sum
from rest_framework.response import Response
from rest_framework.views import APIView

from revenue.models import RevenueStatistic
from .models import SpendStatistic


class SpendStatisticAPIView(APIView):

    def get(self, request):
        queryset = SpendStatistic.objects.values("name", "date").annotate(
            total_spend=Sum("spend"),
            total_impressions=Sum("impressions"),
            total_clicks=Sum("clicks"),
            total_conversion=Sum("conversion"),
        )

        for entry in queryset:
            entry["revenue"] = RevenueStatistic.objects.filter(
                name=entry["name"], date=entry["date"]
            ).aggregate(total_revenue=Sum("revenue"))["total_revenue"]

        return Response(queryset)
