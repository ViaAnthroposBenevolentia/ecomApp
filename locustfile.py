from locust import HttpUser, task, between

class EcommerceUser(HttpUser):
    wait_time = between(1, 5)
    token = None

    def on_start(self):
        self.login()

    def login(self):
        response = self.client.post("/api/token/", json={
            "username": "test_user",
            "password": "password123" 
        })
        if response.status_code == 200:
            self.token = response.json().get("access")
            print(f"Logged in! Token: {self.token}")
        else:
            print(f"Failed to log in: {response.status_code} - {response.text}")

    @task(1)
    def view_products(self):
        headers = self._get_headers()
        self.client.get("/api/products/", headers=headers)

    @task(2)
    def create_order(self):
        headers = self._get_headers()
        self.client.post("/api/orders/", json={
            "items": [
                {"product_id": 1, "quantity": 2},
                {"product_id": 2, "quantity": 1}
            ]
        }, headers=headers)

    def _get_headers(self):
        if self.token:
            return {"Authorization": f"Bearer {self.token}"}
        return {}
