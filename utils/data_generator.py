from faker import Faker
import uuid

class DataGenerator:
    def __init__(self):
        self.faker = Faker()

    def generate_project_data(self, project_id=None, name=None, description=None):
        """Генерация данных для проекта."""
        return {
            "id": project_id or f"Project_{uuid.uuid4().hex[:8]}",
            "name": name or self.faker.company(),
            "description": description or self.faker.sentence()
        }

    def generate_role_data(self, role_id, project_id):
        """Генерация данных для назначения роли."""
        return {
            "roleId": role_id,
            "scope": f"project:{project_id}"
        }