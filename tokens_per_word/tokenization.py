import sys

from transformers import AutoTokenizer, PreTrainedTokenizer


def get_tokenizer(tokenizer_string: str) -> PreTrainedTokenizer:
    return AutoTokenizer.from_pretrained(tokenizer_string)


def run_full_tokenization(tokenizer: PreTrainedTokenizer):
    num_words = 0
    num_tokens = 0
    for line in sys.stdin:
        text = line.rstrip()
        result = tokenizer(text)
        num_words += len(text.split())
        num_tokens += len(result.input_ids)
    print(f"Number of tokens: {num_tokens}")
    print(f"Number of words : {num_words}")
    print(f"Tokens per word : {num_tokens/num_words:.4f}")
