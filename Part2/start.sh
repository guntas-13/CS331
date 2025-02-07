#!/bin/bash

# Check if arguments are provided
if [ $# -ne 2 ]; then
    echo "Usage: $0 <python_script> <number_of_times>"
    exit 1
fi

PYTHON_SCRIPT=$1
NUM_RUNS=$(echo "$2" | tr -d '\r')  # Remove hidden carriage return characters

# Validate NUM_RUNS as a positive integer
if ! echo "$NUM_RUNS" | grep -qE '^[0-9]+$' || [ "$NUM_RUNS" -le 0 ]; then
    echo "Error: Number of times must be a positive integer!"
    exit 1
fi

echo "Running '$PYTHON_SCRIPT' $NUM_RUNS times concurrently..."

# Use gdate for high-precision timing on macOS
if command -v gdate &> /dev/null; then
    DATE_CMD="gdate"
else
    DATE_CMD="date"
    echo "Warning: gdate not found. Timing precision may be low. Install coreutils using: brew install coreutils"
fi

START_TIME=$($DATE_CMD +%s.%N)  # Capture start time

# Run the Python script concurrently the specified number of times
for ((i=1; i<=NUM_RUNS; i++)); do
    echo "Starting instance #$i..."
    python3 "$PYTHON_SCRIPT" &  # Run in the background
done

wait  # Wait for all background jobs to finish

END_TIME=$($DATE_CMD +%s.%N)  # Capture end time

# Calculate total execution time
TOTAL_TIME=$(echo "$END_TIME - $START_TIME" | bc)
AVERAGE_TIME=$(echo "scale=6; $TOTAL_TIME / $NUM_RUNS" | bc)

echo "Total Execution Time: $TOTAL_TIME seconds"
echo "Average Execution Time per script: $AVERAGE_TIME seconds"