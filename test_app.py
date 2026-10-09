import pytest
from app import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_home_page_status(client):
    """Validates the dashboard UI base route is accessible."""
    response = client.get('/')
    assert response.status_code == 200
    assert b"ACEest FUNCTIONAL FITNESS" in response.data

def test_valid_program_endpoint(client):
    """Validates retrieval of existing muscle gain configurations."""
    response = client.get('/api/programs/muscle_gain')
    assert response.status_code == 200
    json_data = response.get_json()
    assert json_data['name'] == "Muscle Gain (MG)"
    assert "Target: 3,200 kcal" in json_data['diet']

def test_invalid_program_endpoint(client):
    """Validates proper application handling of unmapped keys (404 error)."""
    response = client.get('/api/programs/crossfit_elite')
    assert response.status_code == 404

def test_metrics_endpoint(client):
    """Validates internal capacity metrics logic configuration."""
    response = client.get('/api/metrics')
    assert response.status_code == 200
    assert response.get_json()['capacity'] == 150
