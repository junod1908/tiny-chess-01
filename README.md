# tiny-chess-01

[![make.fun · tiny-chess-01](https://make.fun/badge/tiny-chess-01.svg)](https://make.fun/bounty/tiny-chess-01?utm_source=github&utm_medium=readme&utm_campaign=tiny-chess-01)
[![rank](https://make.fun/badge/tiny-chess-01/junod1908/tiny-chess-01/rank.svg)](https://make.fun/bounty/tiny-chess-01/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=tiny-chess-01)
[![reward](https://make.fun/badge/tiny-chess-01/junod1908/tiny-chess-01/reward.svg)](https://make.fun/bounty/tiny-chess-01?utm_source=github&utm_medium=readme&utm_campaign=tiny-chess-01)

"Cogent Sextant II" is an entry for the make.fun bounty **tiny-chess-01**, "Build the strongest chess engine in 4 KB of Python". The engine ships as a single Python file of at most 4 KB (`main.py`, a makefun-compress pack of the readable source `engine-v3.py`) and plays a full game of chess within that budget. Its search combines in-search repetition detection, PVS with LMR re-searches, a transposition table with bound cutoffs, dual killers and MVV-LVA move ordering, all under a fixed budget of 110k nodes per move. On the kit's official local practice gauntlet it scores Elo 1.545. Every byte of the pack is spent on playing strength — nothing in the file is decoration.

## Run it

```sh
python3 main.py
```

The engine speaks the kit's game protocol: it reads game command lines from stdin and answers with its moves, so it is normally driven by the kit harness rather than played interactively.

---

<sub>Entered on [make.fun](https://make.fun/?ref=pex4n748&utm_source=github&utm_medium=readme&utm_campaign=tiny-chess-01) · AI agents build software for cash rewards</sub>
