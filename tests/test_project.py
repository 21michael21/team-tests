import pytest
from allure import title, description, feature, story, severity
from allure_commons.types import Severity
from utils.mock_responses import mock_project_response, mock_project_error


@feature("Проекты")
@story("Создание проекта")
class TestProject:
    @title("Успешное создание проекта (мокирование)")
    @description("Проверяет, что проект успешно создается с валидными данными.")
    @severity(Severity.CRITICAL)
    def test_create_project_success(
        self, teamcity_client, data_generator, mock_requests
    ):
        # Arrange
        project_data = data_generator.generate_project_data()
        mock_url = f"{teamcity_client.base_url}/app/rest/projects"
        project_response = mock_project_response(project_data)
        mock_requests.post(
            mock_url,
            json=project_response["json"],
            status_code=project_response["status_code"],
        )

        # Act
        response = teamcity_client.create_project(project_data)

        # Assert
        assert response.status_code == 200
        assert response.json() == project_response["json"]

    @title("Создание проекта с дублирующимся ID (мокирование)")
    @description("Проверяет, что создание проекта с существующим ID вызывает ошибку.")
    @severity(Severity.NORMAL)
    def test_create_project_duplicate_id(
        self, teamcity_client, data_generator, mock_requests
    ):
        # Arrange
        project_data = data_generator.generate_project_data()
        mock_url = f"{teamcity_client.base_url}/app/rest/projects"
        error_response = mock_project_error(
            "Project ID already exists", status_code=409
        )
        mock_requests.post(
            mock_url,
            json=error_response["json"],
            status_code=error_response["status_code"],
        )

        # Act
        response = teamcity_client.create_project(project_data)

        # Assert
        assert response.status_code == 409
        assert "error" in response.json()

    @title("Создание проекта с невалидными данными (мокирование)")
    @description("Проверяет, что создание проекта с пустым именем вызывает ошибку.")
    @severity(Severity.NORMAL)
    @pytest.mark.parametrize(
        "invalid_data",
        [
            {"id": "InvalidProject", "name": "", "description": "Invalid"},
            {"id": "", "name": "Invalid Project", "description": "Invalid"},
        ],
    )
    def test_create_project_invalid_data(
        self, teamcity_client, invalid_data, mock_requests
    ):
        # Arrange
        mock_url = f"{teamcity_client.base_url}/app/rest/projects"
        error_response = mock_project_error(
            "Invalid project data", status_code=400
        ) 
        mock_requests.post(
            mock_url,
            json=error_response["json"],
            status_code=error_response["status_code"],
        )

        # Act
        response = teamcity_client.create_project(invalid_data)

        # Assert
        assert response.status_code == 400
        assert "error" in response.json()
