<!DOCTYPE html>
<html>
<head>
</head>
<body>
  <h1>Image Upload API</h1>
  <p>This is a simple REST API that allows users to upload images in PNG or JPG format. The API also generates thumbnails of the uploaded images in different sizes.</p>
  
  <h2>Installation</h2>
  <p>To install the project, follow these steps:</p>
  <ol>
    <li>Clone the repository:</li>
    <code>git clone https://github.com/daniloeder/image_upload_api.git</code>
    <li>Change directory to the project directory and activate the virtual environment:</li>
    <code>cd image_upload_api && source ./venv/bin/activate</code>
    <li>Install the required dependencies:</li>
    <code>pip install -r requirements.txt</code>
    <li>Install Django REST Framework:</li>
    <code>pip install djangorestframework</code>
    <li>Create the database tables:</li>
    <code>python manage.py migrate</code>
    <li>Collect the static files:</li>
    <code>python manage.py collectstatic</code>
  </ol>
  
  <h2>Usage</h2>
  <p>To start the development server, run the following command:</p>
  <pre><code>python manage.py runserver</code></pre>
  <p>The API will now be available at <a href="http://localhost:8000/api/">http://localhost:8000/api/</a></p>
  <p>The <code>image_file</code> should be a PNG or JPG file.</p>
  
  <h3>Retrieving a list of images</h3>
  <p>To retrieve a list of all images, send a GET request to the <code>/api/images/list/</code> endpoint.</p>
  
  <h2>Authentication</h2>
  
  <h3>Upload an image with authentication</h3>
  <p>To upload an image with authentication, you can use the following curl command:</p>
  <pre><code>curl -X POST -H "Authorization: Basic $(echo -n root:root | base64 -w0)" -F "image=@/home/daniloeder/Desktop/cats.jpg" -F "tier=Premium" -F "user=1" http://localhost:8000/api/images/upload/</code></pre>
  <p>This command will upload the image <code>cats.jpg</code> to the API with the tier Premium and the user ID 1.</p>
  <p>The <code>-H</code> for Authentication that username is root and password is root. This account already exists as a pattern for tests.</p>
  <p>Note: You will need to replace the <code>/home/daniloeder/Desktop/cats.jpg</code> path with the path to the image that you want to upload.</p>
  
  <h2>Docker Compose</h2>
  <p>To run the project using Docker Compose, follow these steps:</p>
  <ol>
    <li>Build the Docker images:</li>
    <code>docker-compose build</code>
    <li>Start the Docker Compose containers:</li>
    <code>docker-compose up -d</code>
  </ol>
  <p>The API will now be available at <a href="http://localhost:8000/api/">http://localhost:8000/api/</a></p>
  <p>I hope this README file is helpful!</p>
</body>
</html>
