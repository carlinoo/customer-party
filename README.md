# Customer Party

### Introduction
I was asked to create a program to read a JSON file with information about customers. Each customer has a latitude and longitude. I was also given the position of the Dublin Office. I have to read the JSON file, filter out the customers whose location is greater than 100km from the Office in Dublin, and output them like shown below. All the automated test cases are in the /test folder. When running the program, the output is the following:

``` text
  user_id: 4, name: Ian Kehoe
  user_id: 5, name: Nora Dempsey
  user_id: 6, name: Theresa Enright
  user_id: 8, name: Eoin Ahearn
  user_id: 11, name: Richard Finnegan
  user_id: 12, name: Christina McArdle
  user_id: 13, name: Olive Ahearn
  user_id: 15, name: Michael Ahearn
  user_id: 17, name: Patricia Cahill
  user_id: 23, name: Eoin Gallagher
  user_id: 24, name: Rose Enright
  user_id: 26, name: Stephen McArdle
  user_id: 29, name: Oliver Ahearn
  user_id: 30, name: Nick Enright
  user_id: 31, name: Alan Behan
  user_id: 39, name: Lisa Ahearn

```

### Most Interesting Piece of Software Built by me
The most Interesting piece of Software I have built is **Vinum**. Vinum is an open source Model View Controller (MVC), Object-Relational Mapping (ORM) framework for PHP. Although it is not completely finished, it is built to create and deploy web-applications very fast, keeping track of Database Migrations, and making calls to Database much simpler.

To make Vinum a rapid development framework, I use Convention over Configuration. This means that if you follow the Vinum Convention, you won't have to tweak anything to make it work, it just works.

Also, Vinum has a Command Line Interface. This makes it very simple for the developer to create Models, Resources, Migrations and even migrate the database. Migrating the database it is very useful if you are working with other developers, as you can keep track of all the changes you have made to the database, so you are not only making changes to your database, but everyone else's.

As I said, the framework needs a bit more work, but it is nearly finished. I believe it is amazing!
