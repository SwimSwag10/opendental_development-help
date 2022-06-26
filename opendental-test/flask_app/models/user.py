from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash, session
import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')


class User:
  db = 'personal'
  def __init__(self,data):
    self.first_name = data['first_name']
    self.last_name = data['last_name']
    # self.patient_number = data['PatNum']
    # self.first_name = data['FName']
    # self.last_name = data['LName']
    # self.gender = data['Gender']
    # self.address = data['Address']

  @classmethod
  def get_all(cls):
    # this query is only returning one iteration of patient
    query = """SELECT * FROM user;"""
    print(f"!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
    result = connectToMySQL(cls.db).query_db(query)
    patients = []
    for row in result:
      patients.append(cls(row))
    return result
  
  print(f"###################################")

  @classmethod
  def get_one(cls):
    patients = []
    query = """SELECT * FROM user WHERE id = 1;"""
    results = connectToMySQL(cls.db).query_db(query)
    print(f"############################# {results}")
    for row in results:
      patients.append(cls(row))
    return cls(results[0])

  # this method is for getting the user's id that has been put into session[]
  # @classmethod
  # def get_by_id(cls,data):
  #   query = "SELECT * FROM patients WHERE PatNum = %(patient_number)s;"
  #   results = connectToMySQL(cls.db).query_db(query,data)
  #   return cls(results[0])