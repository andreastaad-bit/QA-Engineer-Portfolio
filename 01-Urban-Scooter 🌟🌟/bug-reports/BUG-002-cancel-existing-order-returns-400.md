# BUG-002: Cancelling an Existing Order Returns a 400 Bad Request

## Summary

When attempting to cancel an existing order using the `PUT` method, the API returns a `400 Bad Request` response instead of successfully cancelling the order.

## Endpoint

```text
PUT /api/v1/orders/cancel
```

## Preconditions

* An order has been successfully created.
* A valid `track` number is available for the order.

## Steps to Reproduce

1. Create a new order using Postman.
2. Copy the `track` number returned in the response.
3. Create a new `PUT` request using the following endpoint:

```text
PUT /api/v1/orders/cancel
```

4. Send the request using the `track` number associated with the existing order.
5. Verify the API response.

## Expected Result

The API should return a `200 OK` status code and successfully cancel the existing order.

## Actual Result

The API returns a `400 Bad Request` status code, and the order is not cancelled.

## Impact

Users may be unable to cancel valid existing orders through the API, preventing the expected order cancellation flow from functioning correctly.

## Testing Tools

* Postman
* API testing checklist
* Jira

## Defect Tracking

The original defect was identified and documented in Jira during the API testing process.
