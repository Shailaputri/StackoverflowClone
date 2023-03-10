# StackoverflowClone
Uses Django framework to develop a clone of stackoverflow

Workflow:

1. Setup :     
--- Check if Python, mysql, pipenv/virtualenv server are present.       
--- Make project folder in local machine (and link to git).    
--- Activate virtual env in project folder.     
--- Install Django framework and its dependencies(pillow, django-crispy-forms, freeze).     
--- Create Django project (django-admin startproject).     

2. Templates :        
--- Django templates that display HTML GUI seen by clients, using server side Python.       
--- Common layouts : base.html(block content to be embeded on each page) and home.html.       
--- Make static folder for main.css, main.scss and main.js and update settings.py to make the HTML pages interactive.      

3. Django Admin Setup and Migrations:      
--- makemigrations and create superuser.       

4. Views and URL routing for Authentication of user.      
--- views.py under Migrations using render and UserCreatoinForms.     
--- Create HTML register page.    
--- Create path for register in urls.py under project sub-folder.     
--- Align HTTP methids GET/PUSH for username, password fields.     

5. Django forms to include email in SignUp.     
--- Login and Logout

6. Profile Picture and Profile information - Upload and Delete.     

7. List View.

8. Detail View.

9. Create View.

10. Update View

11. Delete View

12. Adding restrictions a/c to users

13. Comment feature

14. Upvote, downvote buttons

15. Richtext Editor

16. Search feature
