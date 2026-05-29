import os
import subprocess
import sys
import unittest
from pathlib import Path

from lexical_obfuscation import obfuscate_text, scramble_word


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "lexical_obfuscation.py"


def run_cli(text, *, python_hash_seed="1"):
    env = os.environ.copy()
    env["PYTHONHASHSEED"] = python_hash_seed

    completed = subprocess.run(
        [
            sys.executable,
            str(SCRIPT),
            text,
            "--deterministic",
            "--seed",
            "123",
        ],
        check=True,
        capture_output=True,
        text=True,
        env=env,
    )
    return completed.stdout.strip()


class LexicalObfuscationTests(unittest.TestCase):
    def test_scramble_word_preserves_short_words(self):
        self.assertEqual(scramble_word("a"), "a")
        self.assertEqual(scramble_word("cat"), "cat")

    def test_scramble_word_preserves_boundaries_and_letters_when_deterministic(self):
        word = "modernization"

        scrambled = scramble_word(word, deterministic=True, seed=123)

        self.assertEqual(scrambled[0], word[0])
        self.assertEqual(scrambled[-1], word[-1])
        self.assertEqual(sorted(scrambled), sorted(word))
        self.assertEqual(scrambled, scramble_word(word, deterministic=True, seed=123))

    def test_obfuscate_text_preserves_punctuation_and_word_boundaries(self):
        text = "Hello, modernization!"

        obfuscated = obfuscate_text(text, deterministic=True, seed=123)

        self.assertTrue(obfuscated.startswith("H"))
        self.assertEqual(obfuscated[4], "o")
        self.assertEqual(obfuscated[5:7], ", ")
        self.assertTrue(obfuscated.endswith("!"))
        self.assertEqual(sorted(obfuscated[7:-1]), sorted("modernization"))

    def test_deterministic_cli_is_stable_with_same_python_hash_seed(self):
        text = "modernization infrastructure stratification transformation"

        self.assertEqual(
            run_cli(text, python_hash_seed="1"),
            run_cli(text, python_hash_seed="1"),
        )

    def test_deterministic_cli_is_stable_across_python_hash_seeds(self):
        text = "modernization infrastructure stratification transformation"

        self.assertEqual(
            run_cli(text, python_hash_seed="1"),
            run_cli(text, python_hash_seed="2"),
        )
