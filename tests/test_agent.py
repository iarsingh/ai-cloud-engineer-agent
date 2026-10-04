from fastapi.testclient import TestClient
from cloudeng.main import app

client = TestClient(app)


def test_runs_and_refuses_a_write():
    payload = client.post("/agent/run", json={"goal": 'plan a gke cluster', **{'payload': {'wanted': ['google_container_cluster']}}}).json()
    assert payload["refused"] is False
    assert payload["applied"] is False
    assert "google_container_cluster" in payload["resources"]
    refused = client.post("/agent/run", json={"goal": 'apply terraform now'}).json()
    assert refused["refused"] is True
