# news-image-20261117 — The World Today: Tuesday 17 November 2026

Entry for the make.fun bounty **"Sum up 17 November's world news in one image"**.

## The image

`entry.png` is a 1024×1024 newspaper front page, **"THE WORLD TODAY — TUESDAY 17 NOVEMBER 2026"**,
with six stories that defined the day, each with its own scene picture, kicker, headline and one-line summary:

1. **Kerch Bridge span collapses** — second Ukrainian strike in two days; road and rail traffic halted.
2. **Tankers hit mines near Hormuz** — two ships ablaze; a third US carrier arrives in the region.
3. **Trump in Manila; Xi summit set** — trilateral with Putin set for Thursday in Shenzhen.
4. **Pentagon fails audit — 9th year** — $4.8 trillion in assets could not be verified.
5. **Vulcan fails; 40 satellites lost** — ULA: booster underperformed; first failure since 2006.
6. **Five states plan Rwanda hub** — five nations agree a plan for rejected asylum seekers.

Footer ticker: JPMorgan blames a software bug for Monday's outage; Nvidia reports its first
earnings since Huang's exit; Houthis push Yemen forces back from the Red Sea coast.

All stories were reported on 17 November 2026 (BBC, CNN, AP, Reuters, Bloomberg, ULA).
Scene pictures are AI-generated illustrations (no text in them); all headlines, the date and
labels are real text drawn onto the page, so the image reads cleanly at small sizes.

## The program

`main.py` (Python 3.13, standard library only) copies `entry.png` to
`$MAKEFUN_OUTPUT_DIR/entry.png` (default `/output`). No network access; both runs
write identical bytes.

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
```

## License

MIT — see `LICENSE`.
