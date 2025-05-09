import os
import psycopg2
from psycopg2 import sql
from dotenv import load_dotenv
import logging

load_dotenv()

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class PostgresRDSClient:
    _connection = None

    @staticmethod
    def get_connection():
        if PostgresRDSClient._connection is None:
            try:
                PostgresRDSClient._connection = psycopg2.connect(
                    dbname=os.getenv("RDS_DB_NAME"),
                    user=os.getenv("RDS_USERNAME"),
                    password=os.getenv("RDS_PASSWORD"),
                    host=os.getenv("RDS_HOST"),
                    port=os.getenv("RDS_PORT")
                )
                logger.info("Connected to Amazon RDS PostgreSQL")
            except psycopg2.OperationalError as e:
                # Check if the error is because the database doesn't exist
                if "does not exist" in str(e):
                    logger.info(f"Database {os.getenv('RDS_DB_NAME')} does not exist. Attempting to create it.")
                    PostgresRDSClient._create_database()
                    # Try to connect again after creating the database
                    PostgresRDSClient._connection = psycopg2.connect(
                        dbname=os.getenv("RDS_DB_NAME"),
                        user=os.getenv("RDS_USERNAME"),
                        password=os.getenv("RDS_PASSWORD"),
                        host=os.getenv("RDS_HOST"),
                        port=os.getenv("RDS_PORT")
                    )
                    logger.info(f"Connected to newly created database {os.getenv('RDS_DB_NAME')}")
                else:
                    logger.error(f"Error connecting to PostgreSQL: {str(e)}")
                    raise
            except Exception as e:
                logger.error(f"Error connecting to PostgreSQL: {str(e)}")
                raise
        return PostgresRDSClient._connection

    @staticmethod
    def _create_database():
        """Creates the database if it doesn't exist."""
        # Connect to default 'postgres' database to create our database
        try:
            conn = psycopg2.connect(
                dbname="postgres",  # Connect to default postgres database
                user=os.getenv("RDS_USERNAME"),
                password=os.getenv("RDS_PASSWORD"),
                host=os.getenv("RDS_HOST"),
                port=os.getenv("RDS_PORT")
            )
            conn.autocommit = True  # Required for creating database
            
            with conn.cursor() as cursor:
                db_name = os.getenv("RDS_DB_NAME")
                # Use sql.Identifier to safely quote the database name
                cursor.execute(
                    sql.SQL("CREATE DATABASE {}").format(sql.Identifier(db_name))
                )
                logger.info(f"Database {db_name} created successfully")
            
            conn.close()
            
            # After creating the database, initialize schema if needed
            PostgresRDSClient._initialize_schema()
        except Exception as e:
            logger.error(f"Error creating database: {str(e)}")
            raise

    @staticmethod
    def _initialize_schema():
        """Initialize database schema with required tables."""
        # Connect to the newly created database and create tables
        try:
            temp_conn = psycopg2.connect(
                dbname=os.getenv("RDS_DB_NAME"),
                user=os.getenv("RDS_USERNAME"),
                password=os.getenv("RDS_PASSWORD"),
                host=os.getenv("RDS_HOST"),
                port=os.getenv("RDS_PORT")
            )
            temp_conn.autocommit = True
            
            with temp_conn.cursor() as cursor:
                # Create users table
                cursor.execute("""
                    CREATE TABLE IF NOT EXISTS users (
                        id SERIAL PRIMARY KEY,
                        username VARCHAR(20) UNIQUE NOT NULL,
                        email VARCHAR(255) UNIQUE NOT NULL,
                        password VARCHAR(255),
                        name VARCHAR(255),
                        age INTEGER,
                        gender VARCHAR(10),
                        preferred_language VARCHAR(2),
                        profile_picture VARCHAR(255),
                        google_id VARCHAR(255)
                    )
                """)
                logger.info("Database schema initialized successfully")
            
            temp_conn.close()
        except Exception as e:
            logger.error(f"Error initializing schema: {str(e)}")
            raise

    @staticmethod
    def check_database_exists():
        """Check if the database exists."""
        try:
            conn = psycopg2.connect(
                dbname="postgres",
                user=os.getenv("RDS_USERNAME"),
                password=os.getenv("RDS_PASSWORD"),
                host=os.getenv("RDS_HOST"),
                port=os.getenv("RDS_PORT")
            )
            conn.autocommit = True
            
            with conn.cursor() as cursor:
                cursor.execute("SELECT 1 FROM pg_database WHERE datname = %s", 
                             (os.getenv("RDS_DB_NAME"),))
                exists = cursor.fetchone() is not None
            
            conn.close()
            return exists
        except Exception as e:
            logger.error(f"Error checking if database exists: {str(e)}")
            raise

    @staticmethod
    def execute_query(query, params=None, fetch_one=False, fetch_all=False):
        conn = PostgresRDSClient.get_connection()
        with conn.cursor() as cursor:
            try:
                cursor.execute(query, params)
                if fetch_one:
                    result = cursor.fetchone()
                    if result:
                        # Return both the result and column descriptions
                        columns = [desc[0] for desc in cursor.description]
                        return {"data": result, "columns": columns}
                    return None
                if fetch_all:
                    results = cursor.fetchall()
                    if results:
                        # Return both results and column descriptions
                        columns = [desc[0] for desc in cursor.description]
                        return {"data": results, "columns": columns}
                    return None
                conn.commit()
            except Exception as e:
                logger.error(f"Error executing query: {str(e)}")
                conn.rollback()
                raise
