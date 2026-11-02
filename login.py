"""Small in-memory login exercise using salted password hashes."""
from hashlib import pbkdf2_hmac
from hmac import compare_digest


def hash_password(password, salt):
    """Derive a password hash for this educational example."""
    return pbkdf2_hmac("sha256", password.encode("utf-8"), salt, 200_000)


def login(username, password, users):
    """Return True when credentials match a stored (salt, hash) record."""
    if not isinstance(username, str) or not isinstance(password, str):
        return False
    if not username or not password or username not in users:
        return False
    salt, expected_hash = users[username]
    return compare_digest(hash_password(password, salt), expected_hash)
