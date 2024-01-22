# DevFusion API Reference

Welcome to the DevFusion API reference. This document provides information on the backend API endpoints available in the DevFusion app, which has been enhanced with UI elements from BloopAI and upgraded to use the GPT-4 Turbo AI model.

## Base URL

All API requests are made to the following base URL:

```
API_BASE_URL
```

## Endpoints

### User Management

- **GET** `/api/users/`
  - Retrieves a list of all users.
  - Response schema: `UserSchema[]`

- **POST** `/api/users/`
  - Creates a new user.
  - Request schema: `UserSchema`
  - Response schema: `UserSchema`

- **GET** `/api/users/{id}/`
  - Retrieves a user by ID.
  - Response schema: `UserSchema`

- **PUT** `/api/users/{id}/`
  - Updates a user by ID.
  - Request schema: `UserSchema`
  - Response schema: `UserSchema`

- **DELETE** `/api/users/{id}/`
  - Deletes a user by ID.

### Feedback Submission

- **POST** `/api/feedback/`
  - Submits user feedback.
  - Request schema: `FeedbackSchema`
  - Response: `MODEL_UPDATE_SUCCESS` on success.

### AI Model Interaction

- **POST** `/api/model/query/`
  - Sends a query to the GPT-4 Turbo model.
  - Request schema: `ModelResponseSchema`
  - Response schema: `ModelResponseSchema`

## Schemas

### UserSchema

```json
{
  "id": "UUID",
  "username": "string",
  "email": "string",
  "created_at": "datetime",
  "updated_at": "datetime"
}
```

### FeedbackSchema

```json
{
  "user_id": "UUID",
  "content": "string",
  "submitted_at": "datetime"
}
```

### ModelResponseSchema

```json
{
  "query": "string",
  "response": "string",
  "context": "string",
  "created_at": "datetime"
}
```

## Status Messages

- `MODEL_UPDATE_SUCCESS`: Returned when the AI model has been successfully updated.
- `UI_INTEGRATION_COMPLETE`: Returned when UI components have been successfully integrated.
- `DEPLOYMENT_STATUS`: Used to communicate the status of the application deployment.

For more detailed examples and usage, please refer to the [User Guide](docs/user_guide.md) and [Installation Guide](docs/installation_guide.md).

## Feedback

To provide feedback on the API or report any issues, please use the feedback submission endpoint or contact our support team.

Thank you for using DevFusion. We hope this API reference will help you integrate and build on top of our platform effectively.