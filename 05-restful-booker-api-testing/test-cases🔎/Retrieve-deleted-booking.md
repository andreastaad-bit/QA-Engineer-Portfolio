|  *FIELD*  |  *DETAILS*  |
|----------|-------------|
|  *ID*  |  RBT-009  |
|  *DESCRIPTIONS*  |  Verify you can not retrieve a deleted booking  |
|  *INFORMATION USED*  |  ENDPOINT: `/booking/id` |
|  *PRE-CONDITIONS*  |  1.Have an auth token generated <br> 2.Create a booking and retrieve ID number <br>  |
|  *STEPS*  |  1.Open Postman <br> 2.Select DELETE method <br> 3.Use `/booking/id`as endpoint, make sure to use the id number of the booking you created before <br> 4.Send request <br> 4.Select GET method <br> 5.Use `/booking/id`use the ID belonging to the booking you just deleted <br> 6. Send request <br> 7.Verify code and body on response  |
|  *EXPECTED RESULTS*  |  HTTP 404 NOT FOUND, no response  body  |
|  *ACTUAL RESULTS*  |  HTTP 404 NOT FOUND, no response body  |
|  *STATUS*  |  PASS  |
|  *VERSION*  |  Postman 12.22.11  |
