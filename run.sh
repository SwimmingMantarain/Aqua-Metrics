#!/bin/bash

# Start the backend (FastAPI)
echo "Starting FastAPI backend..."
cd backend
source venv/bin/activate
uvicorn app:app --reload &
backend_pid=$!
cd ..

# Start the frontend
echo "Starting the frontend..."
cd frontend
# Open TailwindCSS build process if necessary
npm run tailwind &
frontend_pid=$!
cd ..

# Log output
echo "Backend PID: $backend_pid"
echo "Frontend PID: $frontend_pid"

# Wait for user to stop the processes
trap "kill $backend_pid $frontend_pid; exit 0" SIGINT
wait
