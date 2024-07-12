# Lesson 8: Working with APIs

## Objective
The objective of this lesson is to teach students how to retrieve and manipulate data from external APIs within the context of the library application. By the end of this lesson, students will understand how to make HTTP requests, handle API responses, integrate API data into their application, and have a basic understanding of common authentication methods for REST APIs.

## Key Points

1. **Introduction to APIs**
   - What is an API?
   - Importance of APIs in modern applications.
   - Overview of RESTful APIs.

2. **REST Verbs and Their Purpose**
   - GET, POST, PUT, DELETE, PATCH
   - Intended purpose of each verb in RESTful APIs.

3. **Common Forms of Authentication for REST APIs**
   - Basic Authentication
   - API Key
   - Bearer Tokens
   - OAuth 2.0

4. **Making HTTP Requests**
   - Using the `requests` library in Python.
   - Making GET and POST requests.
   - Handling API responses.

5. **Parsing JSON Data**
   - Understanding JSON format.
   - Using Python's `json` module to parse JSON data.

6. **Integrating API Data into the Library Application**
   - Fetching book data from an external API.
   - Updating the library application with the fetched data.
   - Handling errors and edge cases.

## Lesson Content

### 1. Introduction to APIs

**Discussion Points:**
- API stands for Application Programming Interface.
- APIs allow different software systems to communicate with each other.
- RESTful APIs follow a set of conventions for creating, reading, updating, and deleting resources over HTTP.

