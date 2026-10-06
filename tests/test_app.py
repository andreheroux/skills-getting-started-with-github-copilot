from fastapi.testclient import TestClient

from src.app import app, activities

client = TestClient(app)


def test_student_cannot_register_twice_for_same_activity():
    # Arrange
    activity_name = "Chess Club"
    email = "duplicate.student@mergington.edu"
    activities[activity_name]["participants"] = [email]

    # Act
    response = client.post(
        f"/activities/{activity_name}/signup",
        params={"email": email},
    )

    # Assert
    assert response.status_code == 400
    assert response.json() == {"detail": "Student is already signed up for this activity"}
    assert activities[activity_name]["participants"] == [email]


def test_student_can_unregister_from_activity():
    # Arrange
    activity_name = "Chess Club"
    email = "student.to.remove@mergington.edu"
    activities[activity_name]["participants"] = [email]

    # Act
    response = client.delete(
        f"/activities/{activity_name}/signup",
        params={"email": email},
    )

    # Assert
    assert response.status_code == 200
    assert response.json() == {"message": f"Removed {email} from {activity_name}"}
    assert activities[activity_name]["participants"] == []
