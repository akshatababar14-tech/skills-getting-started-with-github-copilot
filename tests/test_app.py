from fastapi.testclient import TestClient

from src.app import app


def test_unregister_participant_removes_email_from_activity():
    client = TestClient(app)

    response = client.post('/activities/Chess Club/signup?email=student@example.com')
    assert response.status_code == 200

    remove_response = client.delete('/activities/Chess Club/unregister?email=student@example.com')
    assert remove_response.status_code == 200

    updated = client.get('/activities')
    assert 'student@example.com' not in updated.json()['Chess Club']['participants']
