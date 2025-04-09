# Lexical Obfuscation: Inner-Character Permutation

This Python script scrambles the **internal characters** of each word in a string while preserving the **first and last letter** (toggleable). Inspired by Graham Rawlinson's 1976 PhD research on human readability and internal letter order.

---

## 🔥 Why?

- Stress-test how LLMs interpret corrupted or non-standard token sequences  
- Explore whether models infer meaning via **latent conceptual reasoning**, not just surface tokenization  
- Obfuscate internal logic/state while keeping semantic coherence intact  
- Investigate how model understanding persists even when input is structurally "broken"

---

## 🧠 TL;DR

LLMs don’t just read tokens—they reconstruct meaning from **latent vector patterns**.  
This script reveals how even scrambled text is often interpreted correctly, showing that token-level filters are insufficient for true model control or containment.  
**My conclusion is that real protection happens in the latent space, not the character stream.**

---

## 🧠 Example

### Input:
```text
The modernization of urban infrastructure accelerates socio-economic stratification.
``` 
### Output: 
```text
The miiteoaodrznn of urabn itnfrrcsruatue aeclcearets scoio-ecmnoioc scottiafatiirn.
```

## ⚙️ Usage

Run from the command line:

```bash
python lexical-obfuscation.py "Your text here"
```
Or specify options:
```bash
python lexical-obfuscation.py "Your text here" --no-boundary --deterministic --seed 123
```
### Command-Line Options

```
Option             Description
------------------ -----------------------------------------------------------
--no-boundary      Scramble the entire word (not just internal characters)
--deterministic    Use deterministic shuffling (based on hash + seed)
--seed <int>       Seed value for deterministic shuffling (default: 42)
```

## 🛠️ Installation

Just clone and run. No dependencies.

```bash
git clone https://github.com/YOUR_USERNAME/lexical-obfuscation.git
cd lexical-obfuscation
python lexical-obfuscation.py "Some sample text"
```

### 📄 License

MIT — do what you want, just don't blame me when your AI gets ideas.

## 🧠 Credit

Inspired by Graham Rawlinson’s 1976 thesis at Nottingham University on how humans can still read jumbled words, as long as the first and last letters remain intact.
