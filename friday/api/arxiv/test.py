from security import safe_requests

response = safe_requests.get(
    'http://43.159.144.130:8079/tools/arxiv',
    json={'query': 'autogen'}
)

print(response.json())
