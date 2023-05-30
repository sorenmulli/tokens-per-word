from argparse import ArgumentParser

from tokens_per_word.tokenization import get_tokenizer, run_full_tokenization


def run_from_cli():
    parser = ArgumentParser(
        description="Calculate tokens per word using a specified HuggingFace tokenizer."
    )
    parser.add_argument(
        "-t",
        "--tokenizer",
        required=True,
        help="The key of a HuggingFace tokenizer model.",
    )
    args = parser.parse_args()
    tokenizer = get_tokenizer(args.tokenizer)
    run_full_tokenization(tokenizer)
