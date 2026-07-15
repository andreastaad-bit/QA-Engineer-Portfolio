# BUG-001: Associated Orders Remain in the Database After Courier Deletion

## Summary

When a courier is deleted through the `DELETE` API request, the API returns a `200 OK` status code and the courier is successfully removed from the `Courier` table. However, the orders associated with the deleted courier remain in the `Orders` table.

## Endpoint

```text
DELETE /api/v1/courier/:id
```

## Preconditions

* A courier has been created through the API.
* An order has been created and assigned to the courier.

## Steps to Reproduce

1. Create a courier using a `POST` request to:

```text
POST /api/v1/courier
```

2. Create an order and assign it to the courier.
3. Send a `DELETE` request to:

```text
DELETE /api/v1/courier/:id
```

4. Verify the courier table in the database.
5. Verify the orders table in the database.

## Expected Result

After deleting the courier, all orders associated with that courier should also be deleted from the `Orders` table.

## Actual Result

The courier is successfully removed from the `Courier` table. However, the order associated with the deleted courier remains in the `Orders` table.

## API Response

```text
HTTP 200 OK
```

The API returns a successful response, but the associated order remains in the database.

## Impact

This issue may lead to orphaned orders and inconsistent data between the `Courier` and `Orders` tables.

## Testing Tools

* Postman
* Remote terminal
* Database validation

## Defect Tracking

The original defect was identified and documented in Jira during the API testing process.
