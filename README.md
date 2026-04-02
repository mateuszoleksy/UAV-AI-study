# UAV-AI-study
Repository for project AI for drones: navigation and communication

## AI for Drones: Communication & Navigation Resilience
### Project Overview

The goal of this project is to investigate the resilience of AI-based autonomous drone navigation systems against communication channel disturbances. Unlike traditional PID control, this system utilizes Behavior Cloning (BC) to mimic expert pilot behavior.

### Key Research Areas
- Behavior Cloning: Mapping position and velocity data to control decisions such as thrust, roll, pitch, and yaw.

- Latency Impact: Analyzing how data transfer delays between sensors and the AI "brain" cause oscillations.

- Signal Noise: Modeling signal degradation using real-world RSSI and Noise parameters from PX4 logs.

- Uncertainty Navigation: Testing if AI trained on "clean" data can recover during sudden connection loss.

### Methodology
- Data Acquisition: Collecting 20-50 high-quality .ulg flight logs from review.px4.io.

- Preprocessing: Extracting and synchronizing vehicle_local_position and actuator_motors tables.

- Model Training: Building a neural network regressor to predict control decisions from position and velocity data.

- Simulation: Integrating the model into the gym-pybullet-drones environment.

- Stress Testing: Running flights with artificial noise and latencies ranging from 50 ms to 500 ms.

### Performance Metrics
- MSE (Mean Squared Error): Average deviation from the planned trajectory.
- Jitter: Control "nervousness" based on motor RPM changes.
- Success Rate: Percentage of collision-free missions reaching the target.
- Inference Time: AI decision-making speed.

### Tech Stack

- Language: Python 3.10.
- Simulator: gym-pybullet-drones.
- AI/ML: PyTorch (MLP) or scikit-learn (Random Forest).
- Analysis: pandas, pyulog, matplotlib