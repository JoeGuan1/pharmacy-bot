# Discord Bot.

In this milestone, students will create a Discord bot that will serve as a bridge interface between the user and the student's database models created in this class. Database models will be tested against 16 business rules (plus two optional extra-credit business rules) created by the student and previosly approved by 
the class' instructor. 

The following are some examples of business rules for a learning management database system (e.g iLearn). Note that if you have this topic, you cannot use these business rules for your project.: 

1. "Find the Number of students with GPA greater then 3.0 that have not yet applied to grad school"
2. "For each professor that taught the same class, find the number of students that dropped before the drop deadline"
3. "For each professor, show the average grade per course taught by those professors"
4. "For each course, find the number of exams"
5. "For each course, find their prerequisites"
6. "Enroll a student in a course only if the student meets the class prerequisites"
7. "Find the points every student needs to get an A in the courses they are enrolled during a specific 
    semester"
8. "Find the number of students who took the same class within a specific date range"
9. "Update automatically the grade letter table every time a grade for an assignment is inserted into the database"
10. "Create a procedure to find all the students that took a course (passed as a parameter) that is not scheduled this semester" 
11. "Create a function that returns the number of professors that published more than 10 papers in all their academic life"
    

## Getting Started

Bots are really popular (and sometimes necessary) in modern apps because they can be used to automatize processes, 
automatically handle data from storage systems (e.g databases), and provide specific services to the user of the app.
For instance, Nina's bot -- the one I created to manage my discord server --  helps me to provide useful information 
for students that otherwise, I would need to provide myself by email or in form of messages. Nina's bot saves me a 
lot of work.

In this milestone, students will be building their own Discord bot. Your bot must connect 
to your database system to solve some business problems related to the data stored in your database. 

The following are the high level steps that will be covered in this README file. 

1. Preparing Discord for your bot
2. Implementing your Bot in Python 
3. Hosting your Bot in Replit 

### Preparing Discord for your Bot 

Let's get started with the setting up of your Discord server. In this section you will prepare your discord to provide 
support for your Bot.

#### Discord Account

