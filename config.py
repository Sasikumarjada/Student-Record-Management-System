import os

class Config:
    MYSQL_USER = os.environ.get("MYSQL_USER", "root")
    MYSQL_PASSWORD = os.environ.get("MYSQL_PASSWORD", "password")
    MYSQL_HOST = os.environ.get("MYSQL_HOST", "db")
    MYSQL_PORT = int(os.environ.get("MYSQL_PORT", 3306))
    MYSQL_DATABASE = os.environ.get("MYSQL_DATABASE", "students_db")

    SQLALCHEMY_DATABASE_URI = (
        f"mysql+pymysql://{MYSQL_USER}:{MYSQL_PASSWORD}@{MYSQL_HOST}:{MYSQL_PORT}/{MYSQL_DATABASE}"
    )
    SQLALCHEMY_TRACK_MODIFICATIONS = False
