# Find-A-Pet REST API

Find-A-Pet is a pet adoption REST API based on FastAPI and inspired by [Petfinder API](https://www.petfinder.com/developers).
However Find-A-Pet aims not to be a 1:1 clone but a viable full featured open-source alternative to Petfinder.

# Project Structure

    app
    ├── api              - web related stuff.
    │   └── routes       - web routes.
    ├── core             - application configuration, startup events, logging.
    ├── db               - db related stuff.
    │   ├── database     - database configurations.
    ├── models           - sqlalchemy models for this application.
    ├── schemas          - schemas for using in web routes
    │   └── schemas      - schemas for using in web routes.
    ├── tests            - application tests.
    └── main.py          - FastAPI application creation and configuration.
