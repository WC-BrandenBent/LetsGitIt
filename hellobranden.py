from flask import Flask
from datetime import datetime
from flask_jwt_extended import (
    create_access_token,
    jwt_required,
    unset_jwt_cookies,
    jwt_required,
    get_jwt_identity,
)


def hello():
    print("Hello World")

def hello_abraham():
    print("Hello Abraham")
hello()
hello_abraham()