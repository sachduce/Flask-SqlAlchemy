
import os
from src import create_app, db

from flask_script import Manager, prompt_bool
from flask_migrate import Migrate, MigrateCommand


app = create_app(os.getenv('EXAMINATION_ENV') or 'dev')

manager = Manager(app)
migrate = Migrate(app, db)


manager.add_command('db', MigrateCommand)


@manager.command
def dropdb():
    if prompt_bool('Are you sure you want to drop database'):
        db.drop_all()
        print 'Dropped the database'


if __name__ == '__main__':
    manager.run()