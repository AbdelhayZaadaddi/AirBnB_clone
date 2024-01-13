#!/usr/bin/python3
"""The console handle all commands for Hbnb"""

import cmd
import models
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.place import Place
from models.amenity import Amenity
from models.city import City
from models.review import Review
from models import storage


class HBNBCommand(cmd.Cmd):

    """HBNBCommand class, uses cmd module to make a CI"""

    prompt = "(hbnb) "

    def do_quit(self, arg):
        '''Quit command to exit the program'''
        return True

    def do_EOF(self, arg):
        '''EOF command to exit the program'''
        print()
        return True

    def emptyline(self):
        '''Pass empty line or on enter'''
        pass

    def do_create(self, arg):
        '''Creates a new instance of BaseModel, saves it, and prints the id'''
        if not arg:
            print("** class name missing **")
            return

        try:
            new_instance = eval(arg)()
            new_instance.save()
            print(new_instance.id)
        except NameError:
            print("** class doesn't exist **")

    def do_show(self, arg):
        '''Prints the string representation of an instance.'''
        if len(arg) == 0:
            print("** class name missing **")
        else:
            parts = arg.split()
            if parts[0] not in globals():
                print("** class doesn't exist **")
            elif len(parts) < 2:
                print("** instance id missing **")
            else:
                class_name = parts[0]
                obj_id = parts[1]
                key = f"{class_name}.{obj_id}"
                if key in storage.all():
                    print(storage.all()[key])
                else:
                    print("** no instance found **")

    def do_destroy(self, arg):
        '''
        Deletes an instance based on the class name and id
        using : destroy <class name> <id>
        '''
        if len(arg) == 0:
            print("** class name missing **")
        else:
            parts = arg.split()
            if parts[0] not in globals():
                print("** class doesn't exist **")
            elif len(parts) < 2:
                print("** instance id missing **")
            else:
                class_name = parts[0]
                obj_id = parts[1]
                key = f"{class_name}.{obj_id}"
                if key in storage.all():
                    del storage.all()[key]
                    storage.save()
                else:
                    print("** no instance found **")

    def do_all(self, arg):
        '''
        all Prints all string representation of all instances
        based or not on the class name and id
        using : all or all <class name> <id>
        '''
        # all User
        parts = arg.split()
        if len(parts) < 1:
            print(storage.all())
        else:
            if parts[0] not in globals():
                print("** class doesn't exist **")
            else:
                for key in storage.all():
                    if parts[0] == key.split('.')[0]:
                        print(storage.all()[key])

    def do_update(self, arg):
        '''Updates an instance based on the class name and id.'''
        args = arg.split()
        if len(args) < 1:
            print("** class name missing **")
        elif args[0] not in globals():
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        elif f"{args[0]}.{args[1]}" not in storage.all():
            print("** no instance found **")
        elif len(args) < 3:
            print("** attribute name missing **")
        elif len(args) < 4:
            print("** value missing **")
        else:
            key = "{}.{}".format(args[0], args[1])
            if key not in storage.all():
                print("** no instance found **")
            else:
                if args[2] in ("id", "created_at", "updated_at"):
                    print("** can't update **")
                    return
                obj = storage.all()[key]
                setattr(obj, args[2], args[3])
                storage.save()

    def default(self, arg):
        '''
        handle dynamic commands
        using : <class name>.<method name>(<args>)
        '''
        try:
            names, args = arg.strip(')').split('(')
            class_name, method_name = names.split('.')
            if (method_name == "count"):
                print(self.counter(class_name))
            else:
                fun = f"do_{method_name}"
                method_name = getattr(self, fun, None)
                if len(args) == 0:
                    method_name(class_name)
                else:
                    if fun == "do_update":
                        args = args.split(",", 1)
                        key = f"{class_name}.{eval(args[0].strip())}"
                        if "{" in args[1]:
                            data_obj = eval(args[1])
                            if key in storage.all():
                                obj = storage.all()[key]
                            else:
                                print(f"No key found : {key}")
                            for key, value in data_obj.items():
                                setattr(obj, key, value)
                                storage.save()
                        else:
                            args = args[1].replace('"', "").split(",")
                            c = class_name
                            k = key.split('.')[1]
                            a1 = args[0].strip()
                            a2 = args[1].strip()

                            method_name(f"{c} {k} {a1} {a2}")
                            storage.save()
                    else:
                        args = args.replace('"', "")
                        args = args.replace(" ", "")
                        args = args.replace(",", " ")
                        args = f"{class_name} {args}"
                        method_name(args)
        except Exception:
            return

    def counter(self, arg):
        '''count how many obj we have'''
        count = 0
        for value in storage.all():
            class_name = value.split(".")[0]
            if class_name == arg:
                count += 1
        return count


if __name__ == '__main__':
    HBNBCommand().cmdloop()
