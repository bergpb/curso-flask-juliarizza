# do modulo tal import a classe tal
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand

app = Flask(__name__)
# passando arquivos de config atraves de um arquivo sem sua extensao
app.config.from_object('config')
# recebe a instancia do flask definida acima
db = SQLAlchemy(app)
migrate = Migrate(app, db)

manager = Manager(app)
manager.add_command('db', MigrateCommand)

# python3 import completo do modulo, nao pode ser relativo
from app.controllers import default