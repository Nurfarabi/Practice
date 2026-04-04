import psycopg2
from config import db_condig

def get_connection():
    return psycopg2.connect(**db_condig)