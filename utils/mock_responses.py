def mock_project_response(project_data, status_code=200):
    """Мокированный ответ для создания/получения проекта."""
    return {
        "status_code": status_code,
        "json": {
            "id": project_data["id"],
            "name": project_data["name"],
            "description": project_data["description"]
        }
    }

def mock_project_error(error_message, status_code=400):
    """Мокированный ответ для ошибки проекта."""
    return {
        "status_code": status_code,
        "json": {"error": error_message}
    }

def mock_role_response(role_data, status_code=200):
    """Мокированный ответ для назначения роли."""
    return {
        "status_code": status_code,
        "json": {
            "roleId": role_data["roleId"],
            "scope": role_data["scope"]
        }
    }

def mock_access_response(permissions, status_code=200):
    """Мокированный ответ для проверки доступа."""
    return {
        "status_code": status_code,
        "json": {"permissions": permissions}
    }

def mock_access_error(error_message, status_code=403):
    """Мокированный ответ для ошибки доступа."""
    return {
        "status_code": status_code,
        "json": {"error": error_message}
    }