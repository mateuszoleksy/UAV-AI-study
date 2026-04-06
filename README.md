# UAV-AI-study

Research framework for **AI-driven UAV (drone) navigation and communication**.

## Overview

This repository contains research code, experiments, and datasets for studying:

- **Communication** – inter-drone and ground-station communication protocols, link reliability, signal processing
- **Perception** – sensor fusion, computer vision, localization

## Repository Structure

```
UAV-AI-study/
├── src/
│   ├── communication/    # Communication modules
│   └── perception/       # Perception and sensor fusion
├── experiments/          # Experiment scripts and configurations
├── data/                 # Datasets (raw and processed)
├── docs/                 # Documentation and research notes
├── tests/                # Unit and integration tests
└── notebooks/            # Jupyter notebooks for exploration
```

## Getting Started

### Prerequisites

- Python 3.10+
- pip

### Installation

```bash
git clone https://github.com/mateuszoleksy/UAV-AI-study.git
cd UAV-AI-study
pip install -r requirements.txt
```

### Running Tests

```bash
python -m pytest tests/
```

## License

This project is licensed under the MIT License – see the [LICENSE](LICENSE) file for details.
