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
    assert b"ACEest FUNCTIONAL FITNESS SYSTEM" in response.data

def test_valid_program_endpoint(client):
    """Validates retrieval of existing muscle gain configurations."""
    response = client.get('/api/programs/muscle_gain')
    assert response.status_code == 200
    json_data = response.get_json()
    assert json_data['name'] == "Muscle Gain (MG)"
    # FIXED: Updated string structure matching the Version 2 app.py settings
    assert "Target: ~3200 kcal" in json_data['diet']

def test_invalid_program_endpoint(client):
    """Validates proper application handling of unmapped keys (404 error)."""
    response = client.get('/api/programs/crossfit_elite')
    assert response.status_code == 404

def test_dynamic_calorie_calculation(client):
    """Validates that math calculations return accurate metrics via endpoints."""
    payload = {"weight": 80.0, "program": "muscle_gain"}
    response = client.post('/api/calculate', json=payload)
    assert response.status_code == 200
    assert response.get_json()['estimated_calories'] == 2800  # 80kg * 35 factor

def test_invalid_calculation_parameters(client):
    """Ensures bad payload entry inputs are stopped gracefully with 400."""
    response = client.post('/api/calculate', json={"weight": "invalid_string", "program": "fat_loss"})
    assert response.status_code == 400
