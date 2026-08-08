|  *FIELD*  |  *DETAILS*  |
|------------|------------|
|  *ID*  |  RBT-006  |
|  *DESCRIPTION*  |  Verify de HTTP code and body response with no information in body request  |
|  *INFORMATION USED*  |  Empty  |
|  *STEPS*  |  1.Open Postman <br> 2.Select POST method <br> 3.Use `/booking` as endpoint <br> 4.Leave body empty <br> 5.Send request <br>
|  *EXPECTED RESULT*  |  HTTP 400 Bad request, no body  |
|  *ACTUAL RESULTS*  |  HTTP 500 Internal error, no body  |
|  *STATUS*  |  FAILED  |
|  *VERSION*  |  Postman 12.22.11  |
