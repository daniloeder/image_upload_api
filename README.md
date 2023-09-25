README

Image Upload API

This is a simple REST API that allows users to upload images in PNG or JPG format. The API also generates thumbnails of the uploaded images in different sizes.

Installation

To install the project, follow these steps:

Clone the repository:

git clone https://github.com/daniloeder/image_upload_api.git


Change directory to the project directory and activate the virtual environment:

cd image_upload_api && source ./venv/bin/activate


Install the required dependencies:

pip install -r requirements.txt


Install Django REST Framework:

pip install djangorestframework


Create the database tables:

python manage.py migrate


Collect the static files:

python manage.py collectstatic


Usage

To start the development server, run the following command:

python manage.py runserver
The API will now be available at http://localhost:8000/api/

The image_file should be a PNG or JPG file.

Retrieving an image

To retrieve a specific image, send a GET request to the /api/images/<image_id>/ endpoint.

Retrieving a list of images

To retrieve a list of all images, send a GET request to the /api/images/list/ endpoint.

Authentication

Upload an image with authentication

To upload an image with authentication, you can use the following curl command:

curl -X POST   -H "Authorization: Basic $(echo -n root:root | base64 -w0)"   -F "image=@/home/daniloeder/Desktop/cats.jpg"   -F "tier=Premium"   -F "user=1"   http://localhost:8000/api/images/upload/

This command will upload the image cats.jpg to the API with the tier Premium and the user ID 1.

The -H for Authentication that username is root and password is root. This account already exists as a pattern to tests.

Note: You will need to replace the /home/daniloeder/Desktop/cats.jpg path with the path to the image that you want to upload.



Tests

To run the tests, run the following command:

python manage.py test
Docker Compose

To run the project using Docker Compose, follow these steps:

Build the Docker images:
docker-compose build
Start the Docker Compose containers:
docker-compose up -d
The API will now be available at http://localhost:8000/api/

I hope this README file is helpful!
