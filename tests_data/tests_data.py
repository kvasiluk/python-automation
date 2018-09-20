import os
import json

from utils.config import Config


class TestsData(object):
    @staticmethod
    def json_schema_by_name(schema_name):
        scheme_filepostfix = ".schema"
        filename = "{}{}".format(schema_name, scheme_filepostfix)
        files = os.listdir(Config.json_schemas_path)
        assert filename in files, "Wrong requested schema filename: <{}>. " \
                                  "Available schemas: \n{}".format(schema_name, "\n".join(files))
        filename = os.path.join(os.getcwd(), Config.json_schemas_path, filename)
        with open(filename, "rb") as f:
            return json.load(f)
