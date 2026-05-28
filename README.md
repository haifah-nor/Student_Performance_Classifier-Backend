# EduLens Backend

FastAPI backend for the EduLens student performance predictor.

## Features
- Predict endpoint for student performance inference.
- Metrics endpoint exposing model evaluation details.
- CORS enabled for local frontend development.

## Setup
1. Create and activate a virtual environment.
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Start the API server:
   ```bash
   uvicorn app.main:app --reload
   ```

## API Endpoints
- `POST /predict` - Returns a pass/fail prediction and probabilities.
- `GET /metrics` - Returns model performance metrics and class report.

## Development Notes
- The app entry point is `app.main:app`.
- Local development uses the default FastAPI reload server.
- Adjust `VITE_API_URL` in the frontend if the backend runs on a non-default host or port.
