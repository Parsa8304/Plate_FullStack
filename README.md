# Plate Detector Fullstack Project

This is a fullstack application for license plate detection, built with a Django backend and a React frontend.

## Features

- User registration and login (with token authentication)
- Upload images to detect license plates
- Modern React UI
- Django REST API backend

## Getting Started

### Backend (Django)

1. Install dependencies:
    ```sh
    pip install -r requirements.txt
    ```
2. Run migrations:
    ```sh
    python manage.py migrate
    ```
3. Start the server:
    ```sh
    python manage.py runserver
    ```

### Frontend (React)

1. Install dependencies:
    ```sh
    cd plate_frontend
    npm install
    ```
2. Start the development server:
    ```sh
    npm start
    ```

## Usage

- Register or log in from the frontend.
- Upload an image to detect the license plate.
- The detected plate number will be displayed.

## Folder Structure

- `Plate_Backend/` - Django backend code
- `plate_frontend/` - React frontend code

## License

MIT
