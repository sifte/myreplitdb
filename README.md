## MyReplitDB ![Generic badge](https://img.shields.io/badge/Python-3.8-blue.svg) ![Downloads](https://img.shields.io/pypi/dm/MyReplitDB)

A simple wrapper for replit's db.

## Example

```py
from myreplitdb import Database

db = Database()
db.insert('test', 'hello')
db.get('test') # hello
```
