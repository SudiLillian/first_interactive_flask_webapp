from app import db

class User(db.Model):
  """Create User table details."""

  __tablename__ = 'user'
  id = db.Column(db.Integer, primary_key=True)
  first_name = db.Column(db.String(80))
  username = db.Column(db.String(100))
  password = db.Column(db.String(100))

  def __init__(self, first_name, username, password):
    """Initialize new user."""
    self.first_name = first_name
    self.username = username
    self.password = password
