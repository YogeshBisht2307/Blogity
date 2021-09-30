
![Logo](https://www.saaspegasus.com/static/images/web/modern-javascript/django-react-header.png)

    
# Blogity

Blogity is a REST full API Blog application that is build using Django and Django Rest Framework for backend with JWT authentication , ReactJS and Material UI for front-end of the application and MongoDB Atlas for DataBase.


## Status

Project is currently in **Development** Process. **Intial state** of project is running. Time to time Updatation will be reflected in Respository and Readme file.

  
## Features

- JWT Authentication
- Rich Text Editor
- Category and SubCategory Filter
- Comments and Replies
- Social Share
- Cloud DataBase

  
## Tech Stack

**Client:** React, Material UI

**Server:** Python, Django Rest Framework

**DataBase:** MongoDB, Mongodb-Atlas

  
## Current Project Setup

Steup the current state of project using the following steps.

**Server Side Setup:**
```bash
  cd server
```
- Create a virtual environment and activate it then follow below.
```bash
  pip install -r requirements.txt
  cd core
```
- Create a file named as .env 
- Setup following variable in the .env file according to your application and MongoDB-Atlas connection.
```bash
  SECRET_KEY = "Your django Application Sercret key"

  # mongo database secret data

  MONGO_HOST_URL = "Your mongodb-Atlas url"
  MONGO_USERNAME = "Your mongodb-Atlas username"
  MONGO_PASSWORD = "your mongodb-Atlas password"

  #add database name as "Blogity" in MongoDB-Atlas URL
```
- Let's run the migration into database.
```bash
  #return back to server directory

  cd ..
  python manage.py makemigrations
  python manage.py migrate

```
- Now run your server as below :-
```bash
  python manage.py run server
```

Now API server is Running... You can check out for routes in the core/urls.py file.
So let's setup the Client to use the API.

**Client Side Setup:**
```bash
  cd client

  //install all the dependencies
  npm install

  npm run start
```


    
## Contributing

Contributions are always welcome!

See my email (yogeshbisht.2307@gmail.com) and Contact me for ways to get started.

Please adhere to this project's `code of conduct`.

  
## Support

For support, email yogeshbisht.2307@gmail.com.

  