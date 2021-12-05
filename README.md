## MyReplitDB

- MyReplitDB is the most simplistic and easiest wrapper to use for replit's database system.

## Installing

- You can install it from the [PyPI](https://pypi.org/project/MyReplitDB/1.2/)
- Or you can install it from the [Github](https://github.com/kaylebetter/myreplitdb) directly.

## Example

```py
>>> import myreplitdb

>>> db = myreplitdb.Database()
>>> db.insert('test', 'hello!')
>>> db.get('test')

hello!
```