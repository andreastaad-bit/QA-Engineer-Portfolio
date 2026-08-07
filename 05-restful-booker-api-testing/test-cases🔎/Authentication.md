ID |  RBT-001  | 
---|-----------|
DESCRIPTION  |  Verify the correct response and token creation with valid information  |
INFORMATION USED  |  USER: admin PASSWORD: password123/ ENDPOINT: /auth  |
STEPS  |  1. Open Postman.  2. Select the POST method. 3. Enter the /auth endpoint. 4. Add the valid credentials to the request body. 5. Send the request.
EXPECTED RESULT  | HTTP 200 OK response with a token property in the response body.
ACTUAL RESULTS  | HTTP 200 OK response with a token property in the response body.
STATUS  |  PASS
VERSION  |  Postman : 12.22.11-260807-1732

