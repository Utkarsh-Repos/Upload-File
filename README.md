#### Download the zip file of code ###
#### Now install python 3.10 from below command ###
```sudo apt update ```
```sudo apt install python3.10```
<br>
<br>
Extract the code
<br>
Go inside the code directory
<br>
``Upload_Filee/Upload_Filee``
<br>
<br>
create virtual env by below command
<br>
``virtualenv -p python3 venv``
<br>
<br>
activate virtual env from below command
<br>
```source venv/bin/activate```
<br>
<br>
Now install requirements by below command
<br>
``pip install -r requirements.txt``
<br>
<br>
Now migrate the models, by below command
<br>
``python manage.py migrate``
<br>
<br>
Now run below command, to run server
<br>
``python manage.py runserver``
<br>
<br>





# Signup Api
code-location :--
<br>
```Upload_Filee/Upload_Filee/authentication/api/views.py```
## Overview

The `SignUpView` API endpoint handles user registration (sign-up) requests. On successful registration, it returns a pair of JSON Web Tokens (JWT) including a refresh token and an access token.

## Endpoint

- **URL:** `http://127.0.0.1:8000/authenticate/authentication/signup/`
- **Method:** `POST`

## Request

### Headers

- `Content-Type: application/json`

### Body

The request body should contain the following JSON fields:

```json
{
  "email": "string",
  "password": "string"
}
```
### Curl Command 
```commandline
curl --location --request POST 'http://127.0.0.1:8000/authenticate/authentication/signup/' \
--header 'Content-Type: application/json' \
--data-raw '{

    "email":"utj989@gmail.com",
    "password": 123456
}'
```
### signup from UI
- **URL:** `http://127.0.0.1:8000/signup/`






# Log In Api
code-location :--
<br>
```Upload_Filee/Upload_Filee/authentication/api/views.py```
## Overview

The `LoginView` API endpoint handles user login requests. It authenticates the user based on provided credentials and returns a pair of JSON Web Tokens (JWT), including a refresh token and an access token, if the credentials are valid.

## Endpoint

- **URL:** `http://127.0.0.1:8000/authenticate/authentication/login/`
- **Method:** `POST`

## Request

### Headers

- `Content-Type: application/json`

### Body

The request body should contain the following JSON fields:

```json
{
  "email": "string",
  "password": "string"
}
```
### Curl Command 
```commandline
curl --location --request POST 'http://127.0.0.1:8000/authenticate/authentication/login/' \
--header 'Content-Type: application/json' \
--data-raw '{
    "email":"utj989@gmail.com",
    "password": 123456
}'
```
### login from UI
- **URL:** `http://127.0.0.1:8000/`






# TokenRefreshView Documentation
code-location :--
<br>
```Upload_Filee/Upload_Filee/authentication/api/views.py```
## Overview

`TokenRefreshView` is a Django REST framework API view that handles the refreshing of JWT (JSON Web Token) tokens. It requires a refresh token to be provided in the request and, if the token is valid, returns a new access token. Optionally, it can also issue a new refresh token if token rotation is enabled.

## Endpoint

**POST** `http://127.0.0.1:8000/authenticate/authentication/token-refresh/`

## Request

### Headers

- `Content-Type: application/json`

### Body Parameters

- `refresh` (string): The refresh token used to generate a new access token.

### Example Request

```http
POST /authenticate/authentication/token-refresh/ HTTP/1.1
Host: 127.0.0.1:8000
Content-Type: application/json
Content-Length: 249

{
    "refresh":"eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTcyNTgyNzU0MywiaWF0IjoxNzI1NzQxMTQzLCJqdGkiOiJlMzU3ZTQ1MTE2ZWM0YzNiYjZiMWUwMjYzZTNhNWY0YiIsInVzZXJfaWQiOjJ9.smJ8ZMI9FimjYEHQvRE1jmUaVQQws28tdHiKfU6FQiM"
}
```
### Curl Command 
```commandline
curl --location --request POST 'http://127.0.0.1:8000/authenticate/authentication/token-refresh/' \
--header 'Content-Type: application/json' \
--data-raw '{
    "refresh":"eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTcyNTgyNzU0MywiaWF0IjoxNzI1NzQxMTQzLCJqdGkiOiJlMzU3ZTQ1MTE2ZWM0YzNiYjZiMWUwMjYzZTNhNWY0YiIsInVzZXJfaWQiOjJ9.smJ8ZMI9FimjYEHQvRE1jmUaVQQws28tdHiKfU6FQiM"
}'
```



# File Upload 

code-location :--
<br>
```Upload_Filee/Upload_Filee/Fileupload/views.py```

## Overview

The `file_upload` view handles CSV file uploads to update or create `Product` records in the database. This endpoint is designed to process a CSV file containing product data, handle missing values, and ensure data integrity.

File will be uploaded from:--

**URL** `http://127.0.0.1:8000/file-upload/`

## Sample of CSV file that will upload
![img_1.png](img_1.png)


# Generate Summary Report

code-location :--
<br>
```Upload_Filee/Upload_Filee/Fileupload/views.py```


## Overview

The `generate_summary_report` view generates and returns a CSV summary report of product sales by category. The report includes:
- The category name.
- The total revenue for each category.
- The top product in terms of quantity sold within each category.

Summary Report will be Downloaded from:--

**URL** `http://127.0.0.1:8000/generate-report/`



