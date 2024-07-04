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

- ?

## Program Structure

- Import a user-supplied tabular dataformat from args.input
- Import the yml formatted INSDC combined specification from linkML
- Apply a set of mappings based on args.format to the parsed tabular data
- Export the mapped data to the INSDC format to args.output

