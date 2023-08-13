#!/usr/bin/python3
"""
py shell
"""
import cmd


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


if __name__ == "__main__":
    HBNBCommand().cmdloop()
