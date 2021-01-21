<h1>Live at http://django-blogs-app2.herokuapp.com/</h1>

<h1>Description
<h3>The purpose of this project is learn how relational database works, and to demostrate
  power of django's rapid development with minimal amount of code lines, using its class based 
  views like PasswordResetView(),
  PasswordResetDoneView(), 
  they are django's generic view classes which handle all the backend complexity and when called, renders as html.
  similarly django's class based forms like UserCreationForm(), which is used for new user 
  registration and handles all form validation headches.<h3>
  For more info about this project please visit http://django-blogs-app2.herokuapp.com/about/
</h1>
<h1>To clone and run it</h1>
<h4>Step 1: copy this repository github link</h4>
<img src="https://github.com/saurabh-kumar88/flask-crud-api-v1/blob/main/docs/clone%20repo.png">
<h4>Step 1.1: Create your project folder/dir</h4>
<h4>Step 1.2: cd to project folder</h4>
<h4>Step 1.3: Clone repository -> run git clone "link"</h4>
<h4>Step 2: cd to colned project dir</h4>
<h4>Step 2.1: create virtual environment to install python dependecies by</h4>
<h4>run python -m virtualenv venv</h4>
<h4>Step 2.2: cd venv/Scripts then run ./activate or activate (this will activate virtual environment)</h4>
<h4>Step 2.3: TO disable virtual environment just run deactivate</h4>
<h4>Step 2.4: cd to project folder, now install all python dependencies listed in requiremenst.txt file</h4>
<h4>run pip install -r requirements.txt</h4>
<h4>Step 4: Set environment variables</h4>
<h4>Step 4.1: Create a file into the root dir and name it .env (this will holds our environment variables)</h4>
<h4>Step 4.2: Define these environment variables in .env file</h4>

<h4>SQLALCHEMY_DATABASE_URI="mysql://username:password@server/db"</h4>
<h4>="mysql://username:password@server/db"</h4>
<h4>SQLALCHEMY_DATABASE_URI="mysql://username:password@server/db"</h4>
<h4>SQLALCHEMY_DATABASE_URI="mysql://username:password@server/db"</h4>

<h4>or if you are using postgreSQL</h4>
<h4>SECRET_KEY_BLOG_APP="your scecret key"</h4>
<h4>EMAIL_USER="email id"</h4>
<h4>EMAIL_PASSWD="Email password"</h4>
<h4>AWS_ACCESS_KEY_ID="your aws access key id"</h4>
<h4>AWS_SECRET_ACCESS_KEY="your aws access key"</h4>
<h4>AWS_STORAGE_BUCKET_NAME="aws s3 bucket name"</h4>

<h4>Initialize database tables</h4>
run python manage.py makemigrations blog_app
run python manage.py makemigrations users_app
run python manage.py migrate

<h4>step 5: Start dev server by</h4>
<h4>run python manage.py runserver</h4>
<h4>if every things okay then your console should look like this</h4><br>
<img src="https://github.com/saurabh-kumar88/flask-crud-api-v1/blob/main/docs/console%20running%20dev%20server.png">
<br>
