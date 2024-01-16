
<h1 align="center">AirBnB clone - The console </h1>

## Description of the project

The console:

- create your data model
- manage (create, update, destroy, etc) objects via a console / command interpreter
- store and persist objects to a file (JSON file)

The first piece is to manipulate a powerful storage system. This storage engine will give us an abstraction between “My object” and “How they are stored and persisted”. This means: from your console code (the command interpreter itself) and from the front-end and RestAPI you will build later, you won’t have to pay attention (take care) of how your objects are stored.

This abstraction will also allow you to change the type of storage easily without updating all of your codebase.

The console will be a tool to validate this storage engine

![Hbnb](https://i.ibb.co/RSzZ5yh/815046647d23428a14ca.png)

### Requirements 

#### Python Scripts
- Allowed editors: vi, vim, emacs
- All your files will be interpreted/compiled on Ubuntu 20.04 LTS using python3 (version 3.8.5)
- All your files should end with a new line
- The first line of all your files should be exactly #!/usr/bin/python3
- A README.md file, at the root of the folder of the project, is mandatory
- Your code should use the pycodestyle (version 2.8.*)
- All your files must be executable
- The length of your files will be tested using wc
- All your modules should have a documentation ```(python3 -c 'print(__import__("my_module").__doc__)')```
- All your classes should have a documentation ```(python3 -c 'print(__import__("my_module").MyClass.__doc__)')```
- All your functions (inside and outside a class) should have a documentation ```(python3 -c 'print(__import__("my_module").my_function.__doc__)'``` and ```python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)')```
- A documentation is not a simple word, it’s a real sentence explaining what’s the purpose of the module, class or method (the length of it will be verified)

#### Python Unit Tests
- Allowed editors: vi, vim, emacs
- All your files should end with a new line
- All your test files should be inside a folder tests
- You have to use the unittest module
- All your test files should be python files (extension: .py)
- All your test files and folders should start by test_
- Your file organization in the tests folder should be the same as your project
e.g., For models/base_model.py, unit tests must be in: tests/test_models/test_base_model.py
e.g., For models/user.py, unit tests must be in: tests/test_models/test_user.py
- All your tests should be executed by using this command: ```python3 -m unittest discover tests```
You can also test file by file by using this command: ```python3 -m unittest tests/test_models/test_base_model.py```
- All your modules should have a documentation ```(python3 -c 'print(__import__("my_module").__doc__)')```
- All your classes should have a documentation ```(python3 -c 'print(__import__("my_module").MyClass.__doc__)')```
- All your functions (inside and outside a class) should have a documentation ```(python3 -c 'print(__import__("my_module").my_function.__doc__)'``` and ```python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)')```
  
We strongly encourage you to work together on test cases, so that you don’t miss any edge case


## Description of command interpreter
It’s exactly the same as simple shell but limited to a specific use-case. In our case, we want to be able to manage the objects of our project:

- Create a new object (ex: a new User or a new Place)
- Retrieve an object from a file, a database etc…
- Do operations on objects (count, compute stats, etc…)
- Update attributes of an object
- Destroy an object


## How to start, use and examples

### - Run the following command to start it:

```python
$ ./console.py
```
### - Usage and Examples:

Available Commands:
| Command | Explanation | Example |
| ------- | ----------- | ------- |
| create | Create anew instance of ```BaseModel```, saves it to JSON file and prints the ```id```. | ```create BaseModel``` |
| show | prints the string representation of an instance based on the class name and ```id```.| show BaseModel ```1234-5678-9101``` |
| all | prints all string representations of all instances based or not on the class name. | ```all BaseModel``` |
| update | updates and instance based on the class name and ```id``` by adding or updating an attribute (saves the change to JSON file). | ```update BaseModel 1234-5678-9101 email "someone@gmail.com"```|

Command input:
| Command | Example |
| ------- | ------- |
| create | create [class name] |
| show | show [class name] [id] |
| all | all [class name] [id] |
| update | update [class name] [id] [arg_name] [arg_value] |

Daynamic Commands:
| Command | Example |
| ------- | ------- |
| [class name].all() | User.all() |
| [class name].count() | User.count() |
| [class name].show(id) | User.show("1234-1536-7358") |
| [class name].destroy(id) | User.destroy("1234-1536-7358") |
| [class name].update(id, attribute name, value) | User.update("1234-1536-7358", "first_name", "Huda") |
| [class name].update(id, dictionary) | User.update("1234-1536-7358", {'first_name': "Huda", 'age':20}) |

 Available Classes:

Every model inhertis attributes from BaseModel:

- Attributes
- BaseModel
- User
- City
- Amenity
- Place
- Review


### - Modes:

Interactive mode:
```
$ ./console.py
(hbnb) help
Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb)
(hbnb)
(hbnb) quit
$
```
Non-interactive mode:
```
$ echo "help" | ./console.py
(hbnb)
Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb) 
$
$ cat test_help
help
$
$ cat test_help | ./console.py
(hbnb)
Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb)
$
```

