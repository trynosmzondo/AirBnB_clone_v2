#!/usr/bin/python3
"""Defines HBNB console"""
import cmd
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review

classes = {
    "BaseModel", "User",
    "State", "City",
    "Place", "Amenity",
    "Review"
}

class HBNBCommand(cmd.Cmd):
    """Defines Holberton BNB command line interpreter
    
    Attributes:
        prompt (str): The command prompt,
    """

    prompt = "(hbnb) "

    def emptyline(self):
        """an empty line + ENTER does not execute anything"""
        pass

    def do_create(self, arg):
        """ Usage: create <class>
        creates a new class instance and prints it's id
        """
        if not arg:
            print("** class name missing **")
            return
        arg_dict = arg.split()
        if arg_dict[0] not in classes:
            print("** class doesn't exist **")
            return
        print(eval(arg_dict[0])().id)
        storage.save()

    def do_show(self, arg):
        """Usage: show <class> <id> or <class>.show(<id>)
        prints string representaion of an object
        """
        obj_dict = storage.all()
        if not arg:
            print("** class name missing **")
            return
        else:
            arg_list = arg.split()
        if arg_list[0] not in classes:
            print("** class doesn't exist **")
        elif len(arg_list) < 2:
            print("** instance id missing **")
        elif "{}.{}".format(arg_list[0], arg_list[1]) not in obj_dict.keys():
            print("** no instance found **")
        else:
            print(obj_dict["{}.{}".format(arg_list[0], arg_list[1])])

    def do_destroy(self, arg):
        """Usage: destroy <class> <id> or <class>.destroy(<id>)
        Delete a class instance using it's id.
        """
        obj_dict = storage.all()
        if not arg:
            print("** class name missing **")
            return
        else:
            arg_list = arg.split()
        if arg_list[0] not in classes:
            print("** class doesn't exist **")
        elif len(arg_list) < 2:
            print("** instance id missing **")
        elif "{}.{}".format(arg_list[0], arg_list[1]) not in obj_dict.keys():
            print("** no instance found **")
        else:
            del obj_dict["{}.{}".format(arg_list[0], arg_list[1])]
            storage.save()

    def do_all(self, arg):
        """Usage: all or all <class> or <class>.all()
        Display string representations of all instances of a given class.
        If no class is specified, displays all instantiated objects.
        """
        obj_dict = storage.all().values()
        arg_list = arg.split()
        if len(arg) > 0 and arg_list[0] not in classes:
            print("** class doesn't exist **")
        else:
            objl = []
            for obj in obj_dict:
                if len(arg_list) > 0 and arg_list[0] == obj.__class__.__name__:
                    objl.append(obj.__str__())
                elif len(arg_list) == 0:
                    objl.append(obj.__str__())
            print(objl)

    def do_update(self, arg):
        """Usage: update <class> <id> <attribute_name> <attribute_value> or
        <class>.update(<id>, <attribute_name>, <attribute_value>)
        Update a class instance of a given id by adding or updating
        a given attribute
        """
        obj_dict = storage.all()
        if not arg:
            print("** class name missing **")
            return
        else:
            arg_list = arg.split()
        if arg_list[0] not in classes:
            print("** class doesn't exist **")
        elif len(arg_list) < 2:
            print("** instance id missing **")
        elif "{}.{}".format(arg_list[0], arg_list[1]) not in obj_dict.keys():
            print("** no instance found **")
        elif len(arg_list) < 3:
            print("** attribute name missing **")
        elif len(arg_list) < 4:
            print("** value missing **")
        else:
            obj = obj_dict["{}.{}".format(arg_list[0], arg_list[1])]
            if arg_list[2] in obj.__class__.__dict__.keys():
                var_type = type(obj.__class__.__dict__[arg_list[2]])
                obj.__dict__[arg_list[2]] = var_type(arg_list[3])
            else:
                obj.__dict__[arg_list[2]] = arg_list[3]
        storage.save()

    def do_quit(self, arg):
        """quit command to exit the program."""
        return True

    def do_EOF(self, arg):
        """EOF signal to exit the program."""
        print("")
        return True
if __name__ == '__main__':
    HBNBCommand().cmdloop()
