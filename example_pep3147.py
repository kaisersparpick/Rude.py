from rude import Rude
from random import randint


class Pep3147(object):
    """ The logic for this example was taken from:
    PEP 3147 -- PYC Repository Directories
    https://www.python.org/dev/peps/pep-3147/
    """

    def __init__(self):
        self.result = None

    def py_found(self):
        """ foo.py found? """
        return Pep3147.get_random_value()

    def pyc_found(self):
        """ matching foo.pyc found? """
        return Pep3147.get_random_value()

    def load_pyc(self):
        """ load foo.pyc """
        success = Pep3147.get_random_value()
        if not success:
            self.result = 'Could not load foo.pyc'
        return success

    def pycache_pyc_found(self):
        """ matching pycache/foo.<magic>.pyc found? """
        return Pep3147.get_random_value()

    def load_pycache_pyc(self):
        """ load pycache/foo.<magic>.pyc """
        success = Pep3147.get_random_value()
        if not success:
            self.result = 'Could not load pycache/foo.<magic>.pyc'
        return success

    def pycache_exists(self):
        """ pycache/ exists? """
        return Pep3147.get_random_value()

    def create_pycache(self):
        """ create pycache/ """
        success = Pep3147.get_random_value()
        if not success:
            self.result = 'Could not create pycache/'
        return success

    def byte_compile(self):
        """ byte compile foo.py """
        success = Pep3147.get_random_value()
        if not success:
            self.result = 'Could not byte compile foo.py'
        return success

    def write_pycache(self):
        """ write pycache/foo.<magic>.pyc """
        success = Pep3147.get_random_value()
        if not success:
            self.result = 'Could not write pycache/foo.<magic>.pyc'
        return success

    def success(self):
        """ yay! """
        self.result = 'Yay!'
        return None

    def import_error(self):
        """ bummer :( """
        self.result = 'Import Error'
        return None

    def other_error(self):
        """ bummer :( """
        return None

    @staticmethod
    def get_random_value():
        return randint(1, 10) % 2 == 0


app = Pep3147()

rude = Rude()
rude.add_rule(app.py_found, app.pycache_pyc_found, app.pyc_found)
rude.add_rule(app.pyc_found, app.load_pyc, app.import_error)
rude.add_rule(app.load_pyc, app.success, app.other_error)
rude.add_rule(app.pycache_pyc_found, app.load_pycache_pyc, app.pycache_exists)
rude.add_rule(app.load_pycache_pyc, app.success, app.other_error)
rude.add_rule(app.pycache_exists, app.byte_compile, app.create_pycache)
rude.add_rule(app.byte_compile, app.write_pycache, app.other_error)
rude.add_rule(app.create_pycache, app.byte_compile, app.other_error)
rude.add_rule(app.write_pycache, app.success, app.other_error)
rude.add_rule(app.success)
rude.add_rule(app.import_error)
rude.add_rule(app.other_error)

print("=====================================")
print("Rude.py example")
print("=====================================")
print("Generating random results...")

for i in range(1,11):
    print("---", i, "--------")
    rude.check_conditions(app.py_found)
    print('The result is:', app.result)
    print('And the path was:', rude.get_path())

print("-----------------------")
print("Finished")
