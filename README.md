# convAST

CLI tool to convert antibiotic susceptibility test (AST) results from lab devices, EMRs, LIMs to the an INSDC compatible format.

## Installation

```bash
pip install convast
```

## Usage

```bash
convast --input <input_file> --output <output_file> --format <format>
```

## Supported Formats

- **Vitek**
- Microscan
- Phoenix
- Sensititre

EMR/LIMs exports?

## Program Structure

- Import a user-supplied tabular dataformat from args.input
- Import the yml formatted INSDC combined specification from linkML
- Apply a set of mappings based on args.format to the parsed tabular data
- Export the mapped data to the INSDC format to args.output


## Core data/object model
- Standardised INSDC AST format dataclass imported from linkML (e.g., [linkML documentation example](https://linkml.io/linkml/intro/tutorial05.html))
- Input parent class with generic functions for parsing, iterating, write, applying mappings (e.g., [hAMRonizedResultIterator](https://github.com/pha4ge/hAMRonization/blob/master/hAMRonization/Interfaces.py#L15))  
- For each Vitek/Phoenix/Microtitre etc an iterator subclass that inherits from this input parent class including specific mappings and any adjustments to generic functions needed (e.g., [tool specific hAMRonization classes](https://github.com/pha4ge/hAMRonization/blob/master/hAMRonization/StarAmrIO.py#L14))
