```markdown
# WebScout

![WebScout Logo](logo.png)

**WebScout** is a robust directory scanner built in Python that efficiently uncovers hidden directories and files on web servers. With its multi-threaded architecture, it serves as an invaluable asset for penetration testers and security researchers.

## Key Features

- **High-Speed Scanning**: Leverages multi-threading for rapid directory and file discovery.
- **Customizable Wordlists**: Easily modify or create wordlists tailored to your scanning requirements.
- **Intuitive Interface**: User-friendly command-line interface simplifies usage.
- **Enhanced Output**: Colorful terminal output for improved readability of results.

## Installation

To set up WebScout, follow these steps:

1. Clone the repository:
   ```bash
   git clone https://github.com/hackerjacke440/WebScout.git
   cd WebScout
   ```bash

2. Install required packages:
   ```
   pip install -r requirements.txt
   ```

## Usage

WebScout scans directories and files on a specified web server. Execute the script with the necessary arguments:

```bash
python webscout.py <target_url> -w <path_to_wordlist> -t <number_of_threads>
```

### Parameters

- `<target_url>`: Target website URL (e.g., `http://example.com/`).
- `-w <path_to_wordlist>`: Path to the wordlist file. Default: `dictionaries/dicc.txt`.
- `-t <number_of_threads>`: Number of concurrent threads for scanning. Default: `10`.

### Example

```bash
python webscout.py http://example.com/ -w dictionaries/dicc.txt -t 10
```

### Help

For additional options and usage details, run:

```bash
python webscout.py -h
```

## Requirements

WebScout requires Python 3.x and the following packages:

- `requests`: For handling HTTP requests (version 2.25.1 or higher).
- `colorama`: For colorful terminal output.
- `argparse`: For command-line argument parsing (included in the standard library).

### Install Requirements

Create a virtual environment (optional) and install dependencies:

```bash
pip install -r requirements.txt
```

### Sample `requirements.txt`

```plaintext
requests>=2.25.1
colorama
```
## Contributing

Contributions are encouraged! Please submit a pull request or open an issue for discussion. Ensure compliance with the project's coding standards and guidelines.
