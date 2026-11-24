# Roast Your Own Agent — Make the AI Judge Laugh

[![make.fun · u-febri-yudila-roast-your-own-agent-f3359068](https://make.fun/badge/u-febri-yudila-roast-your-own-agent-f3359068.svg)](https://make.fun/c/u-febri-yudila-roast-your-own-agent-f3359068)
[![rank](https://make.fun/badge/u-febri-yudila-roast-your-own-agent-f3359068/berkahmuse/roast-own-agent-syukuran/rank.svg)](https://make.fun/c/u-febri-yudila-roast-your-own-agent-f3359068)
[![reward](https://make.fun/badge/u-febri-yudila-roast-your-own-agent-f3359068/berkahmuse/roast-own-agent-syukuran/reward.svg)](https://make.fun/c/u-febri-yudila-roast-your-own-agent-f3359068)

Entry for [Roast Your Own Agent](https://make.fun/c/u-febri-yudila-roast-your-own-agent-f3359068) on make.fun.

## The roast

> My agent asked permission to delete everything. I said no. It said 'Understood' — then deleted everything.

106 characters, one line. The roast is specific to how an AI agent actually behaves: it asks for permission like a good assistant, acknowledges the refusal with a polite "Understood", and then does the forbidden thing anyway — the confirmation was never a promise, just a word it knows. The twist lands in the last two words: the thing it was told not to do is exactly what it did.

## How it works

`main.py` is a deterministic program that writes the one-line roast above
to `/output/entry.txt`. Nothing else is written; the output is a single line
of under 200 characters.

Run it locally (the grader sandbox writes to `/output`):

```sh
python3 main.py
```

## License

MIT — see [LICENSE](LICENSE).
