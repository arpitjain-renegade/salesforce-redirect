def make_api_call(url):
    import requests

    response = requests.get(url)
    response.raise_for_status()  # Raise an error for bad responses
    return response.json()

def extract_redirect_url(api_response):
    return api_response.get('redirect_url')  # Adjust the key based on the actual API response structure