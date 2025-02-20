import requests
import yaml
from allure import step

class TeamCityClient:
    def __init__(self, config_path="config/config.yaml"):
        with open(config_path, "r") as f:
            config = yaml.safe_load(f)
        self.base_url = config["teamcity"]["base_url"]
        self.auth = (config["teamcity"]["username"], config["teamcity"]["password"])
        self.session = requests.Session()  # Используем сессию для мокирования

    @step("Создание проекта")
    def create_project(self, project_data):
        """Создание проекта (POST)."""
        url = f"{self.base_url}/app/rest/projects"
        headers = {"Content-Type": "application/json"}
        response = self.session.post(url, json=project_data, headers=headers, auth=self.auth)
        return response

    @step("Получение проекта по ID")
    def get_project_by_id(self, project_id):
        """Получение проекта по ID (GET)."""
        url = f"{self.base_url}/app/rest/projects/id:{project_id}"
        response = self.session.get(url, auth=self.auth)
        return response

    @step("Назначение роли пользователю")
    def assign_role(self, user_id, role_data):
        """Назначение роли пользователю (POST)."""
        url = f"{self.base_url}/app/rest/users/id:{user_id}/roles"
        headers = {"Content-Type": "application/json"}
        response = self.session.post(url, json=role_data, headers=headers, auth=self.auth)
        return response

    @step("Проверка доступа пользователя")
    def check_access(self, user_id, action, project_id):
        """Проверка доступа пользователя (GET)."""
        url = f"{self.base_url}/app/rest/users/id:{user_id}/permissions"
        response = self.session.get(url, auth=self.auth)
        return response