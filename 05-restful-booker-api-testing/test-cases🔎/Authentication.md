| FIELD | DETAILS |
|---|---|
| **ID** | RBT-001 |
| **DESCRIPTION** | Verify successful authentication and token generation with valid credentials |
| **INFORMATION USED** | • Username: `admin`<br>• Password: `password123`<br>• Endpoint: `POST /auth` |
| **STEPS** | 1. Open Postman.<br>2. Select `POST` method.<br>3. Enter `/auth` endpoint.<br>4. Add valid credentials to the request body.<br>5. Send the request. |
| **EXPECTED RESULT** | HTTP `200 OK` response with a `token` property in the response body. |
| **ACTUAL RESULT** | HTTP `200 OK` response received with a `token` property. |
| **STATUS** | PASS |
| **VERSION** | Postman 12.22.11 |
