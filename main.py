from flask import Flask, redirect, request
import requests

app = Flask(__name__)

@app.route('/redirect', methods=['GET'])
def api_redirect():
    phone_number = request.args.get('phone')  # Fetch the phone number from the query parameters
    if not phone_number:
        return "Error: Phone number is required", 400

    api_url = 'https://api.example.com/get-url'  # Replace with the actual API URL
    params = {'phone': phone_number}  # Pass the phone number as a parameter to the API
    response = requests.get(api_url, params=params)

    if response.status_code == 200:
        data = response.json()
        redirect_url = data.get('url')  # Adjust based on the actual response structure
        if redirect_url:
            return redirect(redirect_url)
    return "Error: Unable to retrieve URL", 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)