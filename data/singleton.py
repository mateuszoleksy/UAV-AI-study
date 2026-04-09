import os

class Singleton:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            # Create the instance once
            cls._instance = super(Singleton, cls).__new__(cls)
            # Flag it as not initialized yet
            cls._instance._initialized = False
        return cls._instance