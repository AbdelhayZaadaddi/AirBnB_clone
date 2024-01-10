#!/usr/bin/python3

import cmd
from models.base_model import BaseModel
from models.user import User
from models import storage

class HBNBCommand(cmd.Cmd):

    prompt = "(hbnb) "

    def do_quit(self, arg):
        '''Quit command to exit the program'''
        return True
    
    def do_EOF(self, arg):
        '''EOF command to exit the program'''
        print()
        return True
    
    def emptyline(self):
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
        if not arg:
            print("** class name missing **")
            return
        
        try:
            class_name, instance_id = arg.split()
            obj_key = "{}.{}".format(class_name, instance_id)
            obj = storage.all().get(obj_key)
            if not obj:
                print("** no instance found **")
                return
            print(obj)
        except ValueError:
            print("** instance id missing **")
        except NameError:
            print("** class doesn't exist **")

    def do_destroy(self, arg):
        '''Deletes an instance based on the class name and id.'''
        if not arg:
            print("** class name missing **")
            return
        
        try:
            class_name, instance_id = arg.split()
            obj_key = "{}.{}".format(class_name, instance_id)
            obj = storage.all().get(obj_key)
            if not obj:
                print("** no instance found **")
                return
            del storage.all()[obj_key]
            storage.save()
        except ValueError:
            print("** instance id missing **")
        except NameError:
            print("** class doesn't exist **")

    def do_all(self, arg):
        '''Prints all string representation of all instances.'''
        if arg:
            try:
                obj_list = [str(obj) for obj in storage.all().values() if obj.__class__.__name__ == arg]
                if not obj_list:
                    print("** class doesn't exist **")
                    return
                print(obj_list)
                return
            except NameError:
                pass
            print("** class doesn't exist **")
            return
        
        obj_list = [str(obj) for obj in storage.all().values()]  # fix the typo here
        print(obj_list)



    def do_update(self, arg):
        '''Updates an instance based on the class name and id.'''
        args = arg.split()
        if len(args) < 1:
            print("** class name missing **")
        elif args[0] not in globals():
            print("** class doesn't exist **")
        elif len(args) < 2:
            print(" instance id missing **")
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
                if args[2] in ("id", "craeted_at", "updated_at"):
                    print("can't update **")
                    return
                obj = storage.all()[key]
                setattr(obj, args[2], args[3])
                storage.save()

    def default(self, arg):
        '''
        Handel dynamic commands
        using <class name>.<method name>(<args>)
        '''
        try:
            names, args = arg.strip(')').split('(')
            class_name, method_name = names.split('.')

        except Exception:
            return

if __name__ == '__main__':
    HBNBCommand().cmdloop()