from ...src.app import app


def test_post_create_task():
    with app.test_client() as test_client:
        response = test_client.post('/api/v1/task/create')
        assert response.status_code == 200

def test_get_create_task():
    with app.test_client() as test_client:
        response = test_client.get('/api/v1/task/10/10')
        assert response.status_code == 200