from singleton import Singleton
import os

class Configuration(Singleton):
    def __init__(self, filename=None, columns=None):
        # This prevents re-initialization every time you call the class
        if self._initialized:
            return

        self.absolute_path = os.getcwd()
        self._filename = filename
        self._columns_to_extract = columns

        # Logic for paths
        if filename:
            self.set_filepath(filename)

        self._initialized = True

    def set_filepath(self, new_filename):
        self._filename = new_filename
        self._filepath_to_output = os.path.join(self.absolute_path, 'output', self._filename)
        self._filepath_to_save = os.path.join(self.absolute_path, 'processed', self._filename)
        self._filepath_to_extract = os.path.join(self.absolute_path, 'raw', self._filename)

    def get_filepath_to_extract(self):
        return self._filepath_to_extract

    def get_filepath_to_save(self):
        return self._filepath_to_save

    def get_filepath_to_output(self):
        return self._filepath_to_output

    def get_columns_to_extract(self):
        return self._columns_to_extract


# Initialize the one and only instance
configuration = Configuration(
    "vehicle_local_position.csv",
    ["x", "y", "z", "vx", "vy", "vz", "ax", "ay", "az", "heading", "timestamp"]
)