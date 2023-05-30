# How many tokens per word using given tokenizer and given dataset?

```bash
$ pip install .

$ cat raw-sentences.txt | tokens-per-word -t "north/t5_base_scand3M"
# or (if you have csvkit/csvtools)
$ csvcut -c "text-column" tabular-dataset.csv | tokens-per-word -t "north/t5_base_scand3M"
# or (if you jave jq)
$ cat line-formatted-dataset.jsonl | jq .text-field | tokens-per-word -t "north/t5_base_scand3M"
```
