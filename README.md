# Simple-Task-Management

Get all tasks:
curl -X GET -H "Content-Type: application/json" http://127.0.0.1:8000/api/tasks/

Post:
curl -X POST -H "Content-Type: application/json" -d "{\"title\": \"TEST_TITLE\", \"description\": \"TEST_DESCRIPTION\", \"is_completed\": false}" http://127.0.0.1:8000/api/tasks/

Get a task:
curl -X GET -H "Content-Type: application/json" http://127.0.0.1:8000/api/tasks/{id}/

PUT/Delete a task:
curl -X PUT -H "Content-Type: application/json" -d "{\"title\": \"Updated Task\", \"description\": \"Updated Description\", \"is_completed\": true}" http://127.0.0.1:8000/api/tasks/{id}/
curl -X DELETE -H "Content-Type: application/json" http://127.0.0.1:8000/api/tasks/{id}/



