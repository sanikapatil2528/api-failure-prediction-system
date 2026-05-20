# API Failure Prediction System

This project simulates API/system behavior under increasing load and aims to predict failures before crashes occur using machine learning.

## Current Features

- Synthetic system metric generation
- Cascading degradation simulation
- Failure condition modeling
- Real-time metric visualization
- Predictive future-failure labeling
- ML-ready dataset generation

## Simulation Pipeline

requests → CPU usage → latency → errors → system failure

## Assumptions

- 1 simulation step = 1 monitoring minute
- Current prediction horizon = 5 minutes before failure