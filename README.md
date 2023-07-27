# Find-A-Pet REST API

Find-A-Pet is an experimental REST API for pet adoption based on FastAPI and inspired by [Petfinder API](https://www.petfinder.com/developers).
However Find-A-Pet aims not to be a 1:1 clone but a viable full featured open-source alternative to Petfinder.
This project was created for educational purposes and is nowhere near production-ready state.

## Project Structure

    /
    ├── app
    │   ├── api              - web related stuff.
    │   │   └── routes       - web routes.
    │   ├── core             - application configuration, startup events, logging.
    │   ├── db               - database related stuff.
    │   │   └── database     - database configurations.
    │   │   └── crud         - database functions.
    │   ├── models           - sqlalchemy models for this application.
    │   ├── schemas          - pydantic schemas for using in web routes.
    │   └── main.py          - FastAPI application creation and configuration.
    └── tests                - application tests.
        ├── api              - api tests.
        ├── crud             - database tests.
        └── utils            - test utilities.

## Technologies Used
- **Python**
- **FastAPI**
- **PostgreSQL**
- **Poetry**

## Quick Start

##### 1. Checkout the project from github

```
git checkout https://github.com/enev13/composearch.git
```

##### 2. Run the following command to build and start the containers
```
docker-compose up
```
##### 3. Browse the API in your web browser
```
http://localhost:3000/docs
```

## Coverage report

| Name                           | Stmts   | Miss   | Cover   |
| ------------------------------ | ------- | ------ | ------- |
| app/\_\_init\_\_.py            | 0       | 0      | 100%    |
| app/api/\_\_init\_\_.py        | 0       | 0      | 100%    |
| app/api/routes/\_\_init\_\_.py | 0       | 0      | 100%    |
| app/api/routes/animals.py      | 29      | 0      | 100%    |
| app/api/routes/api.py          | 6       | 0      | 100%    |
| app/api/routes/auth.py         | 20      | 0      | 100%    |
| app/api/routes/users.py        | 33      | 0      | 100%    |
| app/core/\_\_init\_\_.py       | 0       | 0      | 100%    |
| app/core/security.py           | 37      | 9      | 76%     |
| app/db/\_\_init\_\_.py         | 0       | 0      | 100%    |
| app/db/crud/\_\_init\_\_.py    | 0       | 0      | 100%    |
| app/db/crud/animals.py         | 25      | 0      | 100%    |
| app/db/crud/users.py           | 54      | 13     | 76%     |
| app/db/database.py             | 21      | 1      | 95%     |
| app/main.py                    | 10      | 0      | 100%    |
| app/models/\_\_init\_\_.py     | 3       | 0      | 100%    |
| app/models/animals.py          | 48      | 0      | 100%    |
| app/models/breeds.py           | 7       | 0      | 100%    |
| app/models/enums.py            | 112     | 0      | 100%    |
| app/models/users.py            | 16      | 0      | 100%    |
| app/schemas/\_\_init\_\_.py    | 3       | 0      | 100%    |
| app/schemas/animals.py         | 49      | 0      | 100%    |
| app/schemas/base.py            | 33      | 0      | 100%    |
| app/schemas/users.py           | 30      | 0      | 100%    |
| tests/\_\_init\_\_.py          | 0       | 0      | 100%    |
| tests/api/\_\_init\_\_.py      | 0       | 0      | 100%    |
| tests/api/test_animals.py      | 96      | 0      | 100%    |
| tests/api/test_main.py         | 7       | 0      | 100%    |
| tests/api/test_users.py        | 156     | 0      | 100%    |
| tests/conftest.py              | 12      | 0      | 100%    |
| tests/crud/\_\_init\_\_.py     | 0       | 0      | 100%    |
| tests/crud/test_animals.py     | 52      | 0      | 100%    |
| tests/crud/test_users.py       | 85      | 0      | 100%    |
| tests/utils/\_\_init\_\_.py    | 0       | 0      | 100%    |
| tests/utils/random.py          | 35      | 0      | 100%    |
| tests/utils/utils.py           | 6       | 0      | 100%    |
| **TOTAL**                      | **985** | **23** | **98%** |

## To Do
- Add model and schema for Adoptions
- Implement the adoption workflow
- Add authorization dependency for each endpoint, based on user privileges
- Functionality for saving a pet to "Favourites"
