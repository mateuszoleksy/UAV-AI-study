# UAV-AI-study

Research framework for **AI-driven UAV (drone) navigation and perception**.

## Overview

This repository contains research code, experiments, and datasets for studying:

- **Navigation** – path planning, trajectory optimization, and autonomous route execution
- **Perception** – sensor fusion, computer vision, localization

## Repository Structure

```
UAV-AI-study/
├── src/
│   ├── navigation/       # Navigation and path planning modules
│   └── perception/       # Perception and sensor fusion
├── experiments/          # Experiment scripts and configurations
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

## Dataset

The project uses flight logs from [logs.px4.io](https://logs.px4.io/), licensed under [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/).
Download and extract do data folder.