

from datetime import datetime, timedelta

from ..enums.TokenType import TokenType
from ..models.Token import Token
from ..models.TokenSpecs import TokenSpecs

class TokenGenerator:
    @classmethod
    def GenerateRememberMe (cls, valid_for : timedelta = timedelta(hours=1)):  
        from hashlib import md5  

        n = datetime.now()
        e = n + valid_for

        return Token[str](
            value=md5(f"{n.strftime('%d%m%Y%H%M%S')}".encode()).hexdigest(),
            name='remember_me',
            specs=TokenSpecs(
                type=TokenType.MD5,
                created=n,
                expiry=e,
            )
        )
    