# Simple-Task-Management

## Authentication:

To authenticate, provide the **username** and **password** of an existing user in the database to get the **access** and **refresh tokens**.

```
curl -X POST -H "Content-Type: application/json" -d "{\"username\": \"YOUR_USER_NAME_HERE\", \"password\": \"YOUR_PASSWORD_HERE\"}" http://127.0.0.1:8000/api/token/
```

This will return the **access** and **refresh** tokens. Copy the **access token** and use it in the following request for example to get all the tasks.
```
curl -X GET -H "Authorization: Bearer ACCESS_TOKEN_HERE" http://127.0.0.1:8000/api/tasks/
```

### Refreshing the Access Token (If It Expires):
If the access token expires, use the refresh token to get a new access token:

```
curl -X POST -H "Content-Type: application/json" -d "{\"refresh\": \"your-refresh-token-here\"}" http://127.0.0.1:8000/api/token/refresh/
```


#### Get All Tasks:
```
curl -X GET -H "Authorization: Bearer ACCESS_TOKEN_HERE" http://127.0.0.1:8000/api/tasks/
```
#### Create a Task (POST):
```
curl -X POST -H "Authorization: Bearer ACCESS_TOKEN_HERE" -d "{\"title\": \"TEST_TITLE\", \"description\": \"TEST_DESCRIPTION\", \"is_completed\": false}" http://127.0.0.1:8000/api/tasks/
```

#### Get a Specific Task (GET):
Replace `{id}` with the task ID:

```
curl -X GET -H "Authorization: Bearer ACCESS_TOKEN_HERE" http://127.0.0.1:8000/api/tasks/{id}/
```

#### Update a Task (PUT):
Replace `{id}` with the task ID:

```
curl -X PUT -H "Authorization: Bearer ACCESS_TOKEN_HERE" -d "{\"title\": \"Updated Task\", \"description\": \"Updated Description\", \"is_completed\": true}" http://127.0.0.1:8000/api/tasks/{id}/
```

#### Delete a Task (DELETE):
Replace `{id}` with the task ID:

```
curl -X DELETE -H "Authorization: Bearer ACCESS_TOKEN_HERE" http://127.0.0.1:8000/api/tasks/{id}/
```


