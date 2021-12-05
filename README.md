## MyReplitDB

- MyReplitDB is the most simplistic and easiest wrapper to use for replit's database system.

## Example

```py
>>> import myreplitdb

>>> db = myreplitdb.Database()
>>> db.insert('test', 'hello!')
>>> db.get('test')

hello!
```