#!/usr/bin/env python3
import re
from pathlib import Path

page_data = """\
probability_theory_1a.Rmd | 08-Chap-4 | NA |
probability_theory_1b.Rmd | 09-Chap-5 | NA |
probability_theory_2_compound.Rmd | 10-Chap-6 | NA |
probability_theory_3.Rmd | 11-Chap-7 | NA |
probability_theory_4_finite.Rmd | 12-Chap-8 | NA |
sampling_variability.Rmd | 13-Chap-9 | NA |
monte_carlo.Rmd | 14-Chap-10 | NA |
inference_ideas.Rmd | 15-Chap-11 | NA |
inference_intro.Rmd | 16-Chap-12 | NA |
point_estimation.Rmd | 17-Chap-13 | NA |
framing_questions.Rmd | 18-Chap-14 | NA |
testing_counts_1.Rmd | 19-Chap-15 | NA |
significance.Rmd | 20-Chap-16 | NA |
testing_counts_2.Rmd | 21-Chap-17 | NA |
testing_measured.Rmd | 22-Chap-18 | NA |
testing_procedures.Rmd | 23-Chap-19 | NA |
confidence_1.Rmd | 24-Chap-20 | NA |
confidence_2.Rmd | 25-Chap-21 | NA |
reliability_average.Rmd | 26-Chap-22 | NA |
correlation_causation.Rmd | 27-Chap-23 | NA |
how_big_sample.Rmd | 28-Chap-24 | NA |
bayes_simulation.Rmd | 29-Chap-25 | NA |"""

callout_fmt = r"""\1

:::{{.callout-warning}}
## Draft page partially ported from original PDF

This page is an automated and partial import from the [original second-edition
PDF](https://resample.com/content/text/{chapter}.pdf).

We are in the process of updating this page for formatting, and porting any
code from the original [RESAMPLING-STATS
language](http://www.statistics101.net) to Python and R.

Feel free to read this version for the sense, but expect there to be multiple
issues with formatting.

We will remove this warning when the page has adequate formatting, and we have
ported the code.
:::
"""

page_map = {}
for line in page_data.splitlines():
    fname, chapter, *_ = [p.strip() for p in line.split('|')]
    page_map[fname] = chapter

regex = re.compile('^(# .*$)', re.M)

for fname, chapter in page_map.items():
    rmd_pth = Path(fname)
    contents = rmd_pth.read_text()
    if regex.search(contents):
        contents = regex.sub(
            callout_fmt.format(chapter=chapter),
            contents,
            count=1,
        )
        rmd_pth.write_text(contents)
