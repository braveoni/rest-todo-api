import requests
from urllib.parse import urljoin
from requests.api import delete
from requests.auth import HTTPBasicAuth


class Client:
    def __init__(self, username, password) -> None:
        self.url = "http://127.0.0.1:5000/"
        self.username = username
        self.password = password

        requests.post(urljoin(self.url, 'user'), auth=(self.username, self.password))

    def get_todo(self):
        return requests.get(urljoin(self.url, 'todo'), auth=(self.username, self.password)).json()

    def add_task(self, task_name):
        return requests.post(urljoin(self.url, 'todo'), auth=(self.username, self.password), data={'task_name': task_name}).json()
    
    def delete_task(self, task_id):
        return requests.delete(urljoin(urljoin(self.url, '/todo/'), str(task_id)), auth=(self.username, self.password)).json()
    
    def update_task(self, task_id, value: bool):
        requests.put(urljoin(urljoin(self.url, '/todo/'), str(task_id)), auth=(self.username, self.password), data={'task_status': str(value)}).json()

c = Client('admin', 'root')
print(c.get_todo())
# print(c.delete_task(6))
print(c.get_todo())
print(c.update_task(1, False))
print(c.get_todo())
print(c.add_task('test_client'))
print(c.get_todo())
