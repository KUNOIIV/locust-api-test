from locust import HttpUser, task
class WebsiteUser(HttpUser):
    host = "https://httpbin.org"    # this line fixes the error
    @task
    def load_test(self):
        self.client.get("/delay/0")