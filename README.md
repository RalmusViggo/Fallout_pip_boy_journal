# Pip Boy Journal
dette prosjektet går ut på at jeg lager en oversikt over en del informasjon fra *Fallout* spillene. Den har info om skapninger, forskjellige grupper, og annet fra spillene. den er skrevet fra perspektivet til en som reiser rundt og dokumenterer disse tingene.

## kompetansemål
* planlegge og dokumentere arbeidsprosesser og IT-løsninger
* designe og implementere IT-tjenester med innebygget personvern
* modellere og opprette databaser for informasjonsflyt i systemer
* kartlegge behovet for og utvikle veiledninger for brukere og kunder
* feilsøke og rette feil ved hjelp av feilsøkingsstrategier og relevante rammeverk
* administrere brukere, tilganger og rettigheter i relevante systemer


## installerte moduler og sånn

- pip install flask
- pip install mysql-connector-python
- pip install flask-wtf
* pass på at disse er installert i et virtuelt miljø

## install guide

download the files from the github repositort you're currently in, and make sure they are somewhere they can actually run, i haven't tested this on any other type of system besides an ubuntu/apache server.

### **Create a new virtual environment**

1. Create an empty folder for the project with its own name, **example_folder**
2. Open the folder in VSCode 
3. Open the terminal and navigate to the empty folder by cd, to **example_folder**
4. We will now create the env folder so we can run a virtual environment here. Create the folder by running the command in the terminal (while you are in your project folder)

```
python3 -m venv **env**
```

Check that you have a new folder “env”:

```
ls 

#A folder **env** should appear
```

## Activate the virtual environment

This should be done **every time you are going to work on a project where you are using a virtual working environment**

Be in the working folder of your project and run the command below:

```
source **env**/bin/activate
```

If you now get *(env)* before the normal line in the terminal, you have done it correctly so far! You are now in a virtual environment, where your folder **example_folder** is the virtual environment.

Every time you close the terminal, the environment will be deactivated automatically. You must therefore activate the environment every time you are going to start your project again after closing the terminal.

If you want to deactivate the environment to use the terminal for something else, you can deactivate the environment by running the command below in the folder: 

```
deactivate 
```

## **Installing packages in the environment**

This is done every time you are going to create a **new** project where you are going to use Flask, **after** you have created a virtual environment as described above. 

The point of a virtual environment is that you can work with it isolated from the rest of the machine. It is nice when we are going to install packages that we only need for this project, so that we do not have to install packages on the entire machine. To install packages that we need for Flask, we use pip commands. PIP = preferred installer program. (PIP installs packages)

1. To see the packages we have in the environment we are in so far, we can write:

```
pip list
```

Not many packages installed yet. Only the package “pip”.


Then install the packages for flask: 

```
pip3 install flask
```

```
pip3 install flask_wtf
```

```
pip3 install mysql-connector-python
```

Setup to be able to use Flask on Apache:

**IMPORTANT**
in app.py, change the things in the function "def get_conn():" with the things of *your* mysql database.
also use this query to add the collums that the website uses: "CREATE TABLE {{table name}}(user_id INT AUTO_INCREMENT PRIMARY KEY, username VARCHAR(255), password VARCHAR(255), origin VARCHAR(255), origin_trait VARCHAR(255), strength INT, perception INT, endurance INT, charisma INT, intelligence INT, agility INT, luck INT, tagskill1 VARCHAR(255), tagskill2 VARCHAR(255), tagskill3 VARCHAR(255), athletics INT, barter INT, big_guns INT, energy_weapons INT, explosives INT, lockpick INT, medicine INT, melee_weapons INT, pilot INT, repair INT, science INT, small_guns INT, sneak INT, speech INT, survival INT, throwing INT, unarmed INT, level INT);"
[https://www.notion.so/Setup-for-using-Flask-on-Apache-ef15724844df836cac048197d8afb416?source=copy_link](https://www.notion.so/Setup-for-using-Flask-on-Apache-ef15724844df836cac048197d8afb416?source=copy_link)