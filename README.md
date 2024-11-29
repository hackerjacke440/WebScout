```markdown
# 🌐 WebScout

![WebScout Logo](logo.png)

**WebScout** is a Python-powered, high-performance directory scanner designed to uncover hidden directories and files on web servers. Its multi-threaded architecture ensures speed and efficiency, making it indispensable for penetration testers and security researchers.

---

## 🚀 Features

- **Multi-Threaded Scanning**  
  Perform fast, concurrent directory/file scans using multiple threads.

- **Customizable Wordlists**  
  Personalize wordlists to match your specific needs for optimal scanning results.

- **User-Friendly CLI**  
  An intuitive command-line interface ensures effortless usage.

- **Color-Coded Output**  
  Clearly distinguish results with vibrant, color-coded terminal output.

---

## ⚙️ Installation

### 1️⃣ Clone the Repository
Run the following commands to clone WebScout and navigate to its directory:
```bash
git clone https://github.com/hackerjacke440/WebScout.git
cd WebScout
```

### 2️⃣ Install Dependencies
Install the required Python libraries with:
```bash
pip install -r requirements.txt
```

---

## 📖 Usage

Start scanning with WebScout by running the script with the necessary parameters.

### Basic Command:
```bash
python webscout.py <target_url> -w <path_to_wordlist> -t <number_of_threads>
```

### Parameters:
- **`<target_url>`**: The URL of the target website (e.g., `http://example.com/`).
- **`-w <path_to_wordlist>`**: Path to the wordlist file (default: `dictionaries/dicc.txt`).
- **`-t <number_of_threads>`**: Number of concurrent threads (default: `10`).

### Example:
```bash
python webscout.py http://example.com/ -w dictionaries/dicc.txt -t 10
```

### Get Help:
Need more options or details? Run:
```bash
python webscout.py -h
```

---

## 📋 Requirements

WebScout requires **Python 3.x** and the following libraries:

- 🛠️ `requests` (>=2.25.1): For HTTP request handling.
- 🎨 `colorama`: For colorful output in the terminal.
- 📜 `argparse`: For parsing command-line arguments (built into Python).

Install these dependencies using:
```bash
pip install -r requirements.txt
```

---

## 🤝 Contributing

We welcome contributions! Here's how you can contribute:

1. **Fork the Repository**: Create a copy on GitHub.
2. **Create a Branch**: Work on your feature or bugfix in a new branch:
   ```bash
   git checkout -b feature-name
   ```
3. **Commit Changes**: Save your progress with meaningful commit messages:
   ```bash
   git commit -m "Add new feature"
   ```
4. **Push Changes**: Push your branch to your fork:
   ```bash
   git push origin feature-name
   ```
5. **Submit a Pull Request**: Open a pull request on the main repository for review.

---

## 📜 License

WebScout is open-source software, released under the [MIT License](LICENSE). Feel free to use, modify, and share it according to the license terms.
```

### Changes Made:
1. **Icons and Emojis**: Added icons to make sections visually engaging.
2. **Short Descriptions**: Simplified section headers for clarity.
3. **Section Dividers**: Used horizontal rules to separate sections neatly.
4. **Clean Parameters Formatting**: Highlighted key parameters with bold text for emphasis.
5. **Engaging Language**: Made descriptions more dynamic and approachable.
