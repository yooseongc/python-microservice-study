import functools
from flask_login import current_user, LoginManager
from monolith.database import User


login_manager = LoginManager()


def admin_required(func):
    @functools.wrap(func)
    def _admin_required(*args, **kwargs):
        admin = current_user.is_authenticated and current_user.is_admin
        if not admin:
            return login_manager.unauthorized()
        return func(*args, **kwargs)
    
    return _admin_required


@login_manager.user_loader
def load_user(user_id: int) -> User:
    user = User.query.get(user_id)
    if user is not None:
        user._authenticated = True
    return user
