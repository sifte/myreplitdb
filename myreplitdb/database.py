from replit import db
from .errors import KeyNotFound, InvalidType

class Database:
    def __init__(self):
        self.db = db

    def insert(self, name: str, value: str):
        if not isinstance(name, str):
            raise InvalidType(
                f'Excepted name to be str, got {type(name).__name__}'
            )

        if not isinstance(value, str):
            raise InvalidType(
                f'Excepted value to be str, got {type(value).__name__}'
            )
            
        data = self.db[name] = value
        return data

    def get(self, key: str):
        try:
            data = self.db[key]
            return data
        except:
            raise KeyNotFound(
                f'The key \'{key}\' was not found'
            )

    def delete(self, key: str):
        try:
            del self.db[key]
        except KeyError:
            raise KeyNotFound(
                f'The key \'{key}\' was not found'
            )

    def keys(self):
        return self.db.keys()