from jmd_imagescraper.core import * # dont't worry, it's designed to work with import *
from pathlib import Path

root = Path().cwd()/"images"


duckduckgo_search(root, "FMCG","", max_results=20)

