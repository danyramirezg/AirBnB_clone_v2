# :triangular_flag_on_post: Holberton B&B

<img align="center" src="https://i.ibb.co/d5N85Nh/hbnb.png" width="100%">

### Welcome to the AirBnB clone project! (Holberton B&B)

First step: write a command interpreter to manage your AirBnB objects. This is the first step towards building your first full web application: the AirBnB clone. This first step is very important because you will use what you build during this project with all other following projects: HTML/CSS templating, database storage, API, front-end integration.

### Whats a command interpreter?

Do you remember the Shell? Its exactly the same but limited to a specific use-case. In our case, we want to be able to manage the objects of our project:

- Create a new object (ex: a new User or a new Place)
- Retrieve an object from a file, a database etc
- Do operations on objects (count, compute stats, etc)
- Update attributes of an object
- Destroy an object

### HBNBCommand

This is the console (command interpreter) for the Holberton Airbnb clone project. The console can be used to store objects in and retrieve objects from a JSON.

Supported classes:
- BaseModel
- User
- State
- City
- Amenity
- Place
- Review

<img align="center" src="https://i.ibb.co/g6XHQFf/Diagrama.jpg" width="100%">

### Commands

These are some of the commands implemented in our console (HBNBCommand):

| Command | Description |
| ------ | ------ |
| all | Prints all string representation of all instances based or not on the class name |
| create | Creates a new instance of class name, saves it (to the JSON file) and prints the id |
| destroy | Deletes an instance based on the class name and id (save the change into the JSON file) |
| help | List available commands with "help" or detailed help with "help cmd" |
| quit - EOF | Commands to exit the program |
| show | Prints the string representation of an instance based on the class name and id |
| update | Updates an instance based on the class name and id by adding or updating attribute (save the change into the JSON file) |

To start, navigate to the project folder and enter `./console.py` in the shell.

#### Create
`create <class name>`
Ex:
`create BaseModel`

#### Show
`show <class name> <object id>`
Ex:
`show User my_id`

#### Destroy
`destroy <class name> <object id>`
Ex:
`destroy Place my_place_id`

#### All
`all` or `all <class name>`
Ex:
`all` or `all State`

#### Quit
`quit` or `EOF`

#### Help
`help` or `help <command>`
Ex:
`help` or `help quit`

Additionally, the console supports `<class name>.<command>(<parameters>)` syntax. Ex: `City.show(my_city_id)`

<img align="center" src="https://i.ibb.co/L5wPt65/Consola.jpg" width="60%">

### Environment variables

- HBNB_ENV: running environment. It can be dev or test for the moment (production soon!)
- HBNB_MYSQL_USER: the username of your MySQL
- HBNB_MYSQL_PWD: the password of your MySQL
- HBNB_MYSQL_HOST: the hostname of your MySQL
- HBNB_MYSQL_DB: the database name of your MySQL
- HBNB_TYPE_STORAGE: the type of storage used. It can be file (using FileStorage) or db (using DBStorage)


