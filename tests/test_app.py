from fastapi.testclient import TestClient

from src.app import app, activities

client = TestClient(app)


def test_student_cannot_register_twice_for_same_activity():
    activity_name = "Chess Club"
    email = "duplicate.student@mergington.edu"

    activities[activity_name]["participants"] = [email]

    response = client.post(
        f"/activities/{activity_name}/signup",
        params={"email": email},
    )

    assert response.status_code == 400
    assert response.json() == {"detail": "Student is already signed up for this activity"}
    assert activities[activity_name]["participants"] == [email]
