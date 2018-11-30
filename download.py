from pathlib import Path
from math import ceil
import requests
from fastprogress import force_console_behavior#master_bar, progress_bar

master_bar,progress_bar = force_console_behavior()

path = Path('data/')
path.mkdir(exist_ok=True)

wikidump_url = 'https://dumps.wikimedia.org/cewiki/20181101/cewiki-20181101-pages-meta-history.xml.bz2'
wikidump_fn = wikidump_url.split('/')[-1]

req = requests.get(wikidump_url, stream=True)

chunk_size=1024*50
try: size = req.headers['content-length']
except KeyError:
    size = int(ceil(len(req.content)/chunk_size))
    
n = int(ceil(int(size)/chunk_size))
mb = master_bar(range(1))
pb = progress_bar(range(n))

with open(path/wikidump_fn, 'wb') as f:
    for i,chunk in zip(pb,req.iter_content(chunk_size=chunk_size)):
        if chunk: # filter out keep-ailve new chunks
            f.write(chunk)
req.close()