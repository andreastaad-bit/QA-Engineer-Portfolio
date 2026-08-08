
|  *FIELD*  |  *DETAILS*  |
|------------|----------|
|  *ID*  |  RBT-004  |
|  *DESCRIPTION*  |  Update the information on a reservation previously created  |
|  *INFORMATION USED*  |  {    "firstname": `"Ana"`, <br> "lastname": `"Guerra"`,<br> "totalprice": `200`,<br>  "depositpaid": `true`,<br> "bookingdates": <br> "checkin": `"2026-08-10"`,<br>  "checkout": `"2026-08-30"` <br><br>"additionalneeds": `"Breakfast"`} <br>
|  *STEPS*  |  1.Open Postman <br> 2.Selet PUT method <br> 3.Enter `/bookin/` and `booking ID`as endpoint <br> 4.Enter information given as body to be updated <br> 5.Send request <br>
|  *EXPECTED RESULTS*  |  HTTP 200 OK with body in response updated wiht new info  |
|  *ACTUAL RESULTS*  | HTTP 400 BAD REQUEST , no body in response 
|  *STATUS*  |  FAILED  |
|  *VERSION*  |  Postman 12.22.11  |
