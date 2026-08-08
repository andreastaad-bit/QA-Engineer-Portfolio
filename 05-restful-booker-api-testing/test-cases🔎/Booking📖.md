
|  FIELD  |  DETAILS
|---------|----------|
| *ID*  |  RBT-002  |
|  *DESCRIPTION*  |  *Create a booking with the information given. <br> *Obtain revervation ID <br>
|  *INFORMATION USED*  |  "firstname": `"Andrea"`,<br>"lastname": `"Guerra"`,<br>"totalprice": `1230`,<br> "depositpaid": `true`, <br>"bookingdates": { <br>"checkin": `"2026-08-01"`, <br>"checkout": `"2026-08-25"`<br> { "additionalneeds": `"Breakfast"` <b> }
|  *STEPS*  |  1. Open Postman <br> 2. Select POST method <br> 3.Enter `/booking} end point <br> 4. Add valid credentials to the request body. <br> 5. Send request
|  *EXPECTED RESULTS*  | HTTP 200 OK response with booking ID in the response body
|  *ACTUAL RESULTS*  |  HTTP 200 OK response with booking ID in the response body
|  *STATUS*  |  PASS
|  *VERSION*  |  Postman 12.22.11
