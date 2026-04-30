from src.auth.http_client import HttpClient
from src.auth.auth_proxy import AuthProxy
from src.auth.strategies import ApiKeyStrategy, BearerTokenStrategy, JwtStrategy


print("Example 1: API Key authentication\n")

base_client = HttpClient()
api_strategy = ApiKeyStrategy(api_key='my-secret-key-123')
auth_client = AuthProxy(base_client, api_strategy)

print("Client configured with API Key strategy")
print(f"Strategy type: {type(auth_client.auth_strategy).__name__}")
headers = auth_client.auth_strategy.add_auth()
print(f"Headers: {headers}")
print()


print("Example 2: Bearer Token authentication\n")

bearer_strategy = BearerTokenStrategy(token='user-access-token-xyz')
bearer_client = AuthProxy(base_client, bearer_strategy)

print("Client configured with Bearer Token strategy")
print(f"Strategy type: {type(bearer_client.auth_strategy).__name__}")
headers = bearer_client.auth_strategy.add_auth()
print(f"Headers: {headers}")
print()


print("Example 3: JWT authentication\n")

jwt_strategy = JwtStrategy(jwt_token='eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9')
jwt_client = AuthProxy(base_client, jwt_strategy)

print("Client configured with JWT strategy")
print(f"Strategy type: {type(jwt_client.auth_strategy).__name__}")
headers = jwt_client.auth_strategy.add_auth()
print(f"Headers: {headers}")
print()


print("Example 4: Service with Dependency Injection\n")

class GithubService:
    """
    Example service using DI pattern.
    
    Accepts HttpClient through constructor.
    """
    
    def __init__(self, client: HttpClient):
        self.client = client
    
    def get_user_info(self, username: str):
        print(f"Getting user info for: {username}")
        print(f"Using client: {type(self.client).__name__}")
        return f"User data for {username}"


# use with different auth strategies
api_key_client = AuthProxy(HttpClient(), ApiKeyStrategy('github-key'))
github_service = GithubService(api_key_client)

result = github_service.get_user_info('octocat')
print(f"Result: {result}")
print()


print("Example 5: Dynamic strategy switching\n")

strategies = {
    'api_key': ApiKeyStrategy('key-123'),
    'bearer': BearerTokenStrategy('token-456'),
    'jwt': JwtStrategy('jwt-789')
}

print("Available strategies:")
for name, strategy in strategies.items():
    client = AuthProxy(HttpClient(), strategy)
    headers = client.auth_strategy.add_auth()
    print(f"  {name}: {headers}")