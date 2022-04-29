from replit import db
from .exceptions import InvalidType

class Database:
    def __init__(self):
        self.db = db

    def insert(self, name: str, value: str):
        if not isinstance(name, str):
            raise InvalidType(
                f'Expected name to be str, got {type(name).__name__}'
            )

        if not isinstance(value, str):
            raise InvalidType(
                f'Expected value to be str, got {type(value).__name__}'
            )
            
        data = self.db[name] = value
        return data

    def set(self, name: str, value: str):
        return self.insert(name, value)

    def update(self, name: str, value: str):
        key = self.db.get(name, None)

        if key is None:
            raise KeyError(
                f"The key '{name}' was not found"
            )
        
        data = self.db[name] = value
        return data

    def get(self, name: str):
        try:
            data = self.db[name]
            return data
        except:
            raise KeyError(
                f"The key '{name}' was not found"
            )

    def delete(self, name: str):
        try:
            del self.db[name]
        except KeyError:
            raise KeyError(
                f"The key '{name}' was not found"
            )

    def keys(self, return_obj = list):
        try:        
            return return_obj(self.db.keys())
        except Exception as error:
            raise error

    def values(self, return_obj = list):
        try:        
            return return_obj(self.db.values())
        except Exception as error:
            raise error
