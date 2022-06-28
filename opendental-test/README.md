### Bugfixes:
`data` inside the controller `users.py` has to have data inside this method and then apply this as a parameter to the model `user.py` for the model to correctly get the data from the query inside the sql schema.

# Inside the controller `users.py`
``` python
@app.route('/')
def index():
  data = {
    'id' : 1,
  }
  return render_template('index.html', patient=User.get_one(data), patients=User.get_all)
```
These methods are for passing variables and getting data from the templates to the queries located inside the models.

# Inside the model `user.py`
``` python
@classmethod
  def get_one(cls,data):
    query = """
    SELECT * FROM user 
    WHERE id = %(id)s;"""
    results = connectToMySQL(cls.db).query_db(query,data)
    return cls(results[0])
```
Once the data has come from the template and sent to the controller, the data is passed inside as a parameter to the model where data can be inserted inside the query to either read, create, or delete data inside the schema.