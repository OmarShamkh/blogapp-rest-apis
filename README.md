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

## Prerequisites

Before running the application, make sure you have the following software installed:

* Docker: Used to create, deploy, and run the application using containerization.
* Python: The programming language used for this project.

## Running the application

To run the application, you can follow these steps:

```
git clone https://github.com/OmarShamkh/blogapp-rest-apis.git
```
```
cd blogapp-rest-apis/
```
```
docker compose up
```

After running the "docker compose up" command, you should see a series of messages in your terminal as Docker builds and starts the containers. Once the application is running, you can verify it by navigating to http://localhost:8000/blog/posts in your web browser.

The application will be up and running at http://localhost:8000/blog/posts.

## Dependencies

This project depends on the following packages:

* django-admin==2.0.1: A high-level Python web framework that encourages rapid development and clean, pragmatic design.
* django-cors-headers==3.13.0: A Django App that adds Cross-Origin Resource Sharing (CORS) headers to responses.
* djangorestframework==3.13.1: A powerful and flexible toolkit for building Web APIs in Django.

## Frontend

The frontend for the application is hosted at the following repository:

https://github.com/OmarShamkh/blogapp-frontend.git

## Contributing

Contributions are welcome! To contribute:

1. Fork the repository.
2. Create a new branch for your changes.
3. Make your changes in your branch.
4. Submit a pull request.


## Project Structure

The project is organized into several main directories:

* `blog/`: Contains the models, views, and templates for the blog functionality.
* `user/`: Contains the models, views, and templates for user authentication.
* `Dockerfile`: Defines the Docker container for the application.


