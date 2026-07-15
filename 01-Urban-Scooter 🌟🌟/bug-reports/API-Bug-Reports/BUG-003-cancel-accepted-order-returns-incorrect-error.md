# BUG-003: Cancelling an Accepted Order Returns an Incorrect Error Response

## Summary

When attempting to cancel an order after it has already been accepted by a courier, the API returns an incorrect error response.

According to the expected business logic, the order should be considered as being processed and the API should return a `409 Conflict` response.

## Endpoint

```text
PUT /api/v1/orders/cancel
```

## Preconditions

* An order has been successfully created.
* The order has been accepted by a courier through the application.

## Steps to Reproduce

1. Create a new order using Postman.
2. Accept the order using the application through the emulator.
3. Attempt to cancel the order using the `PUT` request to:

```text
PUT /api/v1/orders/cancel
```

4. Verify the API response.

## Expected Result

The API should return:

```json
{
  "message": "The order is being processed"
}
```

with the following status code:

```text
HTTP/1.1 409 Conflict
```

## Actual Result

The API returns:

```json
{
  "code": 400,
  "message": "Not enough data for search."
}
```

with a:

```text
HTTP 400 Bad Request
```

## Impact

The API does not return the expected response for an order that has already been accepted and is currently being processed.

This may lead to inconsistent error handling and may prevent the client application from correctly informing the user that the order cannot be cancelled because it is already in progress.

## Testing Tools

* Postman
* Emulator
* Jira

## Defect Tracking

The original defect was identified and documented in Jira during the API testing process.
