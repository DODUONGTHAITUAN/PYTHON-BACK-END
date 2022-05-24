from uuid import uuid4
from bcrypt import hashpw, checkpw, gensalt


def random_code():
    return uuid4().hex


def hash_code(str):
    return hashpw(str.encode("utf-8"), gensalt())


def check_code(str, hashed):
    return checkpw(str.encode("utf-8"), hashed)
