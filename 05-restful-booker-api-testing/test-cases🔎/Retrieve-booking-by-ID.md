|  *FIELD*  |  *DETAILS*  |
|-----------|-------------|
|  *ID*  |  RBT-010  |
|  *DESCRIPTION*  |  Verify you can retrieve the correct information corresponding a booking  |
|  *INFORMATION USED*  |  ENDPOINT:`/BOOKING` <br> {"firstname" : `"Johan"`,<br>"lastname" : `"Velazquez"`,<br>"totalprice" : `123`,<br> "depositpaid" : `true`,<br>"bookingdates" : {"checkin" : `"2026-01-01"`,<br>"checkout" : `"2026-01-15"` },<br>"additionalneeds" : `"Extra pillows"`}<br>
|  *STEPS*  |  1.Open Postman <br> 2.Select POST method <br> 3.Add given information in the body  <br> 4.Send request <br> 5.Save ID <br> 6.Select GET method <br> 7.Use `/booking/id`make sure to use id corresponding to the booking you just created <br> 8.Verify response body and code  |
|  *EXPECTED RESULTS*  |  200 OK retrieving the information with matching information on the response body  | 
|  *ACTUAL RESULTS*  |  200 OK, information in bod response matches the one from the created booking  |
|  *STATUS*  |  PASS  |
|  *VERSION*  |  Postman 12.22.11
