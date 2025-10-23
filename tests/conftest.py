"""
Pytest configuration and shared fixtures for the Mergington High School Activities API tests.
"""

import pytest
from fastapi.testclient import TestClient
from src.app import app, activities
import copy


@pytest.fixture(scope="function")
def client():
    """Create a test client for the FastAPI app."""
    return TestClient(app)


@pytest.fixture(scope="function")
def reset_activities():
    """
    Reset activities data before each test to ensure clean state.
    This fixture automatically restores the original activities data after each test.
    """
    # Store original activities
    original_activities = copy.deepcopy(activities)
    
    yield
    
    # Restore original activities after test
    activities.clear()
    activities.update(original_activities)