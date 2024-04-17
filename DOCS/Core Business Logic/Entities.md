# Core Business Logic (Entities)

The Core Business Logic of our application, which is focused on enhancing user engagement at events, is encapsulated in our Entities. These Entities are the heart of our application, representing the domain objects that are central to the business logic.

## Entity Definitions

Below are the primary entities of our application, along with their responsibilities and relationships to other entities.

### Event

- **Description**: Represents an event that users can engage with.
- **Attributes**:
  - `eventId`: A unique identifier for the event.
  - `eventName`: The name of the event.
  - `eventDescription`: A detailed description of the event.
  - `startTime`: The scheduled start time of the event.
  - `endTime`: The scheduled end time of the event.
- **Relationships**:
  - Associated with multiple `Session` entities.
  - Linked to `UserEngagement` to track engagement metrics.

### Session

- **Description**: Represents a specific session within an event.
- **Attributes**:
  - `sessionId`: A unique identifier for the session.
  - `sessionName`: The name of the session.
  - `presenter`: The individual or group presenting the session.
  - `sessionDescription`: A detailed description of the session.
- **Relationships**:
  - Belongs to one `Event`.
  - Linked to `UserEngagement` to track session-specific engagement.

### User

- **Description**: Represents a user attending the event.
- **Attributes**:
  - `userId`: A unique identifier for the user.
  - `userName`: The name of the user.
  - `userEmail`: The email address of the user.
- **Relationships**:
  - Engages with multiple `Event` and `Session` entities through `UserEngagement`.

### UserEngagement

- **Description**: Tracks user interactions and engagement with events and sessions.
- **Attributes**:
  - `engagementId`: A unique identifier for the engagement record.
  - `userId`: The identifier of the user engaged.
  - `eventId`: The identifier of the event engaged with.
  - `sessionId`: The identifier of the session engaged with (if applicable).
  - `engagementType`: The type of engagement (e.g., view, like, comment).
  - `engagementTimestamp`: The timestamp when the engagement occurred.
- **Relationships**:
  - Links `User` to `Event` and `Session`.

## Entity Relationships

The following diagram illustrates the relationships between the entities described above:

```
User -- UserEngagement -- Event
                         |
                         -- Session
```

Each `User` can have multiple `UserEngagement` records, each of which is associated with either an `Event` or a `Session`. Each `Event` can encompass multiple `Sessions`.

## Data Model Schema

For detailed schema definitions, please refer to the `DataModelSchema` in the `DOCS/Data Conversion and User Interface/InterfaceAdapters.md` file.

## Business Logic Functions

The core functions that operate on these entities are defined in the `BusinessLogicFunctions` section of the `DOCS/Business Processes/UseCases.md` file. These functions include operations such as creating and updating events, registering user engagement, and querying for event details.

## Conclusion

The entities described here form the foundation of our application's business logic. They are designed to be independent of the user interface, adhering to the principles of Clean Architecture. This separation allows for flexibility and maintainability as the application evolves.

For further details on how these entities interact with the rest of the application, please refer to the respective sections in the `DOCS` folder.