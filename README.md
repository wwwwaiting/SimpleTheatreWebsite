# SimpleTheatreWebsite

This is the first assignment for CSC301: Introduction to Software Engineer.  
This app is for actors to check their blocking number based on the actor ID and script ID, and for directors to manage the blocking information.  

#### heroku link
https://simple-theatre-app.herokuapp.com   
Can be accessed:   
https://simple-theatre-app.herokuapp.com/example which shows an example of script line.   
https://simple-theatre-app.herokuapp.com/script/#scriptID 
  - e.g https://simple-theatre-app.herokuapp.com/script/1 
  
Main page:  
https://simple-theatre-app.herokuapp.com/actor.html   
https://simple-theatre-app.herokuapp.com/director.html

### General Introduction
#### Objective:

- Help theater staffs manage the stage blocking information:
  - Need to have database for necessary information like actor list, scripts...
  - Have input/search boxes to let user search/manage the data

##### Personas:

- Michelle The nervous actor
- Dan The hardworking director
- Mike The lighting crew

#### User Stories:

- As Michelle(the actor), I do love acting but sometimes I am too nervious to remember the exact blocking number before I perform. So I want to know my stage blocking number, then I can be in the right blocks during the actual performance.
- As Dan(the director), I want to record the changes I made to the blocing information over and over again so that everyone can be placed perfectly on the stage and actors can know their positions too. 
- As Mike(the lighting crew), I want to know everyone's position on the stage so that I can know where the spotlights should be.

#### Acceptance Criteria:
* The actor blocking information is displayed when user searching a specific script number and actor number.
* The actor blocking information can be edit and saved.
* The actor blcking information changes need to be reflected to all users.

#### Json Files
Use Json file as the database.   

#### docker Setup

To start:

`docker build -t a1-301 .`

`docker run -d --name a1-301-container -p 80:80 a1-301:latest`

`docker start a1-301-container`

To stop/remove container:

`docker stop a1-301-container`

`docker rm a1-301-container`

