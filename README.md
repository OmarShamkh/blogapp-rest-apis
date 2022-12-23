# Personal Blog REST APIs

### User apis:
Create three endpoints for user register, login and logout.

* Signup : with [email , username, password].
* Login : with [username, password].
**************************
### Blog apis:

User has his own blog page, where he can add new blog posts.
- Non-authenticated users can see all blog posts, but cannot add new posts or comment.
- ONLY authenticated user can (create , edit , delete) comment on posts.

****************************

### Run:
1 -
```
 git clone https://github.com/OmarShamkh/blogapp-rest-apis.git
```
2 -
```
cd blogapp-rest-apis/
```
3 -
```
docker compose up
```

***You are done***

End points:

* (GET) List all posts : http://localhost:8000/blog/posts/

* (GET) List post details by id : http://localhost:8000/blog/posts/{id}

* (POST) Add comment to post with post_id : http://localhost:8000/blog/comments/{id}

* (PUT) Edit comment : http://localhost:8000/blog/comments/{id}

* (DELETE) Delete comment : http://localhost:8000/blog/comments/{id}

****************************************************

**Here is the frontend repo**:
https://github.com/OmarShamkh/blogapp-frontend.git


### Thats all!
