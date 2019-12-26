from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from calendar import monthrange


@api_view(["GET"])
def programmers_day(request):
    try:
        if request.method == "GET":
            weekday_num = 0
            month_num = 0
            days = 256
            year = int(request.GET.get('year'))
            for i in range(1, 12):
                if days - monthrange(year, i)[1] > 0:
                    days -= monthrange(year, i)[1]
                else:
                    weekday_num = (monthrange(year, i)[0] + days)
                    while weekday_num > 7:
                        weekday_num -= 7
                    month_num = i
                    break
            json_pack = JsonResponse({'errorCode': status.HTTP_200_OK,
                                      'dataMessage': f"{days}/{month_num}/{year} and it is the {weekday_num} day of the week"})
            return json_pack
    except ValueError as e:
        return Response(e.args[0], status.HTTP_400_BAD_REQUEST)
    except TypeError as e:
        return Response(e.args[0], status.HTTP_400_BAD_REQUEST)
