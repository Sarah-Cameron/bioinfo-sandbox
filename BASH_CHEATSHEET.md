# Bash cheat sheet (the 15 commands you need today)

| Command | What it does |
|---|---|
| `pwd` | print working directory — where am I? |
| `ls` | list files here |
| `ls -la` | list all files, with details |
| `cd folder` | change into `folder` |
| `cd ..` | go up one level |
| `cd ~` | go to your home directory |
| `cat file` | print a file to the screen |
| `head -5 file` | show the first 5 lines |
| `tail -5 file` | show the last 5 lines |
| `less file` | scroll through a file (press `q` to quit) |
| `mkdir name` | make a new folder |
| `cp a b` | copy file `a` to `b` |
| `mv a b` | move/rename `a` to `b` |
| `rm file` | delete a file (careful — no undo!) |
| `nano file` | open a simple text editor (Ctrl+O save, Ctrl+X exit) |
| `python script.py` | run a Python script |
| `grep ">" file.fasta` | find lines containing `>` (FASTA headers) |
| `wc -l file` | count lines in a file |

## Try this sequence

```bash
pwd
ls
cd data
cat sample.fasta
grep ">" sample.fasta        # just the headers
grep ">" sample.fasta | wc -l  # how many sequences?
cd ..
python scripts/count_bases.py data/sample.fasta
```

## Make and run your own script

```bash
nano hello.py
# type:  print("it works!")
# then Ctrl+O, Enter, Ctrl+X
python hello.py
```
