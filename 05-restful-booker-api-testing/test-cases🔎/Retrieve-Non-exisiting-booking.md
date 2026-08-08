1  *FIELD*  |  *DETAILS*  |
|-----------|-------------|
|  *ID*  |  RBT-008  |
|  *DESCRIPTION*  |  Verify status code and response when requesting information for a non existing booking ID  |
|  *INFORMATION USED*  |  ENDPOINT: `/booking/5678`  |
|  *STEPS*  |  1.Open Postman <br> 2.Select GET method <br> 3.Use `/bookig/5678`as endpoints 4.Send request <br> |
|  *EXPECTED RESULTS*  |  HTTP 404 NOT FOUND, no response body  |
|  *ACTUAL RESLUT*  |  HTTP 404 NOT FOUND, no response body  |
|  *STATUS*  |  PASS  |
|  *VERSION*  |  Postman 12.22.11  |
