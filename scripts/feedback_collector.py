```python
import json
import requests
from datetime import datetime

# Define the base URL for backend API calls
API_BASE_URL = "http://localhost:8000/api"

# Define the endpoint for submitting feedback
FEEDBACK_ENDPOINT = f"{API_BASE_URL}/feedback/"

# Define the data structure for user feedback
FeedbackSchema = {
    "user_id": "",
    "feedback": "",
    "timestamp": "",
    "app_version": ""
}

def collect_user_feedback(user_id, feedback, app_version):
    """
    Collects user feedback and sends it to the backend API.

    :param user_id: The ID of the user submitting the feedback.
    :param feedback: The content of the feedback.
    :param app_version: The version of the app the feedback is for.
    """
    feedback_data = FeedbackSchema.copy()
    feedback_data['user_id'] = user_id
    feedback_data['feedback'] = feedback
    feedback_data['timestamp'] = datetime.now().isoformat()
    feedback_data['app_version'] = app_version

    response = requests.post(FEEDBACK_ENDPOINT, json=feedback_data)
    return response.status_code, response.json()

def main():
    # Example usage:
    # Collect feedback from a user and send it to the backend.
    user_id = "12345"
    feedback = "I really enjoy the new UI components!"
    app_version = "2.0.0"

    status_code, response = collect_user_feedback(user_id, feedback, app_version)
    if status_code == 200:
        print("Feedback submitted successfully.")
    else:
        print(f"Failed to submit feedback. Status code: {status_code}, Response: {response}")

if __name__ == "__main__":
    main()
```