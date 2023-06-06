import re
from pathlib import Path

regex = re.compile(r'(^---\n\n)', flags=re.M)

for rmd_pth in Path().glob('*.Rmd'):
    contents = rmd_pth.read_text()
    if '_common.R' in contents:
        continue
    if regex.search(contents):
        contents = regex.sub("""\
---

```{r setup, include=FALSE}
source("_common.R")
```

""", contents)
        rmd_pth.write_text(contents)