If you do not have a Discord account yet, create a new one [here](https://discord.com). If you already have a Discord account,
then ignore this step

#### Creating a Discord Server (Technically Know as Guild)

We'll use a Discord server as the user interface between out Bot and the user. 

1. Head to the discord [home](https://discord.com) page and sign in (if needed) using your Discord account
2. On the left hand panel, select select the + icon to add a new server 
3. It will prompt two options, select "Create Your Server", and provide the following name to your server 
"<your sfsu username>Server". For instance, my server would be named "jortizcoServer"
4. Create two new channels, ```#commands and #business-requirements```
5. In the ```#commands``` channel write the list of commands that the bot needs in order to solve each one of your business rules, and also add there some real examples about how to run those commands. (similar to what I did with my NinaBot in #bot-commands channel) 
6. In the ```#business-requirements``` channel write the list of bussiness requirements that your bot will solve. 

**Note that the lists of commands and business requirements must be approved by the class instructor by email**

#### Discord Application 

A Discord application allows you to interact with the Discord API. As many other APIs, 
you'll need to provide authentication and permissions. Applications in Discord are a high level abstraction to provide
communication between the Discord API and your Bot. 

1. In your [Discord Develpper Portal](https://discord.com/developers/applications), click on the "New Application" button
to create a new application. 
2. You'll be prompted to enter the name of the application, create the following name "CSC675M3" for your application, and
save the changes. 
3. Next, you'll be able to see all the information about your new application.  

#### Discord Bot 

Once an application has been successfully created, it is time to create your Bot user. The job of the Bot user is to 
react to certain events and command triggered by the user.  

1. Head to the left panel of your application in your [Developer Portal](https://discord.com/developers/applications)
and select the tab "Bot", and click on the "Add Bot" button found on the right panel of the bot tab. 
2. After the bot is successfully created, edit the name of your bot. Set the new name to "CSC675<your sfsu username>Bot"
where your SFSU username is the name before the @ in your SFSU email. For instance, if I were to create a bot, I would 
name it "CSC675jortizcoBot" (without quotes) because my SFSU email is jortizco@sfsu.edu. 
3. Click on reveal the Token link that is located below the username field of your bot, this token will be used later to provide authentication when the bot needs 
to access to the Discord API of your application. We'll use this token later when coding the Bot.  
4. Save all the changes 


#### Adding your Bot to your Server

Finally, we'll finish the set up of our application by registering our Bot to our server. Note that the Bots use the 
[QAuth2](https://oauth.net/2/), and we need to set up the Bot to use that protocol. 

1. Head again to your application [Developer Portal](https://discord.com/developers/applications) and click in your application. 
2. Head to the left hand panel of your application and select the QAuth2 tab. This tool will authorize the use of Discord APIs for your bot using your 
application's credentials 
3. On the right panel, set the authorization method to "In-app Authorization" and then in "scopes" check the "bot" checkbox. 
4. On the same panel, head to "Bot Permissions" and allow "administrator" permissions for your bot
5. Copy and paste the client id that can be found in "Client Information". 
6. Use the following link https://discordapp.com/oauth2/authorize?&client_id=YOUR_CLIENT_ID_HERE&scope=bot and replace YOUR_CLIENT_ID_HERE in the url with the client id from (5)


### Implementing your Bot in Python 

In this directory (milestone3), you'll find the following files: 

#### bot.py

The sample code provided in this file will help you to understand the basics of how the bot triggers
some events based on messages received by users (or the Discord system)

#### database.py 

In this file, you will implement the methods needed to handle all the connection and data manipulation that the bot needs to 
do in order to process requests from the Discord user. 

The connection method has been implemented for you already. However, you must set up first your secret environment 
variables to make it work. More details about this can be found in section "Host Bot in Replit" of this document

Finally, you will need to implement your own methods in order for your bot to solve the business rules approved by the
class' instructor. 

### Hosting your Bot in Replit 

For this milestone it is mandatory that students host their Bots in [Replit](htpps://replit.com). That way system 
incompatibilities during the grading process are minimized. In addition, a remote database must be created using your database model from milestone 2.

#### Hosting your Database Remotely

First of all, students must host their database model remotely (localhost is not allowed in this milestone). Students are 
free to choose the hosting server to host their databases. However, I totally recommend [Remote MySQL](https://remotemysql.com)
because it is free (without storage limitations) and very easy to use. [Remote MySQL](https://remotemysql.com) has also
a database management tool (PhpMyAdmin) where you can import in seconds your databasemodel.sql and inserts.sql scripts 
in order to create your database. 

Once your database has been created in [Remote MySQL](https://remotemysql.com), save the following information somewhere because you will need it later on: 

• The name of the database 
    
• Your db username 
    
• Your db password 

#### Create a Bot in Replit 

The next steps will guide you into creating your bot (manually or importing this repository) into [Replit](https://replit.com)

1. Create a new account in [Replit](https://replit.com) (if you don't have one already)
2. Login using your email and password from step (1)
3. Create a new Python repl app. Note that [Replit](https://replit.com) supports many other programming languages. In this milestone, you are free to create your
bot using your favorite programming language. There are two ways to create a new repl app (1) importing the code from this repository, and 
(2) creating the app manually. The new steps cover the (2) way.   
4. Give a name to your repl. The name of your repl must be your SFSU username followed by "bot". For example, my app would be "jortizcobot" because my SFSU username is "jortizco".
5. If everything goes as expected, your screen will show your new programming environment for your app. Take your time to familiarize yourself with this environment. 
6. Copy and paste the code from "bot.py" into the "main.py" file of your repl app. 
7. In your repl app, create a new file "database.py" and copy and paste there the code from the same file found in this repository

Now is time to set up all the secret environment variables in your repl app

#### Secret Environment Variables

Your repl app allows you to set up secret environment variables such as tokens, db usernames and passwords. We'll use this tool
to set all the environments variables related to our bot and the database

Head to the left hand panel of your application, and click in the lock icon. 
Once there, set the following secret environment variables and their values 

```.env
DISCORD_TOKEN= dicord token of your bot
DISCORD_GUILD= the name of your Discord server
DB_HOST=       the host url where your remote database is hosted. (localhost won't work here)
DB_USER=       db username 
DB_PASSWORD=   db password
DB_NAME =      database name 
```

The Discord token can be copied and pasted from your [Developer Portal](https://discord.com/developers/applications) 
in the Bot tab from your application. 

Note that you don't need to modify the code related to the secret environment variables in 
"main.py" and "database.py". It is already ready to be used because it is reading
from any value set in those keys. For example, ```host = os.environ['DB_HOST']``` will save the
database host in the ```host``` variable. 

Now, your bot is ready to be tested. 

#### Testing your Bot 

Before you start the development of your methods for the database part of this project is imperative that you test 
your bot with the code provided by the instructor to make sure that everything works as expected, and then you can focus
in the database part of this project. 

Let's test your Bot. Before running the Bot client, make sure that the bot has been added to your Discord Server. You 
should see your bot in the list of users, and the bot must be offline. Also, make sure that all the environment variables
in repl have the correct values.  

1. In your repl application, click in your "main.py" file, and click in the "Run" button located on the top. Your 
console will begin installing all the Discord and pymysql libraries needed to run your app. Then, if no errors found, your app automatically will be deployed. 
2. If your program throws errors, they are probably due to secret environment variables with
wrong values. Fix this, and re-run the program. 
3. If no errors found, you'll see in console a message saying that your bot is connected to 
your database, and joined your Discord server
4. Head to your Discord server and check that your bot is online. If your bot is still offline, 
then check the logs of your repl to see what went wrong. 
5. If your bot is online, congratulations! you created your first Discord Bot. 
6. Now is time to test your bot. Write the following message in any of the channels of your
Discord server: ```milestone3``` and click enter. Your bot should react with the following message 
```I am alive. Signed: 'your bot'```


Pretty cool right? you just created your first bot. Now you are all set. 

Your job is to implement all your business requirements.
Note that the commands to trigger your bot must also be approved by the class' instructor together with the 
business requirements that must be implemented here. 


### Useful Resources 

Here is a list of useful resources that you can use that will help you with the development of your bot for this milestone

* [How to create a Discord Bot with Java](https://medium.com/discord-bots/making-a-basic-discord-bot-with-java-834949008c2b)
* [How to create a Discord Bot with Javascript](https://www.freecodecamp.org/news/create-a-discord-bot-with-javascript-nodejs/)
* [Sample Repl App with the code from this repo](https://replit.com/join/aexibrqa-jortizco)


















 





