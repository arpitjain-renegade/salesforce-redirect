from flask import Flask, redirect, request
import requests

app = Flask(__name__)

@app.route('/redirect', methods=['GET'])
def api_redirect():
    api_url = 'https://api.example.com/get-url'  # Replace with your API endpoint
    response = requests.get(api_url)
    
    if response.status_code == 200:
        data = response.json()
        redirect_url = data.get('url')  # Adjust based on your API response structure
        return redirect(redirect_url, code=302)
    else:
        return "Error fetching URL", response.status_code

if __name__ == '__main__':
    app.run(debug=True)