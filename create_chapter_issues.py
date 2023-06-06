from pathlib import Path
from github import Github

issue_data = """\
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

original_fname_fmt = 'https://resample.com/content/text/{chapter}.pdf'

issue_map = {}
for line in issue_data.splitlines():
    fname, chapter, *_ = [p.strip() for p in line.split('|')]
    issue_map[Path(fname).stem] = chapter

# Get the GitHub API token
token = 'your_token'

# Create a GitHub client
client = Github(token)

# Get the repository name and issue title from the user
repo_name = 'resampling-stats/resampling-with'

repo = client.get_repo(repo_name)
chapter_label = repo.get_label('Chapter')

for fname, chapter in issue_map.items():
    issue_title = f'First pass on chapter {fname}'
    link = original_fname_fmt.format(chapter=chapter)
    issue = repo.create_issue(
        title=issue_title,
        body=f'See [{chapter}]({link})',
        labels=[chapter_label]
    )
