<<<<<<< HEAD
=======
<<<<<<< HEAD
>>>>>>> first
# django-blog-app

Description

This project is a perfect demonstration of django's rapid development features, it is a basic blog app with some common features like
New user registration, login & logout
Password reset
Default user profile & profile update feature
create new post with update and delete capability
Native comments system
Post title search

Main architecture of this app is relational database, we have mainly two database tables and relations Post-User (one--> many relation ,a user can have multiple post but each post can have only one author)
same as Post-Comment (one --> many, a post can have many comments but a comment can only be associated to one post)

Users can create account and create new post, edit & comment, all these info get stored and can maintained by django's nice admin panel api.

Users can request Password reset, this feature is implemented by django's class based views e.g PasswordResetView(), PasswordResetDoneView(), they are django's generic view classes which handle all the backend complexity and when called, rendered as html. to send Email we have used django's smtp lib which require google's id and password for developer app.

Views: I have tried to used maximum generic and class based views, because they allow rapid developemnt, less code and provide built in feature and methods which can be overridden e.g
ListView() --> To display all posts
DetailView()--> To display particular post with post_id
UpdateView() --> renders Post update form takes post_id
etc.

Django's Form Class & Crispy Forms: Django provide form class which renders pre-compiled html forms and handle authentication, crispy forms is django third party form generation and styling api, it helps in form styling and authentication, by using django's Form class, we can avoid headache of form creation, handling GET and POST validation and styling.

AWS S3 Bucket: I have used heroku cloud platform for deployment of this app, but heroku does not allows local file based storage system, images get deleted when pushed to heroku git repo. so i have to used aws s3 bucket for storage of users uploaded profile image,
once user uploaded profile image to s3 through form, then django only saves image file name in database,
a complete s3 file path is re-calculated every time code request user-profile image

Default-profile (Django signals) : It is a very common feature that, we create user account on any blog site it automatically creates default user profile page, with user name and a default profile pic,

Programmatically it says to create and save a profile instance every time a User instance get saved, this feature is achieved by django's signal method
@receiver(post_save, sender=User)
def method(): # do some code

The decorator @receiver is a special method used for signal handling, it takes two arguments a type of signal (post_save -- fired after a instance get saved ) and sender Database name
So every time a new User instance get saved, save_post signal get triggered which invokes the a method to create default profile.

Scope of Improvements

In web developments, the scope of improvements and addition of new feature are end-less, no app is a perfect.
there is always have room for new features and improvements, I have designed this app as MVP(minimal viable product), for learning & demonstration purpose only, there are few modifications and and features which can be added like
AWS lambda function :
Right now a user can upload any size of profile image to s3, but this is a compete wastage of s3 storage, so we can design aws-lambda function to resize a image to pre-programmed resolution, This will saves storage and also makes our app more faster and responsive.
Session based login
Inter-app Sharing e.g Whatspp, facebook etc
Reply to comment :
To implement this feature we have to add more relational database tables or some no sql approach. 
<<<<<<< HEAD
=======
=======
# django-project-post
>>>>>>> first
>>>>>>> first
