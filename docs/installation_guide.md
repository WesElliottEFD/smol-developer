# DevFusion Installation Guide

Welcome to the installation guide for DevFusion. This document will guide you through the process of setting up DevFusion on your local machine.

## Prerequisites

Before you begin, ensure you have the following installed:
- Node.js (LTS version recommended)
- npm (comes with Node.js)
- Python 3.8 or higher
- pip (Python package installer)

## Cloning the Repository

To get started, clone the DevFusion repository to your local machine:

```
git clone https://github.com/your-username/DevFusion.git
cd DevFusion
```

## Backend Setup

1. Navigate to the backend directory:

```
cd src/backend
```

2. Create a virtual environment:

```
python -m venv venv
```

3. Activate the virtual environment:

- On Windows:

```
venv\Scripts\activate
```

- On macOS and Linux:

```
source venv/bin/activate
```

4. Install the required Python packages:

```
pip install -r requirements.txt
```

5. Run the backend server:

```
python manage.py runserver
```

## Frontend Setup

1. Navigate to the frontend directory from the root of the project:

```
cd src/frontend
```

2. Install the required npm packages:

```
npm install
```

3. Start the React development server:

```
npm start
```

The frontend should now be running and accessible at `http://localhost:3000`.

## Integrating UI Components from BloopAI

Ensure you have the BloopAI components cloned from the BloopAI repository:

```
git clone https://github.com/BloopAI/bloop.git
```

Follow the instructions in `src/utils/integrateUIComponents.js` to integrate the UI components from BloopAI into DevFusion.

## Upgrading to GPT-4 Turbo

The DevFusion app uses GPT-4 Turbo for AI functionalities. Ensure that the AI model is correctly set up by following the instructions in `src/utils/upgradeToGPT4Turbo.js`.

## Testing and Validation

Run the test suite to ensure that all components are functioning correctly:

```
cd src/tests
npm test
```

## Deployment

To deploy DevFusion, follow the deployment instructions in `scripts/deploy.sh`.

## Post-Deployment Monitoring

After deployment, monitor the application using the script `scripts/post_deploy_monitoring.sh`.

## Collecting User Feedback

Set up a feedback loop using the script `scripts/feedback_collector.py` to collect user feedback for continuous improvement.

For more detailed information on each step, please refer to the respective documentation files in the `docs/` directory.

Thank you for installing DevFusion. We hope you enjoy using the app!