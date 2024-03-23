import requests
import json
lst = []

posts_response = requests.get("https://jsonplaceholder.typicode.com/posts")
my_posts = posts_response.json()


coments_response = requests.get("https://jsonplaceholder.typicode.com/comments")
my_coments = coments_response.json()


todos_response = requests.get("https://jsonplaceholder.typicode.com/todos")
my_todos = todos_response.json()


lst.append({
    "post": my_posts,
    "comment": my_coments,
    "todos": my_todos
})

with open("my_json.json", "w") as file:
    json.dump(lst, file, indent=2)
