from flask import render_template, request, redirect, flash, session
from flask_app import app
from flask_app.models.user import User
# from flask_app.models.sighting import Sighting
from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)


@app.route('/')
def index():
  print(f"??????????????????????????????????????????????????? {User.get_one}")
  return render_template('index.html', patient=User.get_one, patients=User.get_all)

# @app.route('/dashboard')
# def dashboard():
#   if 'user_id' not in session:
#     return redirect('/logout')
#   data ={
#     'id': session['user_id'],
#   }
#   return render_template("dashboard.html", user=User.get_by_id(data), all_sightings=Sighting.get_all(), sightings=User.get_name_by_id(data))

# @app.route('/logout')
# def logout():
#   session.clear()
#   return redirect('/')