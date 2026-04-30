# Lab 8: Authentication Proxy for API Service

Layered architecture for handling API authentication using composition and dependency injection.

## Architecture

Three independent layers:

1. **HttpClient** - Base HTTP client (no authentication knowledge)
2. **AuthProxy** - Authentication wrapper (composition pattern)
3. **Strategies** - Different authentication methods

## Components

### HttpClient

Base HTTP client for making requests without authentication.

**Usage:**

```python
from lab8 import HttpClient

client = HttpClient()
response = client.get('https://api.example.com/data')
```

### AuthProxy

Proxy that wraps HttpClient and adds authentication.

Uses composition pattern - accepts client as parameter.

**Usage:**

```python
from lab8 import HttpClient, AuthProxy, ApiKeyStrategy

base_client = HttpClient()
strategy = ApiKeyStrategy(api_key='secret-key')
auth_client = AuthProxy(base_client, strategy)

response = auth_client.get('https://api.example.com/data')
```

### Authentication Strategies

**API Key:**

```python
strategy = ApiKeyStrategy(api_key='key-123', header_name='X-API-Key')
```

**Bearer Token:**

```python
strategy = BearerTokenStrategy(token='access-token')
```

**JWT:**

```python
strategy = JwtStrategy(jwt_token='eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9')
```

## Dependency Injection Pattern

Services receive HttpClient through constructor:

```python
class GithubService:
    def __init__(self, client: HttpClient):
        self.client = client
    
    def get_user(self, username):
        return self.client.get(f'/users/{username}')

# Use with authentication
auth_client = AuthProxy(HttpClient(), ApiKeyStrategy('github-key'))
service = GithubService(auth_client)
```

## Dynamic Strategy Switching

```python
strategies = {
    'development': ApiKeyStrategy('dev-key'),
    'production': JwtStrategy('prod-jwt-token')
}

env = 'production'
client = AuthProxy(HttpClient(), strategies[env])
```

## Files

- `http_client.py` - Base HTTP client
- `auth_proxy.py` - Authentication proxy
- `strategies.py` - Auth strategies (API Key, Bearer, JWT)
- `examples.py` - Usage examples

## Running Examples

```bash
python lab8/examples.py
```

## Requirements

- Python >= 3.8
- requests library