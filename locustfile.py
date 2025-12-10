
from locust import HttpUser, task, between

class WebsiteUser(HttpUser):
    host = "https://jsonplaceholder.typicode.com"
    wait_time = between(1, 3)

    @task 
    def create_user(self): # This creates a post to the endpoint. Simulates user signup by POSTing JSON to /posts
        self.client.post(
            "/posts",                                   
            json={"title": "Sword", "body": "Warrior", "userId": 1},
            name="POST /posts"
        )

    @task
    def get_users(self): # Fetches list of users/posts
        self.client.get("/posts", name="GET /posts")   

    @task
    def update_user(self): # Updates existing record
        self.client.put(
            "/posts/1",                                 
            json={"title": "Updated Sword", "body": "Master Warrior", "userId": 1},
            name="PUT /posts/1"
        )

    @task
    def delete_user(self): # Deletes record ID 1
        self.client.delete("/posts/1", name="DELETE /posts/1")

    