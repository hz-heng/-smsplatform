from flask_login import LoginManager

login_manager = LoginManager()
login_manager.session_protection = 'strong'
login_manager.login_view = 'auth.login'
login_manager.login_message = "请先登录"
login_manager.login_message_category = "info"

@login_manager.user_loader
def load_user(user_id):
    from app.models import User
    return User.query.get(user_id)
