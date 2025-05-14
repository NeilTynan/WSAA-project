# WSAA-project
Repository for the Project of 24-25: 8640 -- WEB SERVICES AND APPLICATIONS

This README has been written with [GitHub's documentation on README's](https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/about-readmes) in mind.

## About this Project

Link to web application: 

This repository contains my weekly assignments for ATU module 8640 -- WEB SERVICES AND APPLICATIONS. It contains the project work for the course, which is focused on the construction of a REST API which will display information related to the old SFI grant comitments file. The intentions is this API will have a numer of features:

1. An accompanying web interface, using AJAX calls, to perform CRUD operations. 
2. Save the data into a database table that you view elsewhere in your application 
3. The ability to analyse the data in realtime.
4. Will be hosted online via PythonAnywhere.
5. Manipulate/analyse the data in real time.

Note on the grant table.

## Use of this Project

This repository may be of some interest to other students engaged in similar projects around web services and APIs. Feel free to use whatever you like from it (though if another party has been referenced, I would ask that you likewise cite them).

## Getting Started

The workbook is structured in a linear fashion, so reading through it from start to finish is the best approach.

To understand how the workbook has developped to date, please see below a timeline of the work done on the notebook and the material referenced in the course of this work:

- 31/03/2025 - Created ReadMe and Gitignore file. Gitignore file generated using the template at Python gitignore template at https://github.com/github/gitignore/blob/main/Python.gitignore, the Windows gitignore template at https://github.com/github/gitignore/blob/main/Global/Windows.gitignore, the MacOS gitignore template at https://github.com/github/gitignore/blob/main/Global/macOS.gitignore and the Linux gitignore template at https://github.com/github/gitignore/blob/main/Global/Linux.gitignore.
- 03/04/2025 - Set up flask server. Course material referenced: WSAA6.5 REST for project
- 07/04/2025 - Added CRUD operators for flask server. Course material referenced: WSAA6.5 REST for project
- 08/04/2025 - Added in "grantsviewer.html" file to serve as the basis of the main webpage. Internal materials referenced: WSAA09.05 look at sample
- 25/04/2025 - Added a "requirements.txt" file. Start work on hosting the web application on pythonanywhere.
- 27/04/2025 - Continued work on trying to set up hosting for the web application.
- 08/05/2025 - Continued work on hosting but ultimately decided to wait until the web application was fully designed before proceeding any further.
- 10/05/2025 - Focused on the development of an interface, based off a single table ("grants") which heavily mirrored the Books inferface in the coursework. This was then integrated in the existing structure of "1table.html". Achieving this involved:
    + Reverting a lot of the previous work done on "1table.html" and "rest.py", as it was becoming apparrent that these were increasingly less assisted by ChatGpt and were, in fact, become designed by ChatGpt. 
    + Consequently, the api and web application were redisigned more in line with course materials. This involved adding in "grantDAO.py", "dbconfigpy" and updated "rest.py" (now renamed "rest-server.py"). Internal materials referenced: Lab 6.01 DR6.2.3 JavaScript part2, DR6.2.4 JavaScript Part3, WSAA07.01 Data layer, WSAA07.02 databases, Lab 7.2, Lab 9.1, Lab 9.2, Lab 9.4 and GitHub code folders Topic06-implemtation, Topic06-servers, Topic07-data-layer and Topic09-html-ajax.
    + Much of the html in "1table.html" was also adjusted to be more in line with the Book interface, with this being adjusted to accomodate the focus on grants. 
- 11/05/2025 - Work continued on the new interface design. Today's tasks included:
    + Finished setting up the sql database (wssa) that "dbconfig.py" interacts with. 
    + Started work on integrating a second database ("researcher") into the files added on 10/05. 
    + Additional columns were added into the table (programme, institution and then year) as the scale of the updated project was finalised. "grantDAO.py", "rest-server.py" and "1table.html" were updated accordingly.
- 12/05/2025 - Continued work on the new interface design. Today's tasks included:
    + Added in "sfi.py" and "opendata.csv". The former to facilitate the populating the sql table with the data in the later.
    + Completed work on adding in the second ("researcher") table.
    + Started work on comparator function to allow for data from "researcher" to be matched against averages drawn from "grant".
    + Deleted "2.html" and "3.html" as it became apparent that their functions could be embedded into the primary html file without much loss of useability.
- 13/05/2025 - Completed much of the work on the interface. Tasks involved in this included:
    + Finalised work on the comparator function, which was adjusted to do most of the comparison work at the sql level as opposed to using CRUD calls to do the comparison.
    + Updated the html to improve formating of the actual web page, removing now redundent elements such as the nav section. Added in a text section explain how the interface works and how to use it.
    + With the move towards drawing much of the comparator data directly from the sql database it became apparent that the first table ("grants") was now largerly redundent in the final design. Consequently, most references to it were removed from the html, DAO and rest-server files. 
- 14/05/2025 - 

## Getting help

Queries about this repository can be directed directly to my GitHub account (NeilTynan).

## Other References



## Author

I am student Atlantic Technological University's Higher Diploma in Data Science.
