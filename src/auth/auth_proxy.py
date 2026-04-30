from typing import Optional, Dict
from .http_client import HttpClient


class AuthProxy:
    """
    Authentication proxy wrapping HttpClient.
    
    Uses composition pattern - delegates to wrapped client.
    """
    
    def __init__(self, client: HttpClient, auth_strategy):
        """
        Initialize with client and strategy.
        
        Args:
            client: HttpClient to wrap
            auth_strategy: Authentication strategy
        """
        self.client = client
        self.auth_strategy = auth_strategy
    
    def request(self, method: str, url: str, headers: Optional[Dict] = None, **kwargs):
        """
        Make authenticated request.
        
        Adds auth via strategy, then delegates to wrapped client.
        """
        headers = self.auth_strategy.add_auth(headers)
        return self.client.request(method, url, headers=headers, **kwargs)
    
    def get(self, url: str, **kwargs):
        """Authenticated GET request."""
        return self.request('GET', url, **kwargs)
    
    def post(self, url: str, **kwargs):
        """Authenticated POST request."""
        return self.request('POST', url, **kwargs)