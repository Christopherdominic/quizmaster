import os
from dotenv import load_dotenv
from app import create_app
from config import Config

load_dotenv()

app = create_app(Config)

print("Database URI:", app.config['SQLALCHEMY_DATABASE_URI'])  # Add this line to verify

if __name__ == '__main__':
    app.run(debug=True)

