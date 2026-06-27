#!/usr/bin/env python3
"""Count nucleotide bases in a FASTA file.

A deliberately small, readable example for beginners. Run it from the terminal:

    python scripts/count_bases.py data/sample.fasta

or, because postBuild made it executable:

    ./scripts/count_bases.py data/sample.fasta
"""
import sys
from collections import Counter


def read_fasta(path):
    """Yield (header, sequence) pairs from a FASTA file."""
    header, seq = None, []
    with open(path) as fh:
        for line in fh:
            line = line.rstrip()
            if line.startswith(">"):
                if header is not None:
                    yield header, "".join(seq)
                header, seq = line[1:], []
            else:
                seq.append(line)
        if header is not None:
            yield header, "".join(seq)


def main():
    if len(sys.argv) != 2:
        print("Usage: count_bases.py <file.fasta>", file=sys.stderr)
        sys.exit(1)

    path = sys.argv[1]
    total = Counter()
    for header, seq in read_fasta(path):
        counts = Counter(seq.upper())
        gc = counts["G"] + counts["C"]
        pct = 100 * gc / len(seq) if seq else 0
        print(f"{header.split()[0]:10s} len={len(seq):4d}  GC={pct:5.1f}%")
        total.update(counts)

    print("-" * 30)
    print("Totals:", dict(total))


if __name__ == "__main__":
    main()
