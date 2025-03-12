# In your app's middleware.py file
from django.shortcuts import redirect
from django.urls import reverse
from django.utils.deprecation import MiddlewareMixin

class NoCacheMiddleware(MiddlewareMixin):
    # Your existing middleware code...
    def process_response(self, request, response):
        # Add headers to prevent caching
        response['Cache-Control'] = 'no-store, no-cache, must-revalidate, max-age=0'
        response['Pragma'] = 'no-cache'
        response['Expires'] = '0'
        return response

class AuthenticationMiddleware(MiddlewareMixin):
    def process_request(self, request):
        # Exempt login page and public pages from authentication check
        exempt_urls = [reverse('login'), reverse('index'), reverse('send_email')]
        
        # If the user is trying to access a protected page but isn't logged in
        if not request.user.is_authenticated and request.path not in exempt_urls and not request.path.startswith('/static/'):
            return redirect('login')