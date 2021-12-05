## MyReplitDB

- MyReplitDB is the most simplistic and easiest wrapper to use for replit's database system.

## Example

```py
>>> import mydb

>>> db = mydb.Database()
>>> db.insert('test', 'hello!')
>>> db.get('test')

hello!
```