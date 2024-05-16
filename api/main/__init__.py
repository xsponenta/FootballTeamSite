"Init module"

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from main.models import Base
from flask import Flask
from flask_cors import CORS

app = Flask(__name__)
app.config['SECRET_KEY'] = "HW3_SUPER_SECRET_KEY"
CORS(app)
engine = create_engine('sqlite:///petro_united.db', echo=False, pool_size = 0, max_overflow = -1)
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)

from main import routes
