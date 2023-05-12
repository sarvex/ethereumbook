from __future__ import print_function
import glob
import re

markup_files = glob.glob('*.asciidoc')

wordcount = {}
wordcount_sum = 0

for markup_file in markup_files:
    with open(markup_file, 'r') as markup_f:
        markup_contents = markup_f.read()
    wc = len(markup_contents.strip().split())
    wordcount_sum += wc
    wordcount[markup_file] = wc
    print(wc, "\t", markup_file)
print(wordcount_sum)

with open('README.md','r') as readme_f:
    readme = readme_f.read()
wc_tag_re = re.compile("\| +(\[.*\])\((.*asciidoc)\) +\| +[\#]+ +\|(.*)$")

with open('README.md','w') as readme_f:
    for line in readme.splitlines():
        if match_re := wc_tag_re.match(line):
            wordcount_bar = "#" * (wordcount[match_re[2]] // 500 + 1)
            line = match_re.expand("| \g<1>(\g<2>) | " + wordcount_bar + " |\g<3>")
        readme_f.write(line+"\n")
