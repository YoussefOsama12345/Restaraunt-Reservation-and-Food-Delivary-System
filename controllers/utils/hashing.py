"""
hashing_util.py

This module provides utility functions for generating and verifying hashes for various types of data.
It includes functions for creating secure hashes using popular algorithms like bcrypt and SHA256,
as well as for verifying password hashes.

📌 Features:
- Generate secure password hashes using bcrypt with salting.
- Verify passwords by comparing them to their stored bcrypt hashes.
- Generate SHA256 hashes for strings and verify their integrity.
- Utilize cryptographic algorithms to ensure data security.

🛠️ Dependencies:
- hashlib -> For generating cryptographic hash values (SHA256).
- bcrypt -> For securely hashing passwords using bcrypt, including salting.

Functions:
- generate_bcrypt_hash(password: str) -> str: Generates a bcrypt hash for a given password, including salting.
- verify_bcrypt_hash(password: str, hashed_password: str) -> bool: Verifies if a password matches the stored bcrypt hash.
- generate_sha256_hash(data: str) -> str: Generates a SHA256 hash for a given string.
- verify_sha256_hash(data: str, expected_hash: str) -> bool: Verifies if a string matches the expected SHA256 hash.

Note: Use bcrypt for hashing passwords due to its security and salting mechanisms.
SHA256 is suitable for non-password-related sensitive data such as transaction IDs or file integrity checks.
"""

import hashlib
import bcrypt

def generate_bcrypt_hash(password: str) -> str:
    """
    Generates a bcrypt hash for a given password, including salting.

    :param password: The password to hash.
    :return: The bcrypt hash of the password.
    """

    salt = bcrypt.gensalt()
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), salt)
    return hashed_password.decode('utf-8')

def verify_bcrypt_hash(password: str, hashed_password: str) -> bool:
    """
    Verifies if a given password matches the stored bcrypt hash.

    :param password: The plaintext password to check.
    :param hashed_password: The stored bcrypt hash to compare against.
    :return: True if the password matches the hash, False otherwise.
    """

    return bcrypt.checkpw(password.encode('utf-8'), hashed_password.encode('utf-8'))

def generate_sha256_hash(data: str) -> str:
    """
    Generates a SHA256 hash for a given string.

    :param data: The string to hash.
    :return: The SHA256 hash of the input string.
    """

    sha256_hash = hashlib.sha256()
    sha256_hash.update(data.encode('utf-8'))
    return sha256_hash.hexdigest()

def verify_sha256_hash(data: str, expected_hash: str) -> bool:
    """
    Verifies if a given string matches the expected SHA256 hash.

    :param data: The string to check.
    :param expected_hash: The expected SHA256 hash to compare against.
    :return: True if the string matches the expected hash, False otherwise.
    """
    
    generated_hash = generate_sha256_hash(data)
    return generated_hash == expected_hash

