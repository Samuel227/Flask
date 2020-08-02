import os


class Config(object):
    SECRET_KEY = (
        os.environ.get("SECRET_KEY")
        or b"\xaf\x96\xaa\xf9\x964l\xfd\xba\xa2\x10J\xca\xb7t\xcf"
    )

    MONGODB_SETTINGS = {"db": "Servease"}

