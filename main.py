from requests import get as get_request 

response = get_request("https://jsonplaceholder.typicode.com/todos")

print(response.json())