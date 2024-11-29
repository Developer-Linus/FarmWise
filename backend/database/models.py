# backend/database/models.py

import sqlite3

def init_db():
  """
  Initialize the SQLite database and create necessary tables.
  """
  conn = sqlite3.connect('farmwise.db')
  cursor = conn.cursor()

  # Create a table for storing user inputs and advice
  cursor.execute('''
      CREATE TABLE IF NOT EXISTS user_data (
          id INTEGER PRIMARY KEY AUTOINCREMENT,
          crop_type TEXT,
          soil_condition TEXT,
          weather TEXT,
          advice TEXT
      )
  ''')

  conn.commit()
  conn.close()