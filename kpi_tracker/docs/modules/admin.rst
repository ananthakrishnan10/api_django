===========
Admin
===========

------------
Create User
------------

``POST /administrator/user/``

:body parameters:

.. code-block:: JSON

    {
    "email": "arjun1@gmail.com",
    "password": "1234",
    "first_name": "Arjun",
    "last_name": "krishnan",
    "project_name": "new project",
    "address": "velemparambu",
    "phone_number": "8281837694",
    "comments": "hi",
}

:response:

.. code-block:: JSON

    {
    "message": "User added successfully"
    }


-----------
List User
-----------

``GET /administrator/user/``

:response:

.. code-block:: JSON

    [
    {
        "username": "SY6360",
        "email": "ananthan@gmail.com",
        "first_name": "Anantha",
        "last_name": "krishnan",
        "project_name": "new project",
        "address": "velemparambu",
        "phone_number": "8281837694",
        "comments": "hi",
        "unique_id": "SY6360",
        "id": 2,
        "role": 1,
        "password": "1234"
    },
    {
        "username": "SY1859",
        "email": "arjun1@gmail.com",
        "first_name": "Arjun",
        "last_name": "krishnan",
        "project_name": "new project",
        "address": "velemparambu",
        "phone_number": "8281837694",
        "comments": "hi",
        "unique_id": "SY1859",
        "id": 3,
        "role": 2,
        "password": "1234"
    },
    ]

--------------------
Retrieve user by id
--------------------

``GET /administrator/user/{id}/``

:response:

.. code-block:: JSON

    {
    "username": "admin",
    "email": "admin@gmail.com",
    "first_name": "",
    "last_name": "",
    "project_name": "",
    "address": "",
    "phone_number": "",
    "comments": "",
    "unique_id": "",
    "id": 1,
    "role": null,
    "password": "pbkdf2_sha256$260000$lq2JcW0kLgynJkiZPqy6Dy$5IyFGKM3Am8X4ZpNoQkq3rKyVGOXFJ6T8xJq59vnQFk="
    }


--------------------
Edit user by id
--------------------

``PUT /administrator/user/{id}/``

:body parameters:

.. code-block:: JSON

    {
    "email": "arjun1@gmail.com",
    "password": "1234",
    "first_name": "Arjun",
    "last_name": "krishnan",
    "project_name": "new project",
    "address": "velemparambu",
    "phone_number": "8281837694",
    "comments": "hi",
}

:response:

.. code-block:: JSON

    {
    "message": "User updated successfully",
    "data": {
        "email": "arjun@gmail.com",
        "first_name": "Arjun",
        "last_name": "krishnan",
        "project_name": "new project",
        "address": "velemparambu",
        "phone_number": "8281837694",
        "comments": "hi"
    }
    }

--------------------
Delete user by id
--------------------

``DELETE /administrator/user/{id}/``

:response:

.. code-block:: JSON

    {
    "message": "User deleted successfully"
    }

--------------------
Upload excel
--------------------

``POST /administrator/file_upload/``

:body parameters:

.. code-block:: JSON

    {
    "file": "input.xlsx",
    }

:response:

.. code-block:: JSON

    {
    "message": "Supplier_quantity_Files upload successfully",
    "data": [
        {
            "id": 1,
            "month": "Jan",
            "month_actual": "4265",
            "month_target": "614",
            "ytd_actual": "4265",
            "ytd_target": "614",
            "file_id": 1
        },
        {
            "id": 2,
            "month": "Feb",
            "month_actual": "278",
            "month_target": "614",
            "ytd_actual": "2458",
            "ytd_target": "614",
            "file_id": 1
        },
        {
            "id": 3,
            "month": "Mar",
            "month_actual": "500",
            "month_target": "614",
            "ytd_actual": "1831",
            "ytd_target": "614",
            "file_id": 1
        },
        {
            "id": 4,
            "month": "Apr",
            "month_actual": "1571",
            "month_target": "564",
            "ytd_actual": "1779",
            "ytd_target": "602",
            "file_id": 1
        },
        {
            "id": 5,
            "month": "May",
            "month_actual": "1082",
            "month_target": "564",
            "ytd_actual": "1630",
            "ytd_target": "594",
            "file_id": 1
        },
    ]
    }

--------------------
Get data from Excel
--------------------

``GET /administrator/file_data/``

:response:

.. code-block:: JSON

    [
    {
        "id": 1,
        "month": "Jan",
        "month_actual": "4265",
        "month_target": "614",
        "ytd_actual": "4265",
        "ytd_target": "614",
        "file_id": 1
    },
    {
        "id": 2,
        "month": "Feb",
        "month_actual": "278",
        "month_target": "614",
        "ytd_actual": "2458",
        "ytd_target": "614",
        "file_id": 1
    },
    {
        "id": 3,
        "month": "Mar",
        "month_actual": "500",
        "month_target": "614",
        "ytd_actual": "1831",
        "ytd_target": "614",
        "file_id": 1
    },
    {
        "id": 4,
        "month": "Apr",
        "month_actual": "1571",
        "month_target": "564",
        "ytd_actual": "1779",
        "ytd_target": "602",
        "file_id": 1
    },
    ]