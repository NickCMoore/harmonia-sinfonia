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
