### WE have Three endpoints 
1. Base URL http://127.0.0.1:8000/
    This URL takes username and password, authenticate it, fetch role and permissions 
    and displays it on frontend.
2. Api endpoint http://127.0.0.1:8000/api/authenticate/
    This is the api endpoint which also takes username and password as input and gives 
    response of role and permissions as output.
3. http://127.0.0.1:8000/api/register/
    This api endpoint register user using djangorestframework build-in package.
###We have 3 users with different roles and permission assigned to it

###Admin User
username: yasser
password: admin123

###Member User
username: memberuser
password: admin123

###Customer User
username: customeruser
password: admin123

