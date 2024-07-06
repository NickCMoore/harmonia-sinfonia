# **_Harmonia Sinfonia_**

**Background**

Welcome to [Harmonia Sinfonia](https://harmonia-sinfonia-ec3a4797e71d.herokuapp.com/), a dedicated platform designed to connect orchestra members in a seamless and engaging way. As a musician, I understand the importance of staying connected and informed outside of rehearsals and performances. Harmonia Sinfonia aims to bridge this gap by providing a space where members can share content, communicate privately, and stay updated on all orchestra-related activities.

This project combines my passion for music and technology, aiming to foster a vibrant community where members can collaborate, support each other, and enhance their musical journey. Whether members want to share the latest performance, discuss music pieces, or simply stay in touch with fellow musicians, Harmonia Sinfonia is here to support them.

Feel free to view the project [here](https://harmonia-sinfonia-ec3a4797e71d.herokuapp.com/).

# Table of Contents

- [**Overview**](#overview)
  - [Background](#background)
  - [Problem Statement](#problem-statement)
  - [Wireframes](#wireframes)
  - [Design](#design)
  - [Agile Approach](#agile-approach)
  - [Database structure](#database-structure)
- [**User Experience**](#user-experience)
  - [User Stories](#user-stories)
- [**Features**](#features)
  - [Current Features](#current-features)
  - [Future Features](#future-features)
- [**Technologies Used**](#technologies-used)
- [**Bugs**](#bugs)
- [**Testing**](#testing)
- [**Deployment**](#deployment)
- [**Credits**](#credits)
  - [**Code**](#code)
  - [**Design**](#design)
- [**Acknowledgements**](#acknowledgements)

## Background

## Agile Approach

The development process for Harmonia Sinfonia followed Agile methodology, emphasising continuous improvement throughout the development lifecycle.

**Project Management**

GitHub Projects served as the primary Agile tool for managing the development tasks. While GitHub Projects isn't a specialised Agile tool, it was used with the right tags, project creation, and issue assignments to fit the needs of the project.

**User Stories**

User stories were crucial in mapping out the development progress. They were categorised into EPICs A, B, C, D, E, and F based on user types and content specificity. The user stories were organised on a Kanban board, providing a visual representation of the backlog and the current status of tasks. The MoSCoW method was used to prioritise these stories, categorising them into Must have, Should have, Could have, and Won't have, ensuring that the most critical features were developed first.

**Kanban Board**

The basic Kanban board in GitHub Projects helped visualize the workflow and track the progress of tasks. Tasks moved across columns from the backlog, through development stages, to testing, and finally to completion. This setup provided clarity on the workload and helped in managing the project efficiently.

**Continuous Improvement**

Despite working solo on this project, continuous improvement was a key focus. Regular retrospectives allowed reflection on past work, identification of areas for improvement, and brainstorming of solutions. This practice ensured that the development processes and product quality were consistently enhanced.

For a detailed view of the project management and task progression, refer to the [GitHub Project board](https://github.com/users/NickCMoore/projects/2).

## Problem Statement

Orchestra members often face challenges in staying connected and informed outside of rehearsals and performances. Traditional methods of communication, such as email or sporadic meetings, can be inefficient and don't create a sense of community. Also, there is no centralised platform for members to share content, discuss music, or coordinate events effectively.

Harmonia Sinfonia aims to address these issues by providing a dedicated platform where orchestra members can:

- Stay Connected: Promote continuous and streamlined communication among members.
- Share Content: Easily share posts, music pieces, and other relevant content within the community.
- Engage and Collaborate: Generate discussions, likes, and comments to enhance member interaction.
- Coordinate Activities: Efficiently organise and manage events, rehearsals, and performances.

By solving these problems, Harmonia Sinfonia aims to enhance the overall experience for orchestra members, ensuring they remain engaged, informed, and connected.

## Wireframes

Creating the wireframes for Harmonia Sinfonia was important in bringing the project to life. These blueprints helped me visualise the platform's structure and flow, ensuring an intuitive user experience.

For me, it was about more than just placing elements on a page. I imagined how you would navigate, create posts, send messages, and engage with other members. By focusing on both desktop and mobile versions, I aimed to make sure the user experience is smooth and enjoyable on any device.

Below are the wireframes for key sections, illustrating my commitment to a user-friendly and responsive design.

### Homepage

![Homepage (Desktop)](/documentation/wireframes/homepage-desktop.png)
![Homepage (Mobile)](/documentation/wireframes/homepage-mobile.png)

### Posts

![Posts (Desktop)](/documentation/wireframes/posts-desktop.png)
![Posts (Mobile)](/documentation/wireframes/posts-mobile.png)

### Messaging

![Messaging (Desktop)](/documentation/wireframes/messaging-desktop.png)
![Messaging (Mobile)](/documentation/wireframes/messaging-mobile.png)

### Profile

![Profile (Desktop)](/documentation/wireframes/profile-desktop.png)
![Profile (Mobile)](/documentation/wireframes/profile-mobile.png)

### Sign Up

![Sign Up 1 (Desktop)](/documentation/wireframes/signup1-desktop.png)
![Sign Up 2 (Desktop)](/documentation/wireframes/signup2-desktop.png)
![Sign Up (Mobile)](/documentation/wireframes/signup-mobile.png)

### Sign In

![Sign In 1 (Desktop)](/documentation/wireframes/signin1-desktop.png)
![Sign In 2 (Desktop)](/documentation/wireframes/signin2-desktop.png)
![Sign In (Mobile)](/documentation/wireframes/signin-mobile.png)

### Admin

![Admin (Desktop)](/documentation/wireframes/admin-desktop.png)
![Admin (Mobile)](/documentation/wireframes/admin-mobile.png)

## Design

### Data Model Overview

The structure of the database is illustrated using an Entity-Relationship Diagram (ERD). This diagram demonstrates how different entities within the Harmonia Sinfonia platform are interrelated, providing an overview of the data flow and the connections between various models.

![Entity Relationship Diagram](/documentation/entity-relationship-diagram.png)

### Models

In this project, I used Django's built in Allauth library to handle user authentication, registration, and account management. Allauth is an authentication solution that supports aspects such as email verification and social authentication. Also, the use of the Cloudinary library was designed to manage and optimise media assets such as images and videos.

## Users (Allauth User Model)

The `Users` model represents the registered users of the platform. Allauth handles the creation and management of this model.

| PK  | id (unique) | Type       | Notes |
| --- | ----------- | ---------- | ----- |
|     | username    | CharField  |       |
|     | email       | EmailField |       |
|     | password    | CharField  |       |
|     | first_name  | CharField  |       |
|     | last_name   | CharField  |       |

## Profile

The `Profile` model extends the user model to include additional information specific to each user, such as display name, bio, and profile pictures managed via Cloudinary.

| PK  | id (unique)  | Type       | Notes               |
| --- | ------------ | ---------- | ------------------- |
| FK  | user_id      | OneToOne   | FK to Users model   |
|     | display_name | CharField  |                     |
|     | bio          | TextField  |                     |
|     | profile_pic  | URLField   | URL from Cloudinary |
|     | bg_pic       | URLField   | URL from Cloudinary |
|     | followers    | ManyToMany | M2M to Users model  |

## Posts

The `Posts` model represents the content shared by users. It includes fields for the post content, optional images managed via Cloudinary, and metadata such as the posting time and like relationships.

| PK  | id (unique) | Type          | Notes                          |
| --- | ----------- | ------------- | ------------------------------ |
| FK  | user_id     | ForeignKey    | FK to Users model              |
|     | content     | TextField     |                                |
|     | posted_on   | DateTimeField |                                |
|     | image       | URLField      | URL from Cloudinary (optional) |
|     | likes       | ManyToMany    | M2M to Users model             |
|     | is_flagged  | BooleanField  |                                |

## Comments

The `Comments` model allows users to comment on posts. Each comment is linked to a user and a post, and can also receive likes.

| PK  | id (unique) | Type          | Notes              |
| --- | ----------- | ------------- | ------------------ |
| FK  | user_id     | ForeignKey    | FK to Users model  |
|     | comment     | TextField     |                    |
|     | posted_on   | DateTimeField |                    |
|     | likes       | ManyToMany    | M2M to Users model |
| FK  | post_id     | ForeignKey    | FK to Posts model  |

## Likes

The `Likes` model represents the likes on posts and comments, linking them to users.

| PK  | id (unique) | Type       | Notes                |
| --- | ----------- | ---------- | -------------------- |
| FK  | user_id     | ForeignKey | FK to Users model    |
| FK  | post_id     | ForeignKey | FK to Posts model    |
| FK  | comment_id  | ForeignKey | FK to Comments model |

## Follows

The `Follows` model captures the follow relationships between users, indicating who follows whom.

| PK  | id (unique) | Type       | Notes             |
| --- | ----------- | ---------- | ----------------- |
| FK  | follower_id | ForeignKey | FK to Users model |
| FK  | followed_id | ForeignKey | FK to Users model |

## Messages

The `Messages` model handles private messaging between users, including the content of the messages and the timestamps.

| PK  | id (unique) | Type          | Notes             |
| --- | ----------- | ------------- | ----------------- |
| FK  | sender_id   | ForeignKey    | FK to Users model |
| FK  | receiver_id | ForeignKey    | FK to Users model |
|     | content     | TextField     |                   |
|     | sent_at     | DateTimeField |                   |

## Notifications

The `Notifications` model manages notifications sent to users, such as likes, comments, and new messages.

| PK  | id (unique)       | Type          | Notes                |
| --- | ----------------- | ------------- | -------------------- |
|     | notification_type | IntegerField  |                      |
| FK  | to_user           | ForeignKey    | FK to Users model    |
| FK  | from_user         | ForeignKey    | FK to Users model    |
| FK  | post_id           | ForeignKey    | FK to Posts model    |
| FK  | comment_id        | ForeignKey    | FK to Comments model |
| FK  | message_id        | ForeignKey    | FK to Messages model |
|     | date              | DateTimeField |                      |
|     | user_has_seen     | BooleanField  |                      |

## Flags

The `Flags` model allows users to flag posts and comments for review, including the reason for flagging and the timestamp.

| PK  | id (unique) | Type          | Notes                |
| --- | ----------- | ------------- | -------------------- |
| FK  | user_id     | ForeignKey    | FK to Users model    |
| FK  | post_id     | ForeignKey    | FK to Posts model    |
| FK  | comment_id  | ForeignKey    | FK to Comments model |
|     | reason      | TextField     |                      |
|     | flagged_on  | DateTimeField |                      |

## Admins

The `Admins` model extends the user model to include additional permissions specific to admin users.

| PK  | id (unique) | Type       | Notes             |
| --- | ----------- | ---------- | ----------------- |
| FK  | user_id     | ForeignKey | FK to Users model |
|     | permissions | TextField  |                   |

## Events

The `Events` model represents events or rehearsals posted by the orchestra, including optional images managed via Cloudinary.

| PK  | id (unique) | Type       | Notes                          |
| --- | ----------- | ---------- | ------------------------------ |
| FK  | user_id     | ForeignKey | FK to Users model              |
|     | title       | CharField  |                                |
|     | description | TextField  |                                |
|     | date        | DateField  |                                |
|     | time        | TimeField  |                                |
|     | image       | URLField   | URL from Cloudinary (optional) |

# User Experience

## User Stories

To ensure Harmonia Sinfonia meets the needs of its users, I have developed a series of user stories that capture the key functionalities and interactions required by different user groups. These user stories help guide the development process, ensuring that the platform remains user-centered and delivers a valuable experience for all members.

The user stories are prioritised using the MoSCoW method, which categorises features into four groups:

- **Must Have:** Essential features that are fundamental to the platform's functionality and must be included in the initial release.
- **Should Have:** Important features that significantly enhance the user experience but are not critical for the platform's basic operation.
- **Could Have:** Desirable features that improve the user experience but can be deferred to a later release if necessary.
- **Won't Have:** Features that are not considered for the current scope but might be included in future updates.

This prioritisation ensures a clear focus on delivering the most critical features first while allowing for iterative improvements based on user feedback and evolving needs.

Below are the categorised user stories for Harmonia Sinfonia:

### New Visitors (EPIC A)

1. **Sign Up:**

   - _Explanation:_ As a new visitor, I can sign up so that I can join the platform and become a registered member. `(MUST HAVE)`

2. **Site Purpose Clarity:**
   - _Explanation:_ As a new site user, I would like to clearly see the site's purpose, so that I can decide whether or not to sign up. `(MUST HAVE)`

### Registered Users (EPIC B)

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

### Admin Users (EPIC C)

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

# Features

## Current Features

**Homepage**

- Acts as the landing page with navigation links, login/sign-up options, and a brief introduction to the platform.
- Features: Dynamic feed displaying recent posts, upcoming events, and featured content from users.

**Authentication Pages**

- Login Page: Secure login form for returning users.
- Registration Page: Sign-up form for new users, including necessary fields for profile information.
- Password Reset: Links and forms to assist users in resetting forgotten passwords.

**Profiles**

- User Profile Page: Displays user details, their posts, and interactions.
- Edit Profile: Allows users to update their profile information and manage settings.

**Posts and Interactions**

- Posts Page: A list of posts made by users with options to create, edit, or delete posts if the user has the necessary permissions.
- Single Post View: Detailed view of each post with comments, likes, and sharing options.
- Create/Edit Post: Pages/forms where users can add new posts or edit existing ones.

**Comments**

- Linked on Post Pages: Users can view comments related to a post and add their own; editable if posted by the user.

**Search**

- Search Page: Allows users to search for posts, other users, or content within the site.
- Advanced Search Options: Filters to refine search results based on categories, date, relevance, etc.

**Messaging**

- Inbox: A private messaging system where users can view conversations.
- Compose Message: Form to send new messages to other users.
- Message View: Detailed view of conversation threads.

**Notifications**

- Notifications Dropdown/Bar: Real-time updates on interactions like new messages, post likes, comments, or other relevant user activities.

**Feed**

- Dynamic Feed: Aggregates content from followed users and groups, showing recent posts, comments, and perhaps highlights of popular discussions or trending topics.

**Admin**

- Dashboard: For administrators to manage users, content, settings, and view analytics.
- User Management: Admin tools for managing user accounts, permissions, and roles.
- Content Moderation: Tools to review and manage posts, comments, and user submissions.

## Future Features

- About Page: Information about the site, its purpose, and the organisation behind it.
- Contact Page: Form to contact site administrators or support.
- FAQs/Help Section: Helps users understand how to use different aspects of the platform.
- Event Pages: For orchestra to post upcoming events or rehearsals with RSVP functionality.

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
