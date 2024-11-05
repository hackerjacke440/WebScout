```markdown
# WebScout

![WebScout Logo](path/to/logo.png)  <!-- Optional: Add a logo image here -->

WebScout is a simple yet powerful directory scanner written in Python. It leverages multi-threading to quickly discover hidden directories and files on web servers, making it an essential tool for penetration testers and security researchers.

## Features

- **Fast Directory Scanning**: Utilizes multi-threading for speed and efficiency.
- **Configurable Wordlists**: Easily customize your wordlist for specific scanning needs.
- **User-Friendly**: Simple command-line interface for easy usage.
- **Colorful Output**: Enhanced terminal output with colors for better visibility of results.

## Installation

To install WebScout, follow these steps:

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/WebScout.git
   cd WebScout
   ```

2. Install the required packages using `pip`:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

WebScout is designed to scan directories and files on a specified web server. To use WebScout, run the script with the required arguments:

```bash
python webscout.py <target_url> -w <path_to_wordlist> -t <number_of_threads>
```

### Parameters:

- `<target_url>`: The URL of the target website (e.g., `http://example.com/`).
- `-w <path_to_wordlist>`: The path to the wordlist file used for scanning. By default, it uses the `dictionaries/dicc.txt` file included in the repository.
- `-t <number_of_threads>`: The number of concurrent threads to use for the scan. Default is `10`.

### Example:

```bash
python webscout.py http://example.com/ -w dictionaries/dicc.txt -t 10
```

### Help:

To see all available options and usage details, you can run:

```bash
python webscout.py -h
```

## Requirements

WebScout requires Python 3.x and the following Python packages:

- `requests`: To handle HTTP requests (version 2.25.1 or higher).
- `colorama`: For colorful terminal output.
- `argparse`: For command-line argument parsing (part of the standard library).

### Installation of Requirements

To install the required packages, create a virtual environment (optional) and run:

```bash
pip install -r requirements.txt
```

### Sample `requirements.txt`

```plaintext
requests>=2.25.1
colorama
```

## Configuration

You can customize your configuration settings in the `config.cfg` file. Adjust settings according to your needs to optimize the scanning process.

## Testing

To run the tests, use the following command:

```bash
python -m unittest discover -s tests
```

## Contributing

Contributions are welcome! If you would like to contribute, please submit a pull request or open an issue for discussion. Make sure to adhere to the coding standards and guidelines outlined in the project.
