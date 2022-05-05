from app import create_app,db
from app.models import User,Role
from flask_script import  Manager,Server
from flask_migrate import Migrate,MigrateCommand

# creating app instance
app = create_app('development')

manager = Manager(app)
manager .add_command('server',Server)
@manager.command
def test():
    '''
    run unittests
    '''
    import unittest
    tests = unittest.TestLoader().discover('test')
    unittest.TextTestRunner(verbosity=2).run(tests)

@manager.shell
def make_shell_context():
    return dict(app = app, db = db, User = User, Role = Role)

migrate = Migrate(app,db)
manager.add_command('db',MigrateCommand)

if __name__ == '__main__':
    manager.run()