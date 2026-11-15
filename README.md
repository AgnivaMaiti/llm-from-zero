# LLMs from Zero

Code for the **LLMs from Zero** video series on [@ognilingual](https://www.youtube.com/@ognilingual): 100 videos that take you from
"what is a word to a computer?" to training, fine-tuning and shipping your own language models.

Every video has a folder here with code you can run, explained line by line, plus homework.
You only need Python 3 for the first videos. Later ones use PyTorch and run on a free Google Colab GPU.

| # | Video | Code |
|---|---|---|
| 1 | What is NLP? Rules, counting, vectors and LLMs | [`01-what-is-nlp/`](01-what-is-nlp/) |

The full 100-video plan is in [`SERIES_PLAN.csv`](SERIES_PLAN.csv).

## Run video 1

```bash
cd 01-what-is-nlp
python video01.py
```

You should see ELIZA answer "Why do you feel tired?", fail on "I am feeling tired", and the counter predict
`store` with probability 0.67 and `gym` with 0.33.

## License

MIT. Use it, change it, learn from it.
