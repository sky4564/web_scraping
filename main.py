from extractors.wwr import extract_wwr_jobs
from extractors.file import save_to_file

keyword = 'react'

jobs = extract_wwr_jobs(keyword)

save_to_file(keyword, jobs)

