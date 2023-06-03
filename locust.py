from locust import  constant, HttpUser, task


class azDevopOps(HttpUser):
    weight = 1
    wait_time = constant(1)
    host = "https://azmlmoyounus.azurewebsites.net"

    @task
    def get_default_site(self):
        response = self.client.get("/")
        print(response.status_code)
        print(response.headers)
        print(response.text)
        