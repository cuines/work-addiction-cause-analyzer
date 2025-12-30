#!/usr/bin/env python3
"""
Work Addiction Cause Analyzer - Main script.
Data loading function for reading interview excerpts.
"""

import os


def load_excerpts(file_path="data/sample_excerpts.txt"):
    """
    Read a text file and return a list of non‑empty lines (excerpts).
    
    Parameters
    ----------
    file_path : str, optional
        Path to the text file containing excerpts (default is
        'data/sample_excerpts.txt').
    
    Returns
    -------
    list of str
        List where each element is a stripped, non‑empty line from the file.
        If the file does not exist or cannot be read, an empty list is returned
        and an error message is printed.
    """
    excerpts = []
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            for line in f:
                stripped = line.strip()
                if stripped:  # ignore blank lines
                    excerpts.append(stripped)
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
    except OSError as e:
        print(f"Error reading file '{file_path}': {e}")
    return excerpts


if __name__ == "__main__":
    # Example usage
    print("Testing data loading function...")
    loaded = load_excerpts()
    print(f"Loaded {len(loaded)} excerpt(s):")
    for i, excerpt in enumerate(loaded, 1):
        print(f"  {i}. {excerpt}")