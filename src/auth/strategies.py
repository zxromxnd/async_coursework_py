from typing import Optional, Dict


class ApiKeyStrategy:
    """
    API Key authentication strategy.
    """
    
    def __init__(self, api_key: str, header_name: str = 'X-API-Key'):
        """
        Initialize API Key strategy.
        
        Args:
            api_key: API key value
            header_name: Header name for key
        """
        self.api_key = api_key
        self.header_name = header_name
    
    def add_auth(self, headers: Optional[Dict] = None) -> Dict:
        """
        Add API key to headers.
        """
        if headers is None:
            headers = {}
        
        headers[self.header_name] = self.api_key
        return headers


class BearerTokenStrategy:
    """
    Bearer Token authentication strategy.
    """
    
    def __init__(self, token: str):
        """
        Initialize Bearer Token strategy.
        
        Args:
            token: Bearer token value
        """
        self.token = token
    
    def add_auth(self, headers: Optional[Dict] = None) -> Dict:
        """
        Add Bearer token to Authorization header.
        """
        if headers is None:
            headers = {}
        
        headers['Authorization'] = f'Bearer {self.token}'
        return headers


class JwtStrategy:
    """
    JWT authentication strategy.
    """
    
    def __init__(self, jwt_token: str):
        """
        Initialize JWT strategy.
        
        Args:
            jwt_token: JWT token value
        """
        self.jwt_token = jwt_token
    
    def add_auth(self, headers: Optional[Dict] = None) -> Dict:
        """
        Add JWT token to Authorization header.
        """
        if headers is None:
            headers = {}
        
        headers['Authorization'] = f'Bearer {self.jwt_token}'
        return headers