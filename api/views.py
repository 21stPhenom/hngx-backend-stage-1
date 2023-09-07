from django.utils import timezone

from django.http.response import JsonResponse
from rest_framework.response import Response
from rest_framework.views import APIView

# Create your views here.
class DefaultView(APIView):
    def get_weekday_name(self, request, weekday):
        weekday_dict = {
            0: 'Monday',
            1: 'Tuesday',
            2: 'Wednesday',
            3: 'Thursday',
            4: 'Friday',
            5: 'Saturday',
            6: 'Sunday'
        }

        return weekday_dict[weekday]
    
    def get(self, request, *args, **kwargs):
        if len(request.query_params) != 0:
            params = request.query_params
            weekday_as_int = timezone.now().weekday()
            weekday_name = self.get_weekday_name(request, weekday_as_int)

            response_data = {
                'slack_name': params['slack_name'],
                'track': params['track'],

                'current_day': weekday_name,
                'utc_time': timezone.now(),
                'github_file_url': "https://github.com/21stPhenom/hngx-backend-stage-1/blob/dev/api/views.py",
                'github_repo_url': "https://github.com/21stPhenom/hngx-backend-stage-1/",
                'status_code': 200
            }

            return JsonResponse(response_data)
    
        return Response(status=400)
    
api_endpoint = DefaultView.as_view()