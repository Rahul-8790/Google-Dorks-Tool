#!/usr/bin/env python2
import sys
import webbrowser
import argparse
from pathlib import Path

class GoogleDorkToolkit:
    def __init__(self):
        self.dorks_file = "dorks.txt"
        self.dorks = self.load_dorks()
        
    def load_dorks(self):
        """Load dorks from the dorks file"""
        try:
            with open(self.dorks_file, 'r') as f:
                return [line.strip() for line in f if line.strip()]
        except FileNotFoundError:
            print(f"Error: {self.dorks_file} not found!")
            sys.exit(1)
    
    def search(self, dork_index=None, custom_dork=None):
        """Perform the Google search"""
        if custom_dork:
            query = custom_dork
        elif dork_index is not None and 0 <= dork_index < len(self.dorks):
            query = self.dorks[dork_index]
        else:
            print("Invalid dork selection")
            return
            
        url = f"https://www.google.com/search?q={query}"
        print(f"Searching: {query}")
        webbrowser.open(url)
    
    def list_dorks(self):
        """List all available dorks"""
        print("\nAvailable Google Dorks:")
        for i, dork in enumerate(self.dorks):
            print(f"{i}: {dork}")

def main():
    parser = argparse.ArgumentParser(description="Google Dorks Toolkit")
    parser.add_argument("-l", "--list", action="store_true", help="List all available dorks")
    parser.add_argument("-s", "--search", type=int, help="Search by dork number")
    parser.add_argument("-c", "--custom", type=str, help="Use a custom dork")
    args = parser.parse_args()
    
    toolkit = GoogleDorkToolkit()
    
    if args.list:
        toolkit.list_dorks()
    elif args.search is not None:
        toolkit.search(dork_index=args.search)
    elif args.custom:
        toolkit.search(custom_dork=args.custom)
    else:
        toolkit.list_dorks()
        try:
            selection = int(input("\nEnter dork number to search (or Ctrl+C to exit): "))
            toolkit.search(dork_index=selection)
        except (ValueError, KeyboardInterrupt):
            print("\nExiting...")

if __name__ == "__main__":
    main()
