## Assignment: Coding Dojo Wall

### Objectives:

- Practice connecting a Django application to a database
- Integrate the login app with another app
- Practice one-to-many relationships
- Practice validating user input and using flash messages

Create a wall page (think Facebook news feed) where users will be able to post messages and see the messages posted by other users. Follow the below wireframe.

This app will be integrated with our login app. After successfully logging in or registering, a user should be redirected to localhost:8000/wall, where the wall is displayed.

![Assignment Sketch](wall_assignment.png)

Once you get the messages functionality working, allow users to post comments for any message. Comments should be in a separate database table from messages.

**Helpful Tip**

In Jinja, say that you made available a variable called 'messages' where 'messages' contained all the messages in the Wall. For some reason, the following code would not work:

```python
{% for comment in message.comments.all() %}
   <p>{{comment.comment}}</p>
{% endfor %}
```

This however does work:

```python
{% for comment in message.comments.all %}    # no parentheses!
   <p>{{comment.comment}}</p>
{% endfor %}
```

**Extra Credit I (optional but highly recommended)**
Allow the user to delete his/her own messages.

**Extra Credit II (optional but highly recommended)**
Allow the user to delete his/her own message but only if the message was made in the last 30 minutes.

- [x] Complete each of the following routes:

- [x] Create a new Django project and bring in your login app (or recreate it) and create a new wall app
- [x] Set up the necessary models
- [x] Allow users to post messages
- [x] Display all messages on the main page
- [x] Allow users to comment on each message
- [x] Display all comments per message
- [x] NINJA BONUS: Allow users to delete only their own messages
- [x] SENSEI BONUS: Allow the user to delete their own messages only if the message was written within the last 30 minutes
- [ ] SENSEI BONUS: Use AJAX for adding comments, deleting messages, and deleting comments

### My finished project:

![My finished App 1](my_finished_project_login.png)
![My finished App 2](my_finished_project.png)
