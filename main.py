from flask import Flask, redirect, request
import requests
import os

app = Flask(__name__)

@app.route('/redirect', methods=['GET'])
def api_redirect():
    phone_number = request.args.get('phone')  # Fetch the phone number from the query parameters
    if not phone_number:
        return "Error: Phone number is required", 400

    api_url = 'https://n8n.srv792828.hstgr.cloud/webhook/8a9a9643-545e-48ac-9bd7-3b3b7261530c'  # Replace with your API endpoint
    params = {'phone': phone_number}
    response = requests.get(api_url, params=params)

    if response.status_code == 200:
        data = response.json()
        redirect_url = data.get('url')  # Adjust based on your API response structure
        if redirect_url:
            return redirect(redirect_url, code=302)
    return "Error fetching URL", response.status_code

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))  # Use the PORT environment variable or default to 5000
    app.run(host='0.0.0.0', port=port, debug=True)