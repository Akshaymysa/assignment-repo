import pytest
from imp import reload as reload_module
from main import app 
def test_main():
    response = app.test_client().get('/hello')

    assert response.status_code == 200
