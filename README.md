```markdown
# WebScout

![WebScout Logo](logo.png)

**WebScout** is a high-performance directory scanner written in Python, designed to efficiently identify hidden directories and files on web servers. Its multi-threaded architecture makes it an essential tool for penetration testers and security researchers.

## Features

- **Multi-Threaded Scanning**: Utilize multiple threads for fast and efficient directory/file discovery.
- **Customizable Wordlists**: Modify or create custom wordlists based on your scanning needs.
- **User-Friendly CLI**: Intuitive command-line interface for easy setup and use.
- **Color-Coded Output**: Enhanced terminal output for better readability and result analysis.

## Installation

Follow these steps to install WebScout:

1. Clone the repository:
   ```bash
   git clone https://github.com/hackerjacke440/WebScout.git
   cd WebScout
   ```

2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

WebScout is simple to use and requires minimal configuration. Run the following command to start scanning a target server:

```bash
python webscout.py <target_url> -w <path_to_wordlist> -t <number_of_threads>
```

### Parameters:
- `<target_url>`: The URL of the target website (e.g., `http://example.com/`).
- `-w <path_to_wordlist>`: The path to the wordlist file. Default is `dictionaries/dicc.txt`.
- `-t <number_of_threads>`: The number of concurrent threads to use for scanning. Default is `10`.

### Example:
```bash
python webscout.py http://example.com/ -w dictionaries/dicc.txt -t 10
```

### Help:
To see additional options and usage details, run:
```bash
python webscout.py -h
```

## Requirements

WebScout requires Python 3.x and the following libraries:

- `requests` (v2.25.1 or higher) – For making HTTP requests.
- `colorama` – For colorful terminal output.
- `argparse` – For parsing command-line arguments (comes with Python).

To install the required packages, run:
```bash
pip install -r requirements.txt
```

## Contributing

We welcome contributions to WebScout! If you'd like to contribute:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-name`).
3. Make your changes.
4. Commit your changes (`git commit -am 'Add feature'`).
5. Push to your forked repository.
6. Create a pull request.

Please ensure that your code follows the project's coding standards and guidelines.

## License

WebScout is open-source software released under the [MIT License](LICENSE).
```

### Changes and Improvements:
- Enhanced formatting for clarity and better structure.
- Clearly defined sections such as **Features**, **Requirements**, and **License**.
- Proper markdown syntax for code blocks and commands.
