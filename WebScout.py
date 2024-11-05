import os
import requests
import threading
import argparse
from urllib.parse import urljoin
from colorama import Fore, Style, init
import configparser

# Initialize colorama
init(autoreset=True)

# ASCII Art Banner
BANNER = f"""{Fore.CYAN}
 ___       __    ______ ________                  _____ 
 __ |     / /_______  /___  ___/_______________  ___  /_
 __ | /| / /_  _ \\_  __ \\____ \\_  ___/  __ \\  / / /  __/
 __ |/ |/ / /  __/  /_/ /___/ // /__ / /_/ / /_/ // /_  
 ____/|__/  \\___//_.___//____/ \\___/ \\____/\\__,_/ \\__/  
                                                        v1.0
{Style.RESET_ALL}"""

class WebScout:
    def __init__(self, target, wordlist, threads, max_time):
        self.target = target
        self.wordlist = wordlist
        self.threads = threads
        self.max_time = max_time
        self.lock = threading.Lock()
        self.responses = []

    def load_wordlist(self):
        with open(self.wordlist, 'r') as f:
            return [line.strip() for line in f]

    def request_url(self, url):
        try:
            response = requests.get(url, timeout=5)
            return response
        except requests.RequestException as e:
            print(f"{Fore.RED}[ERROR] {e}{Style.RESET_ALL}")
            return None

    def scan_directory(self, base_url):
        wordlist = self.load_wordlist()
        threads = []
        for word in wordlist:
            url = urljoin(base_url, word)
            thread = threading.Thread(target=self.check_url, args=(url,))
            threads.append(thread)
            thread.start()
            if len(threads) >= self.threads:
                for t in threads:
                    t.join()
                threads = []

        # Join remaining threads
        for t in threads:
            t.join()

    def check_url(self, url):
        response = self.request_url(url)
        if response:
            status_code = response.status_code
            self.lock.acquire()
            self.responses.append((url, status_code))
            self.lock.release()
            
            # Color the output based on the status code
            if status_code == 200:
                print(f"{Fore.GREEN}[{status_code}] {url}{Style.RESET_ALL}")  # Success in green
            elif status_code == 404:
                print(f"{Fore.RED}[{status_code}] {url}{Style.RESET_ALL}")  # Not Found in red
            elif status_code == 300:
                print(f"{Fore.YELLOW}[{status_code}] {url}{Style.RESET_ALL}")  # Redirect in yellow
            else:
                print(f"[{status_code}] {url}")  # Other status codes in default color

    def run(self):
        print(BANNER)  # Display the banner
        print(f"\n[+] Scanning {self.target}...\n")
        self.scan_directory(self.target)
        print("\n[+] Scan completed.")

    @staticmethod
    def load_config(config_file):
        config = configparser.ConfigParser()
        config.read(config_file)
        return {
            'wordlist': config.get('dictionary', 'wordlist', fallback='directory-list-2.3-medium.txt'),
            'threads': config.getint('general', 'threads', fallback=10),
            'max_time': config.getint('general', 'max-time', fallback=0)
        }

def main():
    parser = argparse.ArgumentParser(description="WebScout - A Basic Directory Scanner")
    parser.add_argument("target", help="Target URL (e.g., http://example.com/)")
    parser.add_argument("-c", "--config", help="Path to the configuration file", default="webscout.cfg")
    parser.add_argument("-w", "--wordlist", help="Path to the wordlist file", default=None)
    parser.add_argument("-t", "--threads", type=int, help="Number of threads to use", default=None)
    args = parser.parse_args()

    # Load configuration
    config = WebScout.load_config(args.config)

    # Override config values with command-line arguments if provided
    wordlist = args.wordlist if args.wordlist else config['wordlist']
    threads = args.threads if args.threads else config['threads']

    # Create an instance of WebScout and run it
    webscout = WebScout(
        target=args.target.rstrip('/') + '/',
        wordlist=wordlist,
        threads=threads,
        max_time=config['max_time'],
    )
    webscout.run()

if __name__ == "__main__":
    main()
