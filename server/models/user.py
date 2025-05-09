"""This module defines the User model, which represents a user in the system."""
""" Step 1: Import required libraries """
from pydantic import BaseModel, EmailStr, Field, field_validator, validator
from services.postgres_rds import PostgresRDSClient
from bson import ObjectId
from email_validator import validate_email, EmailNotValidError
from typing import Optional, Union

""" Step 2: Define the User model """
class User(BaseModel):
    id: Optional[Union[str, int]] = None
    username: str = Field(..., min_length=3, max_length=20)
    email: EmailStr
    password: Optional[str] = Field(None, min_length=6)
    name: Optional[str] = None
    age: Optional[int] = Field(None, ge=18)  # Age should be a non-negative integer
    gender: Optional[str] = Field(None, pattern='^(male|female|other)$')  # Example to validate gender
    preferredLanguage: Optional[str] = Field(None, pattern='^[a-z]{2}$')  
    profile_picture: Optional[str] = Field("https://i.pinimg.com/736x/0d/64/98/0d64989794b1a4c9d89bff571d3d5842.jpg")
    google_id: Optional[str] = None
    
    """ Step 3: Define class methods """
    # Define a class method to validate the password field
    @validator('password')
    def validate_password(cls, v, values, **kwargs):
        # Allow password to be None (for OAuth users)
        if v is None:
            return v
        if not isinstance(v, str):
            raise ValueError('Password must be a string')
        if len(v) < 6:
            raise ValueError('Password must be at least 6 characters long')
        return v
    
    # Define a class method to find a user by username
    @field_validator('username')
    def username_alphanumeric(cls, v):
        assert v.isalnum(), 'must be alphanumeric'
        return v
    
    # Define a class method to validate the email field
    @field_validator('email')
    def validate_email_field(cls, v):
        try:
            valid = validate_email(v)
            return valid.email
        except EmailNotValidError as e:
            raise ValueError(str(e))
    
    @field_validator('id')
    def convert_id_to_string(cls, v):
        if v is None:
            return v
        return str(v)  # Convert any ID to string

    # Define a class method to find a user by username
    @classmethod
    def find_by_username(cls, username):
        query = "SELECT * FROM users WHERE username = %s"
        result = PostgresRDSClient.execute_query(query, (username,), fetch_one=True)
        if result:
            # Map column names to values and convert types as needed
            user_dict = dict(zip(result["columns"], result["data"]))
            # Ensure ID is a string
            if 'id' in user_dict and user_dict['id'] is not None:
                user_dict['id'] = str(user_dict['id'])
            return cls(**user_dict)
        return None
    
    # Define a class method to find a user by email
    @classmethod
    def update_password(cls, username, new_hashed_password):
        query = "UPDATE users SET password = %s WHERE username = %s"
        result = PostgresRDSClient.execute_query(query, (new_hashed_password, username))
        return result is not None
    
    # Define a class method to find a user by ID
    @classmethod
    def find_by_id(cls, user_id):
        query = "SELECT * FROM users WHERE id = %s"
        result = PostgresRDSClient.execute_query(query, (user_id,), fetch_one=True)
        if result:
            # Map column names to values and convert types as needed
            user_dict = dict(zip(result["columns"], result["data"]))
            # Ensure ID is a string
            if 'id' in user_dict and user_dict['id'] is not None:
                user_dict['id'] = str(user_dict['id'])
            return cls(**user_dict)
        return None
    
    # Define a class method to find a user by email
    @classmethod
    def find_by_email(cls, email):
        query = "SELECT * FROM users WHERE email = %s"
        result = PostgresRDSClient.execute_query(query, (email,), fetch_one=True)
        if result:
            # Map column names to values and convert types as needed
            user_dict = dict(zip(result["columns"], result["data"]))
            # Ensure ID is a string
            if 'id' in user_dict and user_dict['id'] is not None:
                user_dict['id'] = str(user_dict['id'])
            return cls(**user_dict)
        return None