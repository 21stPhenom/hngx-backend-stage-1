from django.utils import timezone

from django.http.response import JsonResponse
from rest_framework.response import Response
from rest_framework.views import APIView

# Create your views here.
class DefaultView(APIView):
    def get_weekday_name(self, weekday):
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
            weekday_name = self.get_weekday_name(weekday_as_int)

            response_data = {
                'slack_name': params.get('slack_name', None),
                'track': params.get('track', None),

                'current_day': weekday_name,
                'utc_time': timezone.now().strftime("%Y-%m-%dT%H:%M:%SZ"),
                'github_file_url': "https://github.com/21stPhenom/hngx-backend-stage-1/blob/dev/api/views.py",
                'github_repo_url': "https://github.com/21stPhenom/hngx-backend-stage-1/",
                'status_code': 200
            }
            if response_data['slack_name'] == None or response_data['track'] == None:
                return JsonResponse({
                    'message': "You omitted one of the required parameters."
                })
            
            return JsonResponse(response_data, status=200)
    
        return Response(status=400)
    
api_endpoint = DefaultView.as_view()