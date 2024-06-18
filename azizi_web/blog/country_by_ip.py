from django.utils import translation
from ipware import get_client_ip
import requests

def get_country_from_ip(ip):
    # api_key = 'b0e9da421ddda5'  # Replace with your actual ipinfo API key
    # url = f'https://ipinfo.io/{ip}/json?token={api_key}'
    url = f'https://api.iplocation.net/?ip={ip}'
    response = requests.get(url)
    data = response.json()
    return data.get('country_code2')


# class SetLanguageMiddleware:
#     def __init__(self, get_response):
#         self.get_response = get_response
#
#     def __call__(self, request):
#
#         ip, is_routable = get_client_ip(request)
#         if ip:
#             # You can use a third-party service to get the country from the IP
#             # For simplicity, let's assume you have a function `get_country_from_ip`
#             country = get_country_from_ip(ip)
#             print(country)
#             if country == 'IR':
#                 translation.activate('fa')
#             else:
#                 translation.activate('en')
#             request.LANGUAGE_CODE = translation.get_language()
#         response = self.get_response(request)
#         translation.deactivate()
#         return response

def get_lang_by_ip(request):

    ip, is_routable = get_client_ip(request)
    if ip:
        country = get_country_from_ip(ip)
        if country == 'IR':
            return 'fa'
        else:
            return 'en'
