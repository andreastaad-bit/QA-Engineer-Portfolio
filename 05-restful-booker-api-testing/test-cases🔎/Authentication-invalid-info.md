| *FIELD*  |  *DETAILS*  |
|-----------|-------------|
|  *ID*  |  RBT-005  |
|  *DESCRIPTION*  |  Verify HTTP code and body response with invalid credentials  |
|  *INFORMATION USED*  |  USERNAME: `Andrea` PASSWROD: `Lolita123`  |
|  *STEPS*  |  1.Open Postman <br> 2.Select POST method <br> 3. Use `/auth`as endpoint <br> 4. Add invalid credentials to body <br> 4.Send request <br>  |
|  *EXPECTED RESULT*  |  HTTP 400 Bad request ,response body `Bad credentials` | 
|  *ACTUAL RESULTS*  |  HTTP 200 OK , response body `Bad credentials` |
|  *STATUS*  | FAILED  |
|  *VERSION*  |  Postman 12.22.11  |
