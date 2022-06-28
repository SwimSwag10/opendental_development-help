# Startup
Make sure you have all dependancies installed on your machine before proceeding:

### python: 
Install python here with version <b>3.10^</b>:
`https://www.python.org/downloads/`
Make sure you have python installed by running `python --version` before proceeding to the next dependancy.

### pipenv
`python3 -m pipenv`
If python installed correctly pipenv should be installed automatically check with `python3 -m pipenv --version`.

### Python packages
`python3 -m pipenv install flask flask-bcrypt pymysql`
Packages are flask, flask-bcrypt, pymysql, python-dotenv

### MySQL
If you have not installed MySQL already you can follow this article by MySQL: `https://dev.mysql.com/doc/mysql-installation-excerpt/5.7/en/`.
Once installed you should be able to run `mysql -u {USERNAME} -p`. The USERNAME is usually set to `root` if you have not changed it.
After running the command you should be able to input your MySQL passcode.

### Setup .env file
Makre sure you care in this working directory: `cd opendental-test`. Once inside the directory create a `.env` file:
`touch .env`
Inside the `.env` file you can add the following 2 variables:
```
MYSQL_PASSCODE = '{MYSQLPASSWORD}'
MYSQL_USER = '{MYSQLUSERNAME}'
```
`MYSQLPASSWORD` should be your MySQL password you have set for your user. `MYSQLUSERNAME` should be your MySQL username, which is usually `root`.


``` shell
git clone 'https://github.com/SwimSwag10/opendental_development-help.git'
```

```
cd opendental-test
```

```

```

# Info:
`data` inside the controller `users.py` has to have data inside this method and then apply this as a parameter to the model `user.py` for the model to correctly get the data from the query inside the sql schema.

## Inside the controller `users.py`
``` python
@app.route('/')
def index():
  data = {
    'id' : 1,
  }
  return render_template('index.html', patient=User.get_one(data), patients=User.get_all)
```
These methods are for passing variables and getting data from the templates to the queries located inside the models.

## Inside the model `user.py`
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