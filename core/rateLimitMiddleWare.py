# middleware.py
from django.http import HttpResponseForbidden
from django.utils import timezone
from collections import defaultdict

class RateLimitMiddleware:
    def __init__(self, get_response, limit=35, duration=60):
        self.get_response = get_response
        self.limit = limit  # Maximum number of requests
        self.duration = duration  # Time window in seconds
        self.requests = defaultdict(list)

    def __call__(self, request):
        if True:
            ip = request.META.get('REMOTE_ADDR')
            current_time = timezone.now()

            # Remove requests older than the time window
            self.requests[ip] = [t for t in self.requests[ip] if (current_time - t).total_seconds() <= self.duration]

            if len(self.requests[ip]) >= self.limit:
                return HttpResponseForbidden("Sorry! You have sent multiple requests in limited time which leads to Rate Limit. Please try again after some time.")

            self.requests[ip].append(current_time)

        response = self.get_response(request)
        return response

