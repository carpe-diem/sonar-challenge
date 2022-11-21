# Sonar Technical Challenge

## Description

This challenge contains two main parts: The backend (DB / Business Logic) and
the Frontend (Visualization). It has no restriction over a specific framework,
however it should be done in Python, and FastAPI or Flask is preferable to Django,
depending on your level of familiarity. We’re curious to see how you approach
structure, and the technologies, tools, libraries, or packages you use to solve the
problem.

Description: You should create a web server with some pre-populated data (i.e.
at least 1 million registers for the ActivityLogs; at least 1,000 random users, and
20 posts). The tables of the DB are the following:

* Posts: It should contain five main fields (ID, ImageSrc, Title, Description).
* Users: For this scope it will be very simple: just an unique ID and a username.
    Any password/login/authentication required.
* ActivityLogs: It should contain three main fields (userId, interactionType, timestamp).
    Here, interactionType can be “Like” or “View”

Visually (Frontend) we should be able to see four views/pages, ideally using React
or NextJS, depending on your level of familiarity:
*  /login: Simple form where you can enter your username, or create a new user.
    You can save the username information in the localStorage for example,
    to have some persistence.
*  / : You must be able to see all the posts with the corresponding title (Not the description).
    And you can perform two actions: Give a “like” to the post, or navigate into the details
    page given a click on the image or title of the post. For this view you need to be logged in,
    otherwise you should be redirected to the /login page.
*  /[postId]: depending on the slug (postId), you should load the full
    information of a post, that includesthe title, the details, the image, and the
    number of likes for that post (Not the number of views over it). Each time
    a user navigates to that page, you should register a new view event in the
    ActivityLogs table. This page also needs to be “logged in”.
* /dashboard: A public view with simple stats: The top 5 most viewed posts
    and the top 5 most liked posts with the corresponding number. And the
    number of “registered” users.

You’re completely free to use the styles that you consider for the views.
Note: The following things are optional - not required - but will give additional
points:
* Use container technologies (Docker) to run the project.
* Use any kind of design pattern to solve the problem.
You should upload your code to a public repo and send us the link when you
consider it ready. Good luck!

## Run it
Run the server with:
docker network create default_network
    $ uvicorn main:app --reload

http://0.0.0.0:8000/docs

## References
* https://fastapi.tiangolo.com/es/tutorial/sql-databases/
* https://pydantic-docs.helpmanual.io/
* https://alembic.sqlalchemy.org/en/latest/
