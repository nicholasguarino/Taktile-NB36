# Taktile-NB36
Taktile - TAM Challenge

## Overview
This project contains a GitHub Actions workflow that automatically updates code nodes in a Taktile flow whenever Python files in the `codenodes` directory are modified. The workflow validates the Python files and updates the corresponding nodes in Taktile using their API.

## Project Structure
```
.
├── .github/workflows/
│   └── update_code_nodes.yml    # GitHub Actions workflow
├── codenodes/
│   ├── Multiply.py             # Code node implementation
│   └── Summarize.py            # Code node implementation
└── update_code_nodes.py        # Script to update Taktile nodes
```

## Setup Instructions

### 1. GitHub Secrets Configuration
1. Fork or clone this repository
2. Go to your repository's Settings > Secrets and Variables > Actions
3. Add the following secret:
   - `TAKTILE_API_KEY`: Your Taktile API key

### 2. Flow Configuration
1. Use Taktile's API endpoints to obtain the necessary IDs:
   - Use the List Decision endpoint to get an overview of available flows
   - Use the Get Decision Graph endpoint to obtain detailed information about your flow
   - From these endpoints, you'll need to extract:
     - Flow ID: The unique identifier for your flow
     - Node IDs: The specific node IDs for each code node in your flow
2. Open `update_code_nodes.py` and update the following:
   - `FLOW_ID`: Your Taktile flow ID
   - `NODE_MAPPING`: Dictionary mapping your Python files to their corresponding node IDs

## How It Works

### GitHub Actions Workflow
The workflow (`update_code_nodes.yml`) is triggered when:
- Changes are pushed to the `main` branch
- The changes include modifications to Python files in the `codenodes` directory

The workflow:
1. Sets up Python 3.11
2. Validates all Python files in the `codenodes` directory
3. Installs required dependencies
4. Runs the update script with the Taktile API key

### Update Script
The `update_code_nodes.py` script:
1. Reads Python files from the `codenodes` directory
2. Makes API calls to Taktile to update each code node
3. Provides feedback on the success or failure of each update

## Code Node Structure
Each code node in the `codenodes` directory should be a valid Python file that implements the required functionality for your Taktile flow. The current implementation includes:
- `Multiply.py`: Implementation for multiplication operations
- `Summarize.py`: Implementation for summarization operations
