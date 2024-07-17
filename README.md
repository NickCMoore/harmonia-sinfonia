# **_Harmonia Sinfonia_**

Welcome to Harmonia Sinfonia, a dedicated platform designed to connect orchestra members in a seamless and engaging way. As a musician, I understand the unique challenges faced by orchestra members in staying connected and informed outside of rehearsals and performances.

To view the platform, please ![click here](https://harmonia-sinfonia-ec3a4797e71d.herokuapp.com/).

## Table of Contents

- [**Overview**](#overview)
  - [Problem Statement](#problem-statement)
  - [Target Audience](#target-audience)
  - [Solution](#solution)
- [**Design & Planning**](#design--planning)
  - [Problem Statement](#problem-statement)
  - [Target Audience](#target-audience)
  - [Solution](#solution)
  - [Wireframes](#wireframes)
  - [Design Rationale](#design-rationale)
  - [Data Model Design](#data-model-design)
  - [Agile Approach](#agile-approach)
- [**User Experience**](#user-experience)
  - [User Stories](#user-stories)
- [**Features**](#features)
  - [Current Features](#current-features)
  - [Future Features](#future-features)
- [**Technologies Used**](#technologies-used)
- [**Bugs**](#bugs)
- [**Testing**](#testing)
- [**Security**](#security)
- [**Deployment**](#deployment)
- [**Credits**](#credits)
  - [Code](#code)
  - [Design](#design)
- [**Acknowledgements**](#acknowledgements)

## Design & Planning

### Problem Statement

Orchestra members often face significant challenges in staying connected and informed outside of rehearsals and performances. Traditional methods of communication, such as email or sporadic meetings, can be inefficient and fail to create a cohesive sense of community. Additionally, there is no centralised platform for members to share content, discuss music, or coordinate events effectively. These issues can lead to missed opportunities for collaboration, a lack of engagement, and difficulty in organising events and rehearsals efficiently.

### Target Audience

Harmonia Sinfonia is specifically designed for:

- Orchestra Members: Musicians of all levels who are part of an orchestra and need a centralised platform to stay connected with their peers.
- Music Enthusiasts: Individuals who are passionate about orchestral music and want to engage in discussions, share content, and collaborate on musical pieces.
- Orchestra Administrators: Individuals responsible for organising and managing orchestra activities, including rehearsals, performances, and events.

### Solution

Harmonia Sinfonia aims to address these issues by providing a dedicated platform where orchestra members can:

- Stay Connected: Promote continuous and streamlined communication among members through posts, comments, and private messaging.
- Share Content: Easily share posts, music pieces, and other relevant content within the community, enhancing collaboration and engagement.
- Engage and Collaborate: Generate discussions, likes, and comments to foster a vibrant community and encourage member interaction.
- Coordinate Activities: Efficiently organise and manage events, rehearsals, and performances, ensuring that all members are informed and involved.

By solving these problems, Harmonia Sinfonia aims to enhance the overall experience for orchestra members, ensuring they remain engaged, informed, and connected. This platform not only facilitates better communication and collaboration but also strengthens the sense of community among members, ultimately contributing to a more cohesive and productive orchestra.

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

## Design Rationale

### Introduction

Harmonia Sinfonia's design prioritises user experience by ensuring the platform is intuitive, accessible, and engaging. Key UX principles applied include:

1. Consistency:

- Navigation: Consistent placement of navigation elements across all pages.
- Styling: Uniform color schemes, typography, and button styles.

2. Feedback:

- User Actions: Immediate feedback for actions like liking a post or submitting a comment.
- Form Validation: Real-time validation informs users of errors or successful submissions instantly.

3. Simplicity:

- Clean Layout: Minimalistic design with ample white space and clear section dividers.
- Direct Interactions: Key actions are easily accessible without unnecessary steps.

### Information Hierarchy

- The platform follows a clear information hierarchy to guide users effortlessly:

1. Homepage:

- Dynamic Feed: Displays recent posts, upcoming events, and featured content prominently.
- Navigation Bar: Provides quick access to main sections like profiles, events, and posts.

2. Profiles:

- User Profile Page: Displays personal information, posts, and interactions in a well-organized manner.

3. Posts and Interactions:

- Post Layout: Clear structure with user information, post content, and interaction buttons.
- Comment Threads: Nested comments to show relationships clearly.

4. Notifications:

- Dropdown and Page: Accessible via a bell icon in the navigation bar, with a dedicated page for a comprehensive list.

### Responsive Design

The platform is fully responsive, providing a seamless experience on both desktop and mobile devices:

- Flexible Grid System: Uses Bootstrap’s grid system for a fluid layout.
- Mobile Navigation: Collapses into a hamburger menu on smaller screens.
- Touch-Friendly Elements: Designed with sufficient spacing for touch interaction.

### Colour Scheme

- `#3B0D11` (Dark Burgundy): Used for the hover state of primary buttons.
- `#FFF1E6` (Cream): Used for the site background, button text, and footer text.
- `#2E4057` (Deep Blue): Used for the site text, footer background, and primary header color.
- `#FFC857` (Golden Yellow): Used for hover state of nav links and primary button background.
- `#8D8D92` (Soft Gray): Used for the site background and form container shadows.

![Colour Scheme](/documentation/colour-scheme.png)

[Coolors](coolors.co) was used to create the color palette.

To simplify updates to the global colour scheme, I used CSS :root variables. This allows for easy changes by updating only one value, rather than searching through the entire CSS file.

### Integration with Bootstrap

The site utilises Bootstrap for its responsive grid system and components. Bootstrap's classes and components were customised using the defined color variables to ensure consistency across the site. For example, the navbar, buttons, and form elements are styled to match the brand colors, enhancing the cohesive look and feel.

### Typography

The simple typography on the site was designed for readability and a clean, professional look.

- **Font Family:** Arial, sans-serif is used for its clarity and wide acceptance.
- **Font Sizes:**
*Base Font Size: 16px for body text.
*Headings: Scaled sizes create a visual hierarchy (e.g., h1 is 2.5em, h2 is 1.5em).
- **Font Weights:**
*Bold: For headings and important text.
*Normal: For regular body text.
- **Text Colors:**
*Primary Text Color: `#2E4057` (Deep Blue) for most text.
*Footer Text Color: `#FFF1E6` (Cream) for footer text, contrasting with the #2E4057 background.
- **Text Alignment:**
*Centered Text: For headers and key sections.
*Left-aligned Text: For body content.## Database Design

## Data Model Design

The structure of the database is illustrated using an Entity-Relationship Diagram (ERD). This diagram demonstrates how different entities within the Harmonia Sinfonia platform are interrelated, providing an overview of the data flow and the connections between various models.

![Entity Relationship Diagram](/documentation/entity-relationship-diagram.png)

### Models

In this project, I used Django's built in Allauth library to handle user authentication, registration, and account management. Allauth is an authentication solution that supports aspects such as email verification and social authentication. Also, the use of the Cloudinary library was designed to manage and optimise media assets such as images and videos.

### Users (Allauth User Model)

The `Users` model represents the registered users of the platform. Allauth handles the creation and management of this model.

| PK  | id (unique) | Type       | Notes |
| --- | ----------- | ---------- | ----- |
|     | username    | CharField  |       |
|     | email       | EmailField |       |
|     | password    | CharField  |       |
|     | first_name  | CharField  |       |
|     | last_name   | CharField  |       |

### Profile Model

The `Profile` model extends the user model to include additional information specific to each user, such as display name, bio, and profile pictures managed via Cloudinary.

| PK  | id (unique)  | Type       | Notes               |
| --- | ------------ | ---------- | ------------------- |
| FK  | user_id      | OneToOne   | FK to Users model   |
|     | display_name | CharField  |                     |
|     | bio          | TextField  |                     |
|     | profile_pic  | URLField   | URL from Cloudinary |
|     | bg_pic       | URLField   | URL from Cloudinary |
|     | followers    | ManyToMany | M2M to Users model  |

### Posts Model

The `Posts` model represents the content shared by users. It includes fields for the post content, optional images managed via Cloudinary, and metadata such as the posting time and like relationships.

| PK  | id (unique) | Type          | Notes                          |
| --- | ----------- | ------------- | ------------------------------ |
| FK  | user_id     | ForeignKey    | FK to Users model              |
|     | content     | TextField     |                                |
|     | posted_on   | DateTimeField |                                |
|     | image       | URLField      | URL from Cloudinary (optional) |
|     | likes       | ManyToMany    | M2M to Users model             |
|     | is_flagged  | BooleanField  |                                |

### Comments

The `Comments` model allows users to comment on posts. Each comment is linked to a user and a post, and can also receive likes.

| PK  | id (unique) | Type          | Notes              |
| --- | ----------- | ------------- | ------------------ |
| FK  | user_id     | ForeignKey    | FK to Users model  |
|     | comment     | TextField     |                    |
|     | posted_on   | DateTimeField |                    |
|     | likes       | ManyToMany    | M2M to Users model |
| FK  | post_id     | ForeignKey    | FK to Posts model  |

### Likes

The `Likes` model represents the likes on posts and comments, linking them to users.

| PK  | id (unique) | Type       | Notes                |
| --- | ----------- | ---------- | -------------------- |
| FK  | user_id     | ForeignKey | FK to Users model    |
| FK  | post_id     | ForeignKey | FK to Posts model    |
| FK  | comment_id  | ForeignKey | FK to Comments model |

### Follows

The `Follows` model captures the follow relationships between users, indicating who follows whom.

| PK  | id (unique) | Type       | Notes             |
| --- | ----------- | ---------- | ----------------- |
| FK  | follower_id | ForeignKey | FK to Users model |
| FK  | followed_id | ForeignKey | FK to Users model |

### Messages

The `Messages` model handles private messaging between users, including the content of the messages and the timestamps.

| PK  | id (unique) | Type          | Notes             |
| --- | ----------- | ------------- | ----------------- |
| FK  | sender_id   | ForeignKey    | FK to Users model |
| FK  | receiver_id | ForeignKey    | FK to Users model |
|     | content     | TextField     |                   |
|     | sent_at     | DateTimeField |                   |

### Notifications

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

### Flags

The `Flags` model allows users to flag posts and comments for review, including the reason for flagging and the timestamp.

| PK  | id (unique) | Type          | Notes                |
| --- | ----------- | ------------- | -------------------- |
| FK  | user_id     | ForeignKey    | FK to Users model    |
| FK  | post_id     | ForeignKey    | FK to Posts model    |
| FK  | comment_id  | ForeignKey    | FK to Comments model |
|     | reason      | TextField     |                      |
|     | flagged_on  | DateTimeField |                      |

### Admins

The `Admins` model extends the user model to include additional permissions specific to admin users.

| PK  | id (unique) | Type       | Notes             |
| --- | ----------- | ---------- | ----------------- |
| FK  | user_id     | ForeignKey | FK to Users model |
|     | permissions | TextField  |                   |

### Events

The `Events` model represents events or rehearsals posted by the orchestra, including optional images managed via Cloudinary.

| PK  | id (unique) | Type       | Notes                          |
| --- | ----------- | ---------- | ------------------------------ |
| FK  | user_id     | ForeignKey | FK to Users model              |
|     | title       | CharField  |                                |
|     | description | TextField  |                                |
|     | date        | DateField  |                                |
|     | time        | TimeField  |                                |
|     | image       | URLField   | URL from Cloudinary (optional) |

## User Experience

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

## Agile Approach

The development process for Harmonia Sinfonia followed Agile methodology, emphasising continuous improvement throughout the development lifecycle.

### Project Management

GitHub Projects served as the primary Agile tool for managing the development tasks. While GitHub Projects isn't a specialised Agile tool, it was used with the right tags, project creation, and issue assignments to fit the needs of the project.

![GitHub Projects](/documentation/project-management.png)
![GitHub Issues)](/documentation/issues.png)

### User Stories Mapping

User stories were crucial in mapping out the development progress. They were categorised into EPICs A, B, C, D, E, and F based on user types and content specificity. The user stories were organised on a Kanban board, providing a visual representation of the backlog and the current status of tasks. The MoSCoW method was used to prioritise these stories, categorising them into Must have, Should have, Could have, and Won't have, ensuring that the most critical features were developed first.

### Kanban Board

The basic Kanban board in GitHub Projects (see above) helped visualise the workflow and track the progress of tasks. Tasks moved across columns from the backlog, through development stages, to testing, and finally to completion. This setup provided clarity on the workload and helped in managing the project efficiently.

### Continuous Improvement

Despite working solo on this project, continuous improvement was a key focus. Regular retrospectives allowed reflection on past work, identification of areas for improvement, and thinking through possible solutions. This practice ensured that the development processes and product quality were consistently enhanced.

For a detailed view of the project management and task progression, refer to the [GitHub Project board](https://github.com/users/NickCMoore/projects/2).

## Technologies Used

### Content and Design

- HTML: Used for the main site content.
- CSS: Used for the main site design and layout.
- CSS Variables: Used for reusable styles throughout the site.
- Bootstrap: Used as the front-end CSS framework for modern responsiveness and pre-built components.

### Interactivity

- Django Templating and Forms: Used for handling user interactions and form submissions, replacing the need for JavaScript for basic interactivity.
- JavaScript: Notifications are managed dynamically using JavaScript to update the bell icon in the navigation bar when users have unread notifications.

### Backend Development

- Python: Used as the back-end programming language.
- Django: Used as the Python framework for the site.
- asgiref: Used to provide ASGI (Asynchronous Server Gateway Interface) compatibility.
- psycopg2-binary: Used to connect to the PostgreSQL database.
- django-allauth: Used for user authentication.
- django-crispy-forms: Used to style Django forms with Bootstrap.
- django-summernote: Used for WYSIWYG editor in Django admin.
- django-environ: Used for environment variable management.
- django-heroku: Used for easy Heroku deployment.
- gunicorn: Used as the WSGI HTTP server for deploying the site.

- Version Control and Development Environment:

   - Git: Used for version control (git add, git commit, git push).
   - GitHub: Used for secure online code storage.
   - VSCode: Used as a cloud-based IDE for development. 

- autopep8 & Flake8 : Used for automatically formatting Python code to conform to PEP 8.

### Deployment and Hosting

- Heroku: Used for hosting the deployed back-end site.
- whitenoise: Used for serving static files in production.

### Graphics and Design

- Balsamiq: Used to design my site wireframes.

### Utilities and Additional Tools

- Markdown Builder by Tim Nelson: Used to help generate the Markdown files.
- WebAIM Contrast Checker: Used to check contrast between colours on the site.
- Code Spell Checker: Used to check for typos in my README and TESTING files.
- Python Decouple: Used to manage environment variables.
- virtualenv: Used to create isolated Python environments.
- Werkzeug: Used for debugging and serving during development.

## Features

### Current Features

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

## Bugs

To view information about bug tracking and management, please click [here](/TESTING.md).

## Testing

To view the testing file, please click [here](/TESTING.md).

## Security

### Password and Secret Key Management

- **Environment Variables**: All sensitive data, such as passwords and secret keys, are stored in environment variables to prevent exposure. The `.gitignore` file ensures these files are not tracked by version control.

### User Authentication and Permissions

- **Role-Based Access Control**: Uses Django’s authentication system to manage user roles and permissions. These views are protected using the `@login_required` decorator.

### Data Validation and Error Handling

- **Form Validation**: User inputs are validated using Django forms to prevent malicious input.
- **Error Handling**: Custom error pages provide user-friendly messages without exposing sensitive information.

### Deployment Security

- **DEBUG Mode**: DEBUG is set to False in production to prevent detailed error pages from being displayed.
- **HTTPS**: Ensures secure communication between server and client.

### Sensitive Information Handling

- **Secret Management**: Secrets like API keys and database credentials are managed through environment variables, not included in the repository.
- **Configuration Management**: Settings are organised and separated for different environments.

### CSRF Protection

- **CSRF Tokens**: All forms that modify data include CSRF tokens, which protect against Cross-Site Request Forgery (CSRF) attacks. This token is automatically added by Django to every form and validated upon form submission, ensuring that requests are legitimate and come from authenticated users.

These security measures aim to ensure that Harmonia Sinfonia protects user data, maintains secure interactions, and adheres to best practices in web security.

## Deployment

### Heroku Deployment

This project uses Heroku, a platform that allows developers to build, run, and operate applications entirely in the cloud.

#### Deployment Steps

1. **Create a New App:**
   - Go to your Heroku Dashboard.
   - Click on `New` in the top-right corner and select `Create new app`.
   - Enter a unique app name and choose a region (EU or USA), then click `Create App`.

2. **Configure Environment Variables:**
   - Navigate to the `Settings` tab.
   - Click `Reveal Config Vars` and set the following variables:

     ```python
     Key               Value
     CLOUDINARY_URL    your_cloudinary_api_key
     DATABASE_URL      your_elephantsql_database_url
     DISABLE_COLLECTSTATIC 1 (remove this for final deployment)
     SECRET_KEY        your_secret_key
     ```

3. **Prepare for Deployment:**
   - Ensure you have the following files in your project:
     - `requirements.txt`
     - `Procfile`

   - To install required packages, run:

     ```bash
     pip3 install -r requirements.txt
     ```

   - To update your `requirements.txt` file with any new packages, run:

     ```bash
     pip3 freeze --local > requirements.txt
     ```

   - Create a `Procfile` with the following command:

     ```bash
     echo web: gunicorn your_app_name.wsgi > Procfile
     ```

     Replace `your_app_name` with the name of your primary Django app where `settings.py` is located.

4. **Deploy the Application:**
   - **Automatic Deployment:**
     - In Heroku, go to the `Deploy` tab.
     - Connect your GitHub repository and enable Automatic Deployments.

   - **Manual Deployment via Terminal:**
     - Log in to Heroku:

       ```bash
       heroku login -i
       ```

     - Set Heroku remote:

       ```bash
       heroku git:remote -a your_app_name
       ```

       Replace `your_app_name` with your Heroku app name.
     - Push your code to Heroku:

       ```bash
       git push heroku main
       ```

Your project should now be deployed to Heroku!

### Local Deployment

To run this project locally, follow these steps:

#### Clone or Fork the Repository

1. **Cloning:**
   - Go to the GitHub repository.
   - Click on the `Code` button and copy the repository URL.
   - Open Git Bash or Terminal and navigate to your desired directory.
   - Run the following command:

     ```bash
     git clone https://github.com/NickCMoore/harmonia-sinfonia.git
     ```

2. **Forking:**
   - Log in to GitHub and locate the repository.
   - Click on the `Fork` button at the top-right corner.
   - This will create a copy of the repository in your GitHub account.

#### Set Up Local Environment

1. **Install Dependencies:**
   - Navigate to the project directory and run:

     ```bash
     pip3 install -r requirements.txt
     ```

2. **Set Environment Variables:**
   - Create a file named `env.py` in the root directory with the following content:

     ```python
     import os

     os.environ.setdefault("CLOUDINARY_URL", "your_cloudinary_api_key")
     os.environ.setdefault("DATABASE_URL", "your_elephantsql_database_url")
     os.environ.setdefault("SECRET_KEY", "your_secret_key")

     # Local environment only (do not include in production/deployment!)
     os.environ.setdefault("DEBUG", "True")
     ```

3. **Run the Application:**
   - Make necessary migrations:

     ```bash
     python3 manage.py makemigrations
     python3 manage.py migrate
     ```

   - Create a superuser:

     ```bash
     python3 manage.py createsuperuser
     ```

   - Load fixtures (if applicable):

     ```bash
     python3 manage.py loaddata file_name.json
     ```

   - Start the Django development server:

     ```bash
     python3 manage.py runserver
     ```

Your local instance of Harmonia Sinfonia should now be running!

### Gitpod Setup

To directly open the project in Gitpod, you need the Gitpod browser extension. Follow the instructions [here](https://www.gitpod.io/docs/browser-extension) to set it up.

Click below to create your own workspace using this repository:

[Open in Gitpod](https://gitpod.io/#https://github.com/NickCMoore/harmonia-sinfonia)

## Credits

### Code

## Acknowledgements

[Back to top](#table-of-contents)
