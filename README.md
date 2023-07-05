# Personal Blog REST APIs

This repository contains the REST APIs for a personal blog application built with Django. The APIs allow users to register, login, and logout, as well as create, edit, and delete blog posts and comments.

## User APIs

The user APIs allow users to register, login, and logout.

* **Signup:** Users can create a new account by providing their email address, username, and password.
    * URL: `http://localhost:8000/user/signup`
* **Login:** Users can log in to their account using their username and password.
    * URL: `http://localhost:8000/user/login`
* **Logout:** Users can log out of their account.
    * URL: `http://localhost:8000/user/logout`

## Blog APIs
The user has his own blog page, where he can add new blog posts.
Non-authenticated users can see all blog posts, but cannot add new posts or comments.
ONLY authenticated users can add comments on posts.

* **Create comment:** Users can create a new comment on a blog post by providing the content of the comment.
    * URL: `http://localhost:8000/blog/comments/{id}/`
* **Edit comment:** Users can edit an existing comment on a blog post by providing the new content of the comment.
    * URL: `http://localhost:8000/blog/comments/{id}`
* **Delete comment:** Users can delete an existing comment on a blog post.
    * URL: `http://localhost:8000/blog/comments/{id}`

## Running the application

To run the application, you can follow these steps:

```
git clone https://github.com/OmarShamkh/blogapp-rest-apis.git
```
```
cd blogapp-rest-apis/
```
```
python3 manage.py makemigrations
python3 manage.py migrate
python3 manage.py runserver
```

The application will be up and running at http://localhost:8000/blog/posts.

## Frontend

The frontend for the application is hosted at the following repository:

https://github.com/OmarShamkh/blogapp-frontend.git


