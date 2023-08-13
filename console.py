#!/usr/bin/python3
"""
py shell
"""
import cmd
import re
from models.base_model import BaseModel
from models import storage


class HBNBCommand(cmd.Cmd):
    """ Cmd class."""


    prompt = "(hbnb) "
    cls = {"BaseModel", "User", "Place", "City", "Amenity", "Review", "State"}

    def do_quit(self, arg):
        """Command quit to exit the program."""
        return True

    def do_EOF(self, arg):
        """EOF to exit the program."""
        print()
        return True
        
    def emptyline(self):
        """ Empty line and do nothing."""
        pass

    def do_show(self, arg):
        """Pstring."""
        ar = arg.split()
        if not ar:
            print("** class name missing **")
        else:
            c_name = ar[0]
            if len(ar) == 0:
                print("** class name missing **")
            elif c_name not in HBNBCommand.cls:
                print("** class doesn't exist **")
            elif len(ar) < 2:
                print("** instance id missing **")
            else:
                obj_key = "{}.{}".format(c_name, ar[1])
                all_objs = storage.all()
                if obj_key in all_objs:
                    print(all_objs[obj_key])
                else:
                    print("** no instance found **")
                    
     def do_create(self, arg):
        """ fresh basemodel."""
        if not arg:
            print("** class name missing **")
        else:
            try:
                new_inst = eval(arg)()
                new_inst.save()
                print(new_inst.id)
            except NameError:
                print("** class doesn't exist **")                   


if __name__ == "__main__":
    HBNBCommand().cmdloop()
