|  *FIELD*  |  *DETAILS*  |
|------------|------------|
|  *ID*  |  RBT-006  |
|  *DESCRIPTION*  |  Verify HTTP code and body response when sending an empty request  |
|  *INFORMATION USED*  |  Empty  |
|  *STEPS*  |  1.Open Postman <br> 2.Select POST method <br> 3.Use `/booking` as endpoint <br> 4.Leave body empty <br> 5.Send request <br>
|  *EXPECTED RESULT*  |  HTTP 400 Bad request, no body  |
|  *ACTUAL RESULTS*  |  HTTP 500 Internal error, no body  |
|  *STATUS*  |  [FAIL](https://antripleten26.atlassian.net/browse/RB-4)  |
|  *VERSION*  |  Postman 12.22.11  |
