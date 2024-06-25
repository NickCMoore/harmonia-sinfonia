# **_Harmonia Sinfonia_**

Welcome to [](h)

# Table of Contents - Readme

- [**User Experience UX**](#user-experience-ux)
  - [User Stories](#user-stories)
  - [Game Design](#game-design)
- [**Current Features**](#current-features)
- [**Future Features**](#future-features)
- [**Technologies Used**](#technologies-used)
- [**Bugs**](#bugs)
- [**Testing**](#testing)
- [**Deployment**](#deployment)
- [**Credits**](#credits)
  - [**Code**](#code)
  - [**Design**](#design)
- [**Acknowledgements**](#acknowledgements)

# User Experience (UX)

## User Stories

### New Visitors

1. **Sign Up:**

   - _Explanation:_ As a new visitor, I can sign up so that I can join the platform and become a registered member. `(MUST HAVE)`

2. **Site Purpose Clarity:**
   - _Explanation:_ As a new site user, I would like to clearly see the site's purpose, so that I can decide whether or not to sign up. `(MUST HAVE)`

### Registered Users

1. **Log In:**

   - _Explanation:_ As a registered user, I can log in so that I can access my account and interact with the platform. `(MUST HAVE)`

2. **View Posts:**

   - _Explanation:_ As a registered user, I can view posts so that I can see content shared by other orchestra members. `(MUST HAVE)`

3. **Create New Posts:**

   - _Explanation:_ As a registered user, I can create new posts so that I can share my own content with the orchestra community. `(MUST HAVE)`

4. **Delete Posts:**

   - _Explanation:_ As a registered user, I can delete my own posts so that I can remove content I no longer want to share. `(MUST HAVE)`

5. **Like Posts:**

   - _Explanation:_ As a registered user, I can like posts so that I can express appreciation for content shared by others. `(MUST HAVE)`

6. **Comment on Posts:**

   - _Explanation:_ As a registered user, I can comment on posts so that I can engage in discussions with other members. `(MUST HAVE)`

7. **Delete Comments:**

   - _Explanation:_ As a registered user, I can delete my own comments so that I can remove comments I no longer want to share. `(MUST HAVE)`

8. **Follow/Unfollow Members:**

   - _Explanation:_ As a registered user, I can follow/unfollow members so that I can customise my feed and stay updated on specific members. `(MUST HAVE)`

9. **View Post Timestamp:**

   - _Explanation:_ As a registered user, I can view the timestamp of posts so that I can see when the posts were made for context. `(MUST HAVE)`

10. **Notifications:**

    - _Explanation:_ As a registered user, I can receive notifications so that I can stay updated on interactions with my content. `(MUST HAVE)`

11. **Search Functionality:**

    - _Explanation:_ As a registered user, I can search for posts and members so that I can quickly find specific content or users. `(MUST HAVE)`

12. **Edit Profile:**

    - _Explanation:_ As a registered user, I can edit my profile so that I can update my personal information and preferences. `(SHOULD HAVE)`

13. **Like Comments:**

    - _Explanation:_ As a registered user, I can like comments so that I can show appreciation for other members' comments. `(SHOULD HAVE)`

14. **Expand Posts:**

    - _Explanation:_ As a registered user, I can expand posts so that I can see the full content of a post without leaving the feed. `(SHOULD HAVE)`

15. **Private Messaging:**

    - _Explanation:_ As a registered user, I can send private messages so that I can communicate privately with other members. `(COULD HAVE)`

16. **Reporting/Flagging:**
    - _Explanation:_ As a registered user, I can report or flag inappropriate content so that it can be reviewed by admins for action. `(COULD HAVE)`

### Admin Users

1. **Delete Posts and Comments:**

   - _Explanation:_ As an admin, I can delete posts and comments so that I can remove inappropriate or violating content from the platform. `(MUST HAVE)`

2. **Flagged Content Review:**

   - _Explanation:_ As an admin, I can review flagged content so that I can manage and moderate reported content effectively. `(MUST HAVE)`

3. **Unflag Content:**

   - _Explanation:_ As an admin, I can unflag content so that I can dismiss flags for content that does not violate guidelines. `(MUST HAVE)`

4. **User Account Suspension:**

   - _Explanation:_ As an admin, I can suspend user accounts so that I can temporarily block members who repeatedly violate guidelines. `(SHOULD HAVE)`

5. **Content Moderation Tools:**
   - _Explanation:_ As an admin, I can use content moderation tools so that I can manage and filter content effectively on the platform. `(COULD HAVE)`

## Design

## Colour Scheme

## Libraries

# Current Features

# Future Features

# Technologies used

# Bugs

# Testing

To view the testing file, please click [here]().

# Deployment

## Local Deployment

## Heroku Deployment

This project uses Heroku, a platform as a service (PaaS) that enables developers to build, run, and operate applications entirely in the cloud.

Deployment steps are as follows, after account setup:

- Select New in the top-right corner of your Heroku Dashboard, and select Create new app from the dropdown menu.
- Your app name must be unique, and then choose a region closest to you (EU or USA), and finally, select Create App.
- From the new app Settings, click Reveal Config Vars, and set the value of KEY to PORT, and the value to 8000 then select add.
- Further down, to support dependencies, select Add Buildpack.
- The order of the buildpacks is important, select Python first, then Node.js second. (if they are not in this order, you can drag them to rearrange them)
- Heroku needs two additional files in order to deploy properly.
  - requirements.txt
  - Procfile

You can install this project's requirements (where applicable) using: pip3 install -r requirements.txt. If you have your own packages that have been installed, then the requirements file needs updated using: pip3 freeze --local > requirements.txt

The Procfile can be created with the following command: echo web: node index.js > Procfile

For Heroku deployment, follow these steps to connect your GitHub repository to the newly created app:

- In the Terminal/CLI, connect to Heroku using this command: heroku login -i
- Set the remote for Heroku: heroku git:remote -a <app_name> (replace app_name with your app, without the angle-brackets)
- After performing the standard Git add, commit, and push to GitHub, you can now type: git push heroku main

The frontend terminal should now be connected and deployed to Heroku.

# Credits

## Code

## Design

# Acknowledgements

[Back to top](#contents)
