ID |  RBT-001  | 
---|-----------|
DESCRIPTION  |  Verify the correct response and token creation with valid information  |
INFORMATION USED  |  USER: admin PASSWORD: password123/ ENDPOINT: /auth  |
STEPS  |  1. Open Postman.  2. Select the POST method. 3. Enter the /auth endpoint. 4. Add the valid credentials to the request body. 5. Send the request.
EXPECTED RESULT  |  200 OK , Body: token
ACTUAL RESULTS  |  200OK , Body: token
STATUS  |  PASS
VERSION  |  Postman : 12.22.11-260807-1732

