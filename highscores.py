import os.path

""" using object "file"
to prompt and clean up correctly
"""

with open("highscores") as score:
    for line in score:
        print line,

