# Package compare

Performs compare of information between two branches of binary packages.

## Installation

1. Clone the repository to your local machine:

    ```bash
    git clone git@github.com:Kolmarovich/compare-packages.git
    ```

2. Navigate to the project directory:

    ```bash
    cd compare-packages
    ```

3. Create a virtual environment:

    ```bash
    python3 -m venv venv
    ```

4. Activate the virtual environment:

    For Linux and macOS:

    ```bash
    source venv/bin/activate
    ```

    For Windows:

    ```bash
    venv\Scripts\activate
    ```

5. Install dependencies:

    ```bash
    pip install -r requirements.txt
    ```

## Usage

To compare packages from two branches, follow these steps:

1. Run the CLI utility with the names of the first, second branches and the architecture of the packages (default is i586):

    ```bash
    python compare_packages_cli.py branch1 branch2 --architecture arch
    ```

    Example:

    ```bash
    python compare_packages_cli.py p10 sisyphus --architecture i586
    ```

    For help:

    ```bash
    python compare_packages_cli.py -h
    ```

3. The comparison results will be saved in 3 .json files in the root directory of the project.      
   The first file unique_packages1.json contains a list of unique packages from the first branch.     
   The second file unique_packages2.json contains a list of unique packages from the second branch.     
   The third file version_release_diff.json contains packages from the second branch whose version is higher than in the first branch.     

## Code Structure and Description

### compare_packages.py

This module contains functions for comparing versions and releases of packages.

#### Functions:

- `load_packages(branch, architecture)`: Loads the list of packages for the specified branch of the operating system and architecture.
- `save_packages_to_file(packages, filename)`: Saves the list of packages to a JSON file.
- `compare_versions(version1, version2)`: Compares two package versions.
- `compare_release(release1, release2)`: Compares two package releases.
- `compare(packages1, packages2)`: Compares packages between two branches of the operating system.

### compare_packages_cli.py

This script provides a command-line interface for comparing packages.

