# Importando bibliotecas
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
import os

# Criando site
app = Flask(__name__)
# Definindo  token de segurança
app.config["SECRET_KEY"] = "97174de82de975265f1f15fd869044f4"
# Configurações do banco de dados
if os.getenv("DATABASE_URL"):
    app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("DATABASE_URL")
else:
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///comunidade.db"
# Criando banco de dados
database = SQLAlchemy(app)
bcrypt = Bcrypt(app)
# Configuração de login
login_manager = LoginManager(app)
login_manager.login_view = "login"
login_manager.login_message_category = "alert-info"


from comunidadeimpressionadora import routes