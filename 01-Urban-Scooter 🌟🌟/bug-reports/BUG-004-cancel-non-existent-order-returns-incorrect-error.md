# BUG-004: Cancelling a Non-Existent Order Returns an Incorrect Error Response

## Summary

When attempting to cancel an order using a tracking number that does not correspond to any existing order, the API returns an incorrect error response.

According to the expected behavior, the API should indicate that the order could not be found.

## Endpoint

```text
PUT /api/v1/orders/cancel
```

## Preconditions

* The order does not exist.
* The request contains a tracking number that is not associated with any existing order.

## Steps to Reproduce

1. Open Postman.
2. Create a `PUT` request to:

```text
PUT /api/v1/orders/cancel
```

3. In the request body, provide a tracking number that does not correspond to any existing order.
4. Send the request.
5. Verify the API response.

## Expected Result

The API should return:

```text
HTTP/1.1 404 Not Found
```

with the following message:

```json
{
  "message": "Order not found"
}
```

## Actual Result

The API returns:

```text
HTTP 400 Bad Request
```

with the following response:

```json
{
  "code": 400,
  "message": "Not enough data for search."
}
```

## Impact

The API does not return the expected response when a user attempts to cancel an order that does not exist.

Returning a `400 Bad Request` instead of a `404 Not Found` may make it more difficult for the client application to correctly distinguish between invalid request data and a resource that cannot be found.

## Testing Tools

* Postman
* Jira

## Defect Tracking

The original defect was identified and documented in Jira during the API testing process.
