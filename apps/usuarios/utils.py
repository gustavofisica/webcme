from django.contrib.auth.tokens import PasswordResetTokenGenerator


class TokenGenerator(PasswordResetTokenGenerator):
    def _make_hash_value(self, usuario, timestamp):
        return str(usuario.pk)+str(timestamp)+str(usuario.is_active)


gerar_token = TokenGenerator()
