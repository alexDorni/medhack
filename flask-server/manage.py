import sqlalchemy as sa
from flask_migrate import Migrate
from flask_migrate import MigrateCommand
from flask_script import Manager

import application  # noqar
from settings import server, db
from utils.printer import Printer

__all__ = ['settings']

with server.server_context():
    from sqlalchemy_continuum import make_versioned
    from sqlalchemy_continuum.plugins import FlaskPlugin

    make_versioned(user_cls=None, plugins=[FlaskPlugin()])
manager = Manager(server)

manager.add_command('db', MigrateCommand)
migrate = Migrate(server, db)


@manager.command
def create_all():
    if server.config['DEBUG']:
        sa.orm.configure_mappers()
        db.create_all()
        Printer.info('tables created')


if __name__ == '__main__':
    manager.run()
