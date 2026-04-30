from typing import Optional, Dict, Any


class HttpClient:
    """
    Base HTTP client for making requests.
    
    Does not handle authentication.
    """
    
    def request(self, method: str, url: str, headers: Optional[Dict] = None, **kwargs) -> Any:
        """
        Make HTTP request.
        
        Args:
            method: HTTP method
            url: Request URL
            headers: Optional headers
            **kwargs: Additional parameters
        
        Returns:
            Response object
        """
        import requests
        return requests.request(method, url, headers=headers, **kwargs)
    
    def get(self, url: str, **kwargs):
        """GET request."""
        return self.request('GET', url, **kwargs)
    
    def post(self, url: str, **kwargs):
        """POST request."""
        return self.request('POST', url, **kwargs)