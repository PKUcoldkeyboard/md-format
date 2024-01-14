from __future__ import annotations

import re
import pangu
import pandas as pd
from glob import glob


def get_nouns(csv_file):
    try:
        df = pd.read_csv(csv_file, header=None)
        df[1] = df[1].astype(str)
        return df[1].tolist()
    except Exception as e:
        print(f"Error occurred while reading CSV file: {e}")
        return []


def format_file(filename, nouns):
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            content = f.read()

        # Use Pangu to automatically insert whitespace between CJK and half-width characters
        content = pangu.spacing_text(content)

        # Check and convert nouns to proper nouns
        for noun in nouns:
            pattern = r'\b({})\b'.format(noun.lower())
            content = re.sub(pattern, noun, content, flags=re.IGNORECASE)

        with open(filename, 'w', encoding='utf-8') as f:
            f.write(content)
    except Exception as e:
        print(f"Error occurred while formatting file {filename}: {e}")


def main():
    try:
        nouns = get_nouns('dicts.csv')
        for filename in glob('*.md'):
            format_file(filename, nouns)
    except Exception as e:
        print(f"Error occurred in main function: {e}")


if __name__ == '__main__':
    main()
