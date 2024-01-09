#!/usr/bin/python3

import cmd
from models.base_model import BaseModel
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
        if not arg:
            print("** class name missing **")
            return
        
        try:
            class_name, instance_id = arg.split()
            obj_key = "{}.{}".format(class_name, instance_id)
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
        
        obj_list = [str(obj) for obj in storage.all().value()]
        print(obj_list)


    def do_update(self, arg):
        pass

if __name__ == '__main__':
    HBNBCommand().cmdloop()