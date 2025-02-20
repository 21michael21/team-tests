import pytest
from allure import title, description, feature, story, severity
from allure_commons.types import Severity
from utils.mock_responses import (
    mock_role_response,
    mock_access_response,
    mock_access_error,
)


@feature("Роли и права")
@story("Назначение и проверка ролей")
class TestRoles:
    @title("Успешное назначение роли пользователю (мокирование)")
    @description("Проверяет, что роль успешно назначается пользователю.")
    @severity(Severity.CRITICAL)
    def test_assign_role_success(self, teamcity_client, data_generator, mock_requests):
        # Arrange
        project_data = data_generator.generate_project_data()
        user_id = "user1"
        role_data = data_generator.generate_role_data(
            role_id="PROJECT_ADMIN", project_id=project_data["id"]
        )
        mock_url = f"{teamcity_client.base_url}/app/rest/users/id:{user_id}/roles"
        role_response = mock_role_response(role_data)
        mock_requests.post(
            mock_url,
            json=role_response["json"],
            status_code=role_response["status_code"],
        )

        # Act
        response = teamcity_client.assign_role(user_id, role_data)

        # Assert
        assert response.status_code == 200
        assert response.json() == role_response["json"]

    @title("Проверка доступа после назначения роли (мокирование)")
    @description("Проверяет, что пользователь с ролью имеет доступ к проекту.")
    @severity(Severity.NORMAL)
    def test_check_access_with_role(
        self, teamcity_client, data_generator, mock_requests
    ):
        # Arrange
        project_data = data_generator.generate_project_data()
        user_id = "user1"
        role_data = data_generator.generate_role_data(
            role_id="PROJECT_ADMIN", project_id=project_data["id"]
        )
        mock_role_url = f"{teamcity_client.base_url}/app/rest/users/id:{user_id}/roles"
        role_response = mock_role_response(
            role_data
        )  # Изменили mock_role_response на role_response
        mock_requests.post(
            mock_role_url,
            json=role_response["json"],
            status_code=role_response["status_code"],
        )

        mock_access_url = (
            f"{teamcity_client.base_url}/app/rest/users/id:{user_id}/permissions"
        )
        access_response = mock_access_response(
            permissions=["editProject"]
        )  
        mock_requests.get(
            mock_access_url,
            json=access_response["json"],
            status_code=access_response["status_code"],
        )

        # Act
        response = teamcity_client.check_access(
            user_id, action="editProject", project_id=project_data["id"]
        )

        # Assert
        assert response.status_code == 200
        assert "editProject" in response.json().get("permissions", [])

    @title("Попытка доступа без роли (мокирование)")
    @description("Проверяет, что пользователь без роли не имеет доступа к проекту.")
    @severity(Severity.NORMAL)
    def test_check_access_without_role(
        self, teamcity_client, data_generator, mock_requests
    ):
        # Arrange
        project_data = data_generator.generate_project_data()
        user_id = "user2"
        mock_access_url = (
            f"{teamcity_client.base_url}/app/rest/users/id:{user_id}/permissions"
        )
        access_response = mock_access_error(
            "Access denied", status_code=403
        )  
        mock_requests.get(
            mock_access_url,
            json=access_response["json"],
            status_code=access_response["status_code"],
        )

        # Act
        response = teamcity_client.check_access(
            user_id, action="editProject", project_id=project_data["id"]
        )

        # Assert
        assert response.status_code == 403
        assert "error" in response.json()
