********** Intro **********

Hive is a django-based webtool designed to help researchers collaborate and find suitable grants for their research. The search tool has two modes: basic keywork search and LSI-powered conceptual search. 

********** Dev Notes **********

This section is intended primarily for any future devs working on the project, to help you get an understanding of the project and how to work on it. Below is a list of important topics you might find useful. 

	1. Virtualenv
		HIVE was developed in python 3.6, and all python packages are encapsulated in a virtual environment. I did this to reduce technical debt and make it easier to maintain the project in the future. If you need to add new libraries to the program, I'd HIGHLY recommend installing them in the virtual environment so that you won't have to worry about updating a package and breaking compatability with another program running on the server.
		To access the various python libraries the program uses, you will first need to activate the venv (cd into the main HIVE folder and enter "source venv/bin/activate". you'll know the venv is activated if you see "(venv)" appear in front of your prompts on the command line. 
	
	2. Database
		The database is currently a work in progress, hopefully I'll have time to come back and update this section later as the backend evolves.
		The database structure was initally much more streamlined, but the structure of the db had to change to accomodate LSI files for the conceptual search. Much of what you see in the database is not how I would have designed it, but the pre-computed LSI files had to dictate the structure unfortunately. I've done everything I can to keep it as clean as possible.  
		See the models.py file (mentioned below) to get a good idea of the db structure.
		
	3. File Structure
		This section will give a brief overview of the file structure of the project.
		+HIVE: The main project directory
		
			+HIVE: This dir is for app-wide settings, you may need to adjust some settings here in the settings.py and wsgi.py files if porting to a different machine, for example.
			
			+searchFunction: The meat of the application is in the directory.
				Perhaps the most important file here is models.py. In django, the models file is what creates the structure of the databases. If you want a good overview of what the database looks like, this file is a good place to start.
				
				+Templates: This is where the html files are. I've used django's "blocks" feature to keep everything as modular as possible. What this means is that the index.html is the core of the site, and most of the other files are "plugged in" to the main page as needed instead of going to a separate page entirely. This way you can add or modify the site without risk of breaking the main page, and you'll never have to copy the base functionality of the index page to any of the sub-pages.
				
				+static: serves static files like pictures.
				
				
			
			

