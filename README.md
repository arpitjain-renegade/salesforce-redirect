# Python API Redirect

This project is a simple web application that calls an external API and redirects the user to the URL received in the response. It is built using Flask.

## Project Structure

```
python-api-redirect
├── app
│   ├── __init__.py
│   ├── main.py
│   └── utils.py
├── requirements.txt
├── .gitignore
└── README.md
```

## Requirements

To run this project, you need to install the required dependencies. You can do this by running:

```
pip install -r requirements.txt
```

## Running the Application

1. Navigate to the project directory:

   ```
   cd python-api-redirect
   ```

2. Run the application:

   ```
   python -m app.main
   ```

3. Open your web browser and go to `http://localhost:5000` to access the application.

## API Endpoint

The application exposes an endpoint that calls an external API. You can customize the API URL in the `app/utils.py` file.

## Contributing

Feel free to submit issues or pull requests if you have suggestions or improvements for the project.