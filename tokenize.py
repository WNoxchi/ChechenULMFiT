from pathlib import Path
import sentencepiece as spm
from time import time

# text_path = 'data/wikimedia/20181116/wiki.ce.txt'
text_path = Path('data/wikimedia')

# get latest wikimedia dump
dates = [d for d in list(text_path.iterdir()) if d.is_dir() and d.name.isnumeric()]
latest_date = str(max(map(lambda x: int(x.name), dates)))
text_path = text_path/latest_date/'wiki.ce.txt' # will fail if empty dir

# train & run tokenizer
t0 = time()
vocab_size = 40000; model_name=f'nx{str(vocab_size)[:2]}k'; m_type='unigram'
spm.SentencePieceTrainer.Train(f'--input={text_path} --model_prefix={model_name} --vocab_size={vocab_size} --character_coverage=1.0 --model_type={m_type}')
t  = time() - t0

# print time
print(f"Time elapsed: {int(t/60)}:{int(t%60):02}.") # m:ss