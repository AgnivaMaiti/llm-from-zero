# Video 1: What is NLP?

## The ideas, in one page

**NLP (Natural Language Processing)** = getting computers to read, understand and write human language.

**Problem 1: computers only see numbers.** The letter `H` is stored as the number 72 (`ord("H")` in Python).
Every NLP system starts by turning words into numbers without throwing away their meaning.

**Problem 2: language is ambiguous.** "I saw a man with a telescope" has two correct readings. "Bank" can be money or a river.
Humans pick the right one from context. Computers have to learn to.

**The four waves**

| Wave | Idea | Strength | Weakness |
|---|---|---|---|
| 1. Rules (ELIZA, 1966) | Humans write if-this-then-that patterns | Predictable | Breaks on anything nobody wrote a rule for |
| 2. Counting | Count which words follow which in lots of text | Learns from data | Has no idea "cat" and "kitten" are similar |
| 3. Vectors | Each word becomes a list of numbers; similar words get similar numbers | Captures meaning | Needs neural networks to learn the numbers |
| 4. LLMs | A huge neural network trained to guess the next word, billions of times | Answers, translates, writes code | Expensive, can be confidently wrong |

## The math: probability is a fraction

If "going to the" appears 100 times and "store" comes next 40 times:

```
P(store | going to the) = 40 / 100 = 0.4
```

Read it as: *the probability of "store", given that the words before it were "going to the"*.
The `|` bar just means "given". That is the whole formula. Video 6 goes deeper.

## The code

`video01.py` has both programs from the video, commented line by line:

1. `eliza()`: a rule-based chatbot. Try it on sentences the rule does not cover.
2. The counter: slides a 3-word window along the text and counts what comes next.

## Homework

1. Make `eliza()` handle "i am feeling X" and "i'm X" too. How many rules would you need for every way of saying "tired"?
2. Add 5 more sentences to `text`. Do the probabilities change?
3. Set `context = ["going", "to"]`. What changes with less context?
4. Ask the counter about a context it has never seen. What happens? (This is called *sparsity*; video 16 fixes it.)
