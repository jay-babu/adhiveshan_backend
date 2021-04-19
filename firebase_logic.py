import os

from cryptography.fernet import Fernet
from firebase_admin import auth
from firebase_admin.auth import InvalidIdTokenError


def encrypt_cred():
    key = os.getenv('CREDENTIALS_KEY')
    key = key.encode('utf-8')
    input_file = 'adhiveshan-firebase-adminsdk.json'
    output_file = 'adhiveshan-firebase-adminsdk.encrypted'
    with open(input_file, 'rb') as f:
        data = f.read()
    fernet = Fernet(key)
    encrypted = fernet.encrypt(data)
    with open(output_file, 'wb') as f:
        f.write(encrypted)


def decrypt_file():
    key = os.getenv('CREDENTIALS_KEY')
    key = key.encode('utf-8')

    output_file = 'adhiveshan-firebase-adminsdk.json'
    input_file = 'adhiveshan-firebase-adminsdk.encrypted'

    with open(input_file, 'rb') as f:
        data = f.read()

    fernet = Fernet(key)
    encrypted = fernet.decrypt(data)

    os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = os.path.join(os.getcwd(), output_file)

    with open(os.path.join(os.getcwd(), output_file), 'wb') as f:
        f.write(encrypted)


def verify_token(token: str):
    try:
        decoded_token = auth.verify_id_token(token)
        return decoded_token['uid']
    except InvalidIdTokenError:
        return False
