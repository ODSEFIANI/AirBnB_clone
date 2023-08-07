"""
base_model class
"""


from datetime import datetime
import uuid


class BaseModel():
    """
    BaseModel class implementation
    """

    def __init__(self):
        """
        initializes an instance
        """
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def __str__(self):
        """
        prints info about an instance
        """
        a = self.__class__.__name__
        b = self.id
        c = self.__dict__
        return "[{}] ({}) <{}>".format(a, b, c)

    def save(self):
        """
        updates the public instance attribute updated_at
        with the current datetime
        """
        self.updated_at = datetime.now()

    def to_dict(self):
        """
        returns a dictionary
        containing all keys/values of __dict__ of the instance
        """
        d = self.__dict__
        d["__class__"] = self.__class__.__name__
        d["created_at"] = self.created_at.isoformat()
        d["updated_at"] = self.updated_at.isoformat()
        return d
