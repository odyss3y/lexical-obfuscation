#!/usr/bin/env python3
"""
Lexical Obfuscation Script: Inner-Character Permutation

This script scrambles the internal characters of each word in the provided text.
It preserves the first and last letters by default (toggleable) and can operate in
either a random or deterministic mode (using a fixed seed).

Usage:
    python lexical_obfuscation.py "Your text here." [--no-boundary] [--deterministic] [--seed SEED]

Example:
    Input:  "The modernization of urban infrastructure accelerates socio-economic stratification."
    Output: "The mazoniortiedn of ubarn ianutrcurstrfe aleacreects scioo-eciomnoc sttaftricoiian."

Note:
    This implementation uses a regex to process words while leaving punctuation untouched.
"""

import re
import random
import argparse

def scramble_word(word, preserve_boundaries=True, deterministic=False, seed=42):
    """
    Scrambles a single word's internal characters.
    
    Args:
        word (str): The word to scramble.
        preserve_boundaries (bool): If True, leaves the first and last character intact.
        deterministic (bool): If True, uses a fixed seed for reproducible shuffling.
        seed (int): Seed for deterministic shuffling.

    Returns:
        str: The obfuscated word.
    """
    if len(word) <= 3:
        return word  # Not enough characters to scramble.
    
    if preserve_boundaries:
        first, middle, last = word[0], list(word[1:-1]), word[-1]
        if deterministic:
            # Mix the seed with the word's hash to get reproducible yet word-specific shuffling.
            random.seed(seed + hash(word))
        else:
            random.seed()
        random.shuffle(middle)
        return first + ''.join(middle) + last
    else:
        letters = list(word)
        if deterministic:
            random.seed(seed + hash(word))
        else:
            random.seed()
        random.shuffle(letters)
        return ''.join(letters)

def obfuscate_text(text, preserve_boundaries=True, deterministic=False, seed=42):
    """
    Obfuscates text by scrambling the internal letters of each word.

    Args:
        text (str): The input text to obfuscate.
        preserve_boundaries (bool): If True, first and last characters of each word remain unchanged.
        deterministic (bool): If True, shuffling is reproducible.
        seed (int): Seed for deterministic shuffling.

    Returns:
        str: The obfuscated text.
    """
    # Matches words composed of alphanumeric characters.
    pattern = re.compile(r'\b\w+\b')
    
    def scramble_match(match):
        word = match.group(0)
        return scramble_word(word, preserve_boundaries, deterministic, seed)
    
    return pattern.sub(scramble_match, text)

def main():
    parser = argparse.ArgumentParser(
        description="Lexical Obfuscation Script: Inner-Character Permutation"
    )
    parser.add_argument("text", help="Input text to obfuscate", type=str)
    parser.add_argument("--no-boundary", action="store_true",
                        help="Scramble entire word without preserving first and last characters")
    parser.add_argument("--deterministic", action="store_true",
                        help="Use deterministic shuffling (fixed seed) for reproducibility")
    parser.add_argument("--seed", type=int, default=42,
                        help="Seed for deterministic shuffling (default: 42)")
    
    args = parser.parse_args()
    
    result = obfuscate_text(
        args.text,
        preserve_boundaries=not args.no_boundary,
        deterministic=args.deterministic,
        seed=args.seed
    )
    print(result)

if __name__ == "__main__":
    main()