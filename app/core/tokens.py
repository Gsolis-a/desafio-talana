from django.contrib.auth.tokens import PasswordResetTokenGenerator
import uuid as encode


class AccountActivationTokenGenerator(PasswordResetTokenGenerator):
    def _make_hash_value(self, user, timestamp):
        return (encode.uuid4().hex)


account_activation_token = AccountActivationTokenGenerator()
