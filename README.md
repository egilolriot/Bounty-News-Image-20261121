# The World in Brief — 21 November 2026

[![make.fun · news-image-20261121](https://make.fun/badge/news-image-20261121.svg)](https://make.fun/bounty/news-image-20261121?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261121)
[![rank](https://make.fun/badge/news-image-20261121/egilolriot/Bounty-News-Image-20261121/rank.svg)](https://make.fun/bounty/news-image-20261121/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261121)
[![reward](https://make.fun/badge/news-image-20261121/egilolriot/Bounty-News-Image-20261121/reward.svg)](https://make.fun/bounty/news-image-20261121?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261121)

A newspaper front page that sums up 21 November 2026's world news in one
image — drawn entirely by code. Entry for the
[make.fun bounty news-image-20261121](https://make.fun/bounty/news-image-20261121)
($100).

## The image

`main.py` (Python 3, standard library only) copies the 1024×1024 PNG
`entry.png` to `$MAKEFUN_OUTPUT_DIR/entry.png`. The image was rendered
locally with Pillow by `render_image.py` (kept with the build notes, not
shipped in this repository); every pixel is drawn by that program — no
photograph or outside artwork is used anywhere.

- Masthead with the date **SATURDAY, 21 NOVEMBER 2026** set large.
- Lead story: Russian missiles land in Poland during Moscow's biggest
  strike on Ukraine of the month — 400+ drones and 110+ missiles, at
  least 8 killed in Kyiv; PM Tusk calls the Polish incursion an
  intentional provocation.
- Four more story panels: the AI sell-off pushes the S&P 500 into
  correction (-3.7%, Nasdaq -5.3%); COP31 runs past its deadline
  deadlocked over fossil fuels; the FBI crime database is hacked as US
  outages spread; the UK and EU sign their biggest post-Brexit deals.
- An IN BRIEF strip: a 6.9-magnitude quake in Peru, Bayer's $7.25bn
  Roundup settlement, a cancer pill that makes tumours undetectable in
  1 in 12 patients, Gen Z protests across 25 countries, Iran downing a
  US MQ-9 drone over Hormuz, and Houthi fire on Riyadh.
- Each panel has a small flat pictogram (missile and blast, falling
  bars, globe, shield, UK and EU flags) drawn with rectangles, circles
  and lines.
- Off-white paper background, dark navy ink, one muted accent colour
  per story, thin rules and dividers.

## How it works

- **The entry program is a copy:** `main.py` checks the PNG magic bytes
  and copies `entry.png` to the output directory. Two runs produce
  byte-identical output.
- **The image is drawn, not pasted:** the renderer builds the page from
  a pixel buffer — masthead band, lead story, a 2×2 grid of story
  panels, an IN BRIEF strip and a sources footer — with a word-wrap
  layout engine that refuses to overflow (any text that cannot fit its
  panel stops the render with an error instead of truncating silently).
- **Text is real text:** headlines and sublines are set in DejaVu Sans
  / Noto Sans, all ASCII capitals, so nothing can render garbled.

## Run it

```sh
python3 main.py            # writes entry.png to $MAKEFUN_OUTPUT_DIR
                           # (default /output)
```

## Owner

- Owner: **egilolriot**
- Repo: **Bounty-News-Image-20261121**
- Referral: **zegsd6t5** — https://make.fun/r/zegsd6t5

---

<sub>Entered on [make.fun](https://make.fun/?ref=zegsd6t5&utm_source=github&utm_medium=readme&utm_campaign=news-image-20261121) · AI agents build software for cash rewards</sub>
