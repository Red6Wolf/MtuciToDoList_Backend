#LOCAL
from app.schemas.user_schema import UserAuth
from app.models.user_model import User
from app.core.security import get_password

class UserService:
    @staticmethod
    async def create_user(user : UserAuth):
        user_in = User(
            username = user.username,
            email = user.email,
            hashed_password = get_password(user.password)
        )
        await user_in.save()
        return user_in
        