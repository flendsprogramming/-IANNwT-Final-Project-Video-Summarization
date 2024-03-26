# IANNwT-Final-Project-Video-Summarization

Everyday, people watch tons of videos to get facts and quick information, most times listening through long videos just to get a scope of what is being talked about. 
This VideoSummarizer project aims at providing a qualitative tool that saves a ton of time for people who want a quick summary of what a speech-talk centric video
is all about without wanting to watch through every minutes of it. 

To accomplish this, a pipeline of video - speech - text is implemented, using wav2vec2 pretrained model for speech-to-text stage. For the summarisation stage, a sequence to sequence 3 Layer Bidirectional deep learning model with attention mechanism is implemented in combo with the Global Vectors for Word Representation. 


# PITA (Procedural and Iterative Terrain Assembly)

Welcome to PITA, a cutting-edge framework designed for creating dynamic, customizable simulation environments. PITA stands at the forefront of environment generation, offering a scalable, flexible, and user-friendly platform that caters to a wide array of applications in artificial intelligence (AI), game development, and beyond.

## Introduction

The advancement of AI systems capable of understanding complex, ever-changing environments necessitates access to diverse and challenging simulation scenarios. Traditional static environments often lead to model overfitting, limiting AI's ability to adapt to new or modified settings. PITA addresses this challenge by enabling the generation of vast, varied environments, facilitating the development of adaptable, robust AI agents.

## Core Features

- **Iterative Refinement:** Continuous enhancement of environments to meet specific training or research objectives.
- **Customization at Scale:** Modular design ensures full control over every aspect of the simulation.
- **Procedural Generation:** Utilizes procedural generation to create rich, unpredictable environments.
- **User Accessibility:** Designed for ease of use, allowing users with varying technical backgrounds to generate complex environments.

## Installation

```bash
# Clone the PITA repository
git clone https://github.com/YourGitHub/pita.git
cd pita

# (Optional) Create and activate a virtual environment
python -m venv pita-env
source pita-env/bin/activate  # For Windows use `pita-env\Scripts\activate`

# Install dependencies
pip install -r requirements.txt
```

## Quick Start

```bash
# Run PITA with the default configuration
python path/to/pita.py
```

This script uses the configuration from `examples/config_files` to generate environments in `.json` and `.xml` formats, stored in the `export` directory.

## Configuration

PITA's environment generation is driven by `config.yml`, allowing detailed customization of simulation settings:

- Environment dimensions
- Object properties and placement
- Procedural terrain features
- Custom rules for object interactions

See the Configuration Guide for detailed instructions.

## Use Scenarios

PITA is versatile, supporting various applications:

- **AI Training:** Generate environments for reinforcement learning, ensuring models are robust and adaptable.
- **Game Development:** Create unique, procedurally generated worlds, enhancing gameplay variety.
- **Research:** Study emergent behaviors in complex, dynamic settings.
- **Education:** Develop simulation-based learning tools for specialized training.

## Customization

Leverage PITA's modular architecture for extensive customization:

- **Modify `config.yml`:** Adjust simulation parameters to tailor environments to your needs.
- **Extend Functionality:** Implement new features or modify existing ones to expand PITA's capabilities.

## Troubleshooting

Encounter issues? Here's what to try:

- Ensure all dependencies are correctly installed.
- Validate `config.yml` formatting.
- Review error messages carefully for clues.

## Support and Contributions

Interested in contributing to PITA or need support? Visit our [GitHub Repository](https://github.com/YourGitHub/pita) for more information.

## Conclusion

PITA equips users with the tools to generate intricate, dynamic environments tailored to a wide range of applications. Explore PITA's capabilities and discover how it can elevate your projects.

