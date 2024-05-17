from db.db import db, app, migrate, jwt

# Importa los modelos
from models.user import User
from models.nutritionist import Nutritionist
from models.comment import Comment
from models.professional_tip import ProfessionalTip

# Importa las rutas
from routes.user_routes import user_api
from routes.nutritionist_routes import nutritionist_api
from routes.comment_routes import comment_api
from routes.professional_tip_routes import professional_tip_api

# Registra las rutas
app.register_blueprint(user_api, url_prefix='/api')
app.register_blueprint(nutritionist_api, url_prefix='/api')
app.register_blueprint(comment_api, url_prefix='/api')
app.register_blueprint(professional_tip_api, url_prefix='/api')


if __name__ == "__main__":
    app.run(debug=True, port=5000)
