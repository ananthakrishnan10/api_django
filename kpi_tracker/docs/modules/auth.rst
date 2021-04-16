===========
Auth
===========

---------
Register
---------

``POST /auth/register/``

:body parameters:

.. code-block:: JSON

    {
    "email":"ananthan2@gmail.com",
    "password":"1234",
    "project_name":"new project",
    "address":"velemparambu",
    "phone_number": "8281837694",
    "comments": "hi",
    "first_name":"Anantha",
    "last_name":"krishnan"
    }

:response:

.. code-block:: JSON

    {
    "authorization": {
        "access_token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjE4NDA3MTQ1LCJqdGkiOiJlZDRjNTdkMTdmYjU0ZDg1ODk3ZTE0YzQ4ZTM1NmI5ZSIsInVzZXJfaWQiOjE1LCJlbWFpbCI6ImFuYW50aGFuMkBnbWFpbC5jb20iLCJ1c2VybmFtZSI6IlNZNjMxMCIsImlkIjoxNSwiZmlyc3RfbmFtZSI6IkFuYW50aGEiLCJsYXN0X25hbWUiOiJrcmlzaG5hbiJ9.oX9gTIJO4atneluiq_zBP10AEoxgOxB-v_zdWX2yIi8",
        "refresh_token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTYxODQwNzE0NSwianRpIjoiZDJmYzg5YWYzZTAxNGE4N2FjNzBiY2U3MzYyOGMwYWEiLCJ1c2VyX2lkIjoxNX0.rE_XPBiUFv_SBTMkmfaKQNUN2kO1vLAY0hG3tGQX4qM"
    },
    "email": "ananthan2@gmail.com",
    "username": "SY6310",
    "id": 15,
    "first_name": "Anantha",
    "last_name": "krishnan"
}


---------
Login
---------

``POST /auth/login/``

:body parameters:

.. code-block:: JSON

    {
    "email":"ananthan2@gmail.com",
    "password":"1234"
    }

:response:

.. code-block:: JSON

    {
    "authorization": {
        "access_token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjE4NDA3MTQ1LCJqdGkiOiJlZDRjNTdkMTdmYjU0ZDg1ODk3ZTE0YzQ4ZTM1NmI5ZSIsInVzZXJfaWQiOjE1LCJlbWFpbCI6ImFuYW50aGFuMkBnbWFpbC5jb20iLCJ1c2VybmFtZSI6IlNZNjMxMCIsImlkIjoxNSwiZmlyc3RfbmFtZSI6IkFuYW50aGEiLCJsYXN0X25hbWUiOiJrcmlzaG5hbiJ9.oX9gTIJO4atneluiq_zBP10AEoxgOxB-v_zdWX2yIi8",
        "refresh_token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTYxODQwNzE0NSwianRpIjoiZDJmYzg5YWYzZTAxNGE4N2FjNzBiY2U3MzYyOGMwYWEiLCJ1c2VyX2lkIjoxNX0.rE_XPBiUFv_SBTMkmfaKQNUN2kO1vLAY0hG3tGQX4qM"
    },
    "email": "ananthan2@gmail.com",
    "username": "SY6310",
    "id": 15,
    "first_name": "Anantha",
    "last_name": "krishnan"
    }


---------
Refresh Token
---------

``POST /auth/refresh_token/``

:body parameters:

.. code-block:: JSON

    {
    "refresh_token" : "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjE4NTAxNzE5LCJqdGkiOiJjN2YxMjAzYjljNDA0MDA2ODJlYjJlYTZjYTg4NDVkNSIsInVzZXJfaWQiOjIsImVtYWlsIjoiYW5hbnRoYW5AZ21haWwuY29tIiwidXNlcm5hbWUiOiJTWTk0MDAiLCJpZCI6MiwiZmlyc3RfbmFtZSI6IkFuYW50aGEiLCJsYXN0X25hbWUiOiJrcmlzaG5hbiJ9.QO1I6XoiZDj4Napib645SnKWpiIiaqftpWvST_BABh4"
    }

:response:

.. code-block:: JSON

    {
    "authorization": {
        "access_token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjE4NTQ3OTY0LCJqdGkiOiI4MDg2ZjM4ZTc1Yjk0NDAyOWFiZWVkYmFhYmY1YTZkNCIsInVzZXJfaWQiOjIsImVtYWlsIjoiYW5hbnRoYW4yQGdtYWlsLmNvbSIsInVzZXJuYW1lIjoiU1k2MzYwIiwiaWQiOjIsImZpcnN0X25hbWUiOiJBbmFudGhhIiwibGFzdF9uYW1lIjoia3Jpc2huYW4ifQ.OobA26ljZbfLT6sJWaELrJv253U9I-exZ5WxGZ8JX9s",
        "refresh_token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTYxODU0Nzk2NCwianRpIjoiYzVkMzc0MzZiYzY3NDQ3ODhiY2ZkMzgyMGFiZWUxYTgiLCJ1c2VyX2lkIjoyfQ.QfXkoEOUV2x9FwQ87WPzQKiu8Kj1ENVIOhsqRlsO9xE"
    }
    }