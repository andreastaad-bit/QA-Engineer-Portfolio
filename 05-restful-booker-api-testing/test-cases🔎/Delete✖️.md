
|  *FIELD*  |  *DETAILS*  |
|-----------|-------------|
|  *ID*  |  RBT-003  |
|  *DESCRIPTION*  |  Verify correct HTTP code when deleting a booking  | 
|  *INFORMATION USED*  |  No body  |
|  *STEPS*  | 1.Open Postman <br> 2.Select DELETE method <br> 3.Enter `/booking/` `booking ID`as endpoints. <br> 4.Send request <br>
|  *EXPECTED RESULTS*  |  HTTP 200 OK with no body 
|  *ACTUAL RESULTS*  |  HTTP 201 CREATED 
|  *STATUS*  |  FAIL  |
|  *VERISON*  |  Postman 12.22.11
