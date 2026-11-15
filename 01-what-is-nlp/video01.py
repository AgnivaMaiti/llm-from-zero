"""Video 1: What is NLP?  Two tiny programs from the video.

Run:  python video01.py
Needs nothing but Python 3 (no installs).

Program 1 = wave one of NLP: RULES (ELIZA, 1966)
Program 2 = wave two of NLP: COUNTING (predict the next word)
"""
import re
from collections import Counter


# ---------------------------------------------------------------------------
# Program 1: a rule-based chatbot, ELIZA style
# ---------------------------------------------------------------------------
def eliza(text):
    # Step 1: lowercase, so "I feel" and "i feel" look the same
    text = text.lower()
    # Step 2: a regular expression = a pattern.  "i feel (.*)" means:
    #   the words "i feel", then (.*) = "capture anything that comes after"
    m = re.match(r"i feel (.*)", text)
    if m:
        # Step 3: m.group(1) is the captured part, e.g. "tired"
        return f"Why do you feel {m.group(1)}?"
    # Step 4: no rule matched, so fall back to a safe answer
    return "Tell me more."


print("=== Program 1: rules ===")
for line in ["I feel tired", "I feel happy today", "I am feeling tired"]:
    print(f"you:   {line}")
    print(f"eliza: {eliza(line)}\n")
# Notice the last one: "I am feeling tired" means the same thing,
# but no rule matches.  That is why rules alone could never handle language.


# ---------------------------------------------------------------------------
# Program 2: next-word prediction by counting
# ---------------------------------------------------------------------------
text = ("i am going to the store . i am going to the gym . "
        "we are going to the store")

words = text.split()          # ['i', 'am', 'going', 'to', 'the', 'store', '.', ...]
context = ["going", "to", "the"]
n = len(context)

counts = Counter()            # a dictionary that counts things, starting at 0
for i in range(len(words) - n):
    # slide a window of 3 words along the text
    if words[i:i + n] == context:
        next_word = words[i + n]
        counts[next_word] += 1

total = sum(counts.values())  # how many times we saw "going to the" at all

print("=== Program 2: counting ===")
print(f"'going to the' was seen {total} times. What came next:")
for word, c in counts.most_common():
    # probability = count / total   (just a fraction!)
    print(f"  P({word} | going to the) = {c}/{total} = {c / total:.2f}")

# ---------------------------------------------------------------------------
# Homework (from the video): change the sentences and see what breaks.
#  1. Add "i feel" variations to eliza(): "i am feeling X", "i'm X".
#  2. Add more sentences to `text`. Does the prediction change?
#  3. Change `context` to ["going", "to"]. What happens with less context?
#  4. What does Program 2 predict for a context it has NEVER seen?
#     (That problem has a name, sparsity, and it is the topic of video 16.)
# ---------------------------------------------------------------------------