**Further Reading:**
- [🔗 What is an API?](https://www.howtogeek.com/devops/what-is-an-api/) on HowToGeek
- [🔗 RESTful API](https://restfulapi.net/) on Restful API

### 2. REST Verbs and Their Purpose

**Discussion Points:**
- **GET**: Retrieve data from the server.
- **POST**: Send data to the server to create a new resource.
- **PUT**: Update an existing resource on the server.
- **DELETE**: Remove a resource from the server.
- **PATCH**: Partially update an existing resource on the server.

**Further Reading:**
- [🔗 REST API Tutorial](https://restfulapi.net/http-methods/) on RESTful API

### 3. Common Forms of Authentication for REST APIs

**Discussion Points:**
- **Basic Authentication**: Sends the username and password encoded in Base64 with each request.
- **API Key**: Uses a unique key assigned to each user to authenticate requests.
- **Bearer Tokens**: Similar to API Keys but passed differently, often in the `Authorization` header.
- **OAuth 2.0**: A more secure and complex method that involves tokens and multiple steps for authentication.

**Basic Authentication**:
- Basic authentication is a simple authentication scheme built into the HTTP protocol.
- The client sends HTTP requests with the `Authorization` header that contains the word `Basic` followed by a space and a base64-encoded string `username:password`.
- It's not recommended for production use over unsecured HTTP because credentials are easily intercepted.

**Examples**:
```python
import requests
from requests.auth import HTTPBasicAuth

response = requests.get('https://api.example.com/data', auth=HTTPBasicAuth('username', 'password'))
print(response.status_code)
print(response.json())
```

**API Key**:
- An API key is a token that a client provides when making API calls.
- API keys are often sent as a query parameter or as a header.
- They are simple to use but offer minimal security since they can be easily shared.

**Examples**:
```python
import requests

api_key = 'your_api_key'
response = requests.get(f'https://api.example.com/data?api_key={api_key}')
print(response.status_code)
print(response.json())
```

**Bearer Tokens**:
- Bearer tokens are similar to API keys but are typically used in the `Authorization` header.
- Bearer tokens are usually obtained through an OAuth 2.0 flow but can be used independently.
- They provide a simple way to authenticate API requests without exposing sensitive credentials.

**Examples**:
```python
import requests

bearer_token = 'your_bearer_token'
headers = {'Authorization': f'Bearer {bearer_token}'}
response = requests.get('https://api.example.com/data', headers=headers)
print(response.status_code)
print(response.json())
```

**OAuth 2.0**:
- OAuth 2.0 is a more secure and complex authentication method.
- It involves multiple steps including obtaining an access token, which is then used to authenticate API requests.
- OAuth 2.0 provides better security by allowing limited access to user resources without exposing user credentials.

**Examples**:
```python
import requests

access_token = 'your_access_token'
headers = {'Authorization': f'Bearer {access_token}'}
response = requests.get('https://api.example.com/data', headers=headers)
print(response.status_code)
print(response.json())
```

**Further Reading:**
- [🔗 Authentication Best Practices](https://swagger.io/docs/specification/authentication/) on Swagger
- [🔗 Understanding OAuth2](https://www.digitalocean.com/community/tutorials/an-introduction-to-oauth-2) on DigitalOcean

### 4. Making HTTP Requests

**Discussion Points:**
- The `requests` library is a popular Python library for making HTTP requests.
- You can make GET requests to retrieve data and POST requests to send data.

**Examples:**
```python
import requests

# Making a GET request
response = requests.get("https://www.googleapis.com/books/v1/volumes?q=isbn:9780143127550")
if response.status_code == 200:
    print("Success:", response.json())
else:
    print("Failed to retrieve data:", response.status_code)

# Making a POST request
data = {"title": "1984", "author": "George Orwell", "year": 1949}
response = requests.post("https://jsonplaceholder.typicode.com/posts", json=data)
if response.status_code == 201:
    print("Book created:", response.json())
else:
    print("Failed to create book:", response.status_code)
```

**Further Reading:**
- [🔗 Requests: HTTP for Humans](https://docs.python-requests.org/en/latest/) on Requests

### 5. Parsing JSON Data

**Discussion Points:**
- JSON (JavaScript Object Notation) is a lightweight data interchange format.
- The `json` module in Python can be used to parse JSON data.

**Examples:**
```python
import json

# Parsing JSON data
response = '{"title": "1984", "author": "George Orwell", "year": 1949}'
data = json.loads(response)
print(data)
print(f"Title: {data['title']}, Author: {data['author']}, Year: {data['year']}")
```

**Further Reading:**
- [🔗 Working with JSON in Python](https://realpython.com/python-json/) on Real Python

### 6. Integrating API Data into the Library Application

**Discussion Points:**
- Fetching book data from an external API and updating the library application.
- Handling errors and edge cases, such as network issues or invalid data.

**Examples:**
```python
import requests
import json

class LibraryAPI:
    def __init__(self, api_url):
        self.api_url = api_url

    def fetch_books(self):
        response = requests.get(self.api_url)
        if response.status_code == 200:
            return response.json()
        else:
            print("Failed to retrieve data:", response.status_code)
            return []

# Example usage
api_url = "https://www.googleapis.com/books/v1/volumes?q=python"
library_api = LibraryAPI(api_url)
books = library_api.fetch_books()
for book in books['items']:
    volume_info = book['volumeInfo']
    print(f"Title: {volume_info['title']}, Authors: {', '.join(volume_info.get('authors', 'N/A'))}, Published Date: {volume_info.get('publishedDate', 'N/A')}")
```

**Further Reading:**
- [🔗 Python Requests Tutorial](https://realpython.com/python-requests/) on Real Python

## Exercises

**Resources for Exercises**
- **Google Books API Overview and Getting Started**: [Google Books API Overview](https://developers.google.com/books/docs/v1/getting_started)
- **Google Books API API Reference**: [Google Books API Reference](https://developers.google.com/books/docs/v1/reference)

**Exercise 1: Making HTTP Requests**
1. Use the `requests` library to make a GET request to Google Books API. Print the status code and the response data. Recomended endpoints for testing with:
- GET https://www.googleapis.com/books/v1/volumes?q=inauthor:J.K. Rowling
- GET https://www.googleapis.com/books/v1/volumes?q=intitle:Harry Potter
- GET https://www.googleapis.com/books/v1/volumes?q=subject:fiction

**Exercise 2: Parsing JSON Data**
1. Write a function that takes a JSON string as input and returns a dictionary with the parsed data. Use this function to parse the JSON response from the previous Exercise.

**Exercise 3: Fetching Book Data from an API**
1. Create a class `LibraryAPI` in `./library/data_operations/LibraryAPI.py` with a method `fetch_books` that retrieves book data by the user input subject from `GET https://www.googleapis.com/books/v1/volumes?q=subject:fiction` and returns it as a list of dictionaries. 

**Exercise 4: Integrating API Data into the Library Application**
1. Update the main menu to include an option for fetching book data from the API using the `LibraryAPI` class and then saving it into a CSV file using `csv_repository.py`.

## Summary

By the end of Lesson 8, students should be comfortable with making HTTP requests, handling API responses, integrating API data into their Python applications, and understanding basic authentication methods for REST APIs. They will understand how to use the `requests` library to interact with RESTful APIs and how to parse JSON data using Python's `json` module. These skills are essential for building modern applications that interact with external services and APIs



