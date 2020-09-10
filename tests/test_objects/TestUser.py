from django.contrib.auth.models import User

class TestUser:
    username = "Kastriot"
    password = "12345678"

    def __init__(self):
        try:
            User.objects.get(username=self.username)
        except User.DoesNotExist:
            user = User.objects.create(
                username=self.username
            )
            user.set_password(self.password)
            user.save()

    def get_test_user(self):
        return User.objects.get(username=self.username)