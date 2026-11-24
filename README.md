# SomethingTracker

A list of GTA VI PC port attempts, related console runtimes and research tools.

[Repository activity](STATUS.md) · [How tracking works](METHODOLOGY.md)

The list includes reported attempts, not confirmed working ports. Some entries may be forks or inactive projects.

## Contents

- [PC port attempts](#pc-port-attempts)
- [Console runtimes](#console-runtimes)
- [Tools and other trackers](#tools-and-other-trackers)

## PC port attempts

- [ubiquitarianism/leonida](https://github.com/ubiquitarianism/leonida) - Xbox Series → Windows: Separate accessible project; inspect source and history before considering claims.
- [LeonidaReforge/Leonida](https://github.com/LeonidaReforge/Leonida) - Xbox Series → Windows: Community continuation.
- [luizwidmer/palmetto](https://github.com/luizwidmer/palmetto) - Xbox Series → Windows: Continuation project.
- [pixl27/ProjectReCity](https://github.com/pixl27/ProjectReCity) - Xbox Series → Windows: Static recompilation effort.
- [Marvisak/VIctory](https://github.com/Marvisak/VIctory) - Xbox Series → Windows: Game-specific runtime research.
- [ThatRecompDev/five-star-recomp](https://github.com/ThatRecompDev/five-star-recomp) - Xbox Series → Windows: Game-specific toolchain.
- [Kajcsi/G6Recomp](https://github.com/Kajcsi/G6Recomp) - Xbox Series → Windows: Loader / recompilation research.
- [OnlyMoisties/GTA6-BootTest](https://github.com/OnlyMoisties/GTA6-BootTest) - Xbox Series → Windows: Boot assertions are project claims, not independently verified.
- [JamesCicada/GTAVI-Recomp](https://github.com/JamesCicada/GTAVI-Recomp) - PS5 → PC: Based on AnyPS5; no verified game test.
- [SailmakerEnhance/Leonida](https://github.com/SailmakerEnhance/Leonida) - Xbox Series → Windows: Possible fork/derivative; do not count as an independent team without verification.

Previously listed: `ItsNotRexed/Leonida` and `realdody/americas-recomp` were inaccessible on 2026-11-24.

## Console runtimes

- [R0Y00/Xbox2Windows](https://github.com/R0Y00/Xbox2Windows) - Xbox x64 recompilation / graphics translation.
- [ivall/xcl](https://github.com/ivall/xcl) - Xbox Series API compatibility.
- [omonkeyz/xbox-emulator](https://github.com/omonkeyz/xbox-emulator) - Xbox runtime.
- [drycheetah84/TomBox](https://github.com/drycheetah84/TomBox) - Related Xbox compatibility project.
- [californiaAlmonds/OpenScarlett](https://github.com/californiaAlmonds/OpenScarlett) - Xbox Series translation layer.
- [OpenCommunityEdition/OpenScarlett](https://github.com/OpenCommunityEdition/OpenScarlett) - Distinct OpenScarlett implementation.
- [Freminet/ScarlettX](https://github.com/Freminet/ScarlettX) - Xbox Series compatibility.
- [sammwyy/xvalkyrie](https://github.com/sammwyy/xvalkyrie) - Xbox family translation.
- [brcly/TuxBox](https://github.com/brcly/TuxBox) - Linux / Proton path.
- [rpatty-dev/PercyScarlett](https://github.com/rpatty-dev/PercyScarlett) - Scarlett API shims.
- [LooperSalty/AnyXboxX](https://github.com/LooperSalty/AnyXboxX) - GDK loader research.
- [Dark3581/AnyBox](https://github.com/Dark3581/AnyBox) - Console import translation.
- [puffnfresh/rebox](https://github.com/puffnfresh/rebox) - Linux / Wine compatibility.
- [jadeowaowa/scarlett-layer](https://github.com/jadeowaowa/scarlett-layer) - Scarlett loader/shims.
- [boykopovar/AnyPS5](https://github.com/boykopovar/AnyPS5) - PS5 system library translation.

## Tools and other trackers

- [rpatty-dev/PercyStar](https://github.com/rpatty-dev/PercyStar) - Asset exploration.
- [holdmysocks/SixNG](https://github.com/holdmysocks/SixNG) - Archive / format / model research.
- [Ahmet-Dedeler/Percy6Stars](https://github.com/Ahmet-Dedeler/Percy6Stars) - Asset explorer fork.
- [DesignWithTommy/6to5m](https://github.com/DesignWithTommy/6to5m) - Asset conversion to GTA V / FiveM, **not** GTA VI running on PC.
- [Ahmet-Dedeler/bcpack-rs](https://github.com/Ahmet-Dedeler/bcpack-rs) - Texture decoding.
- [Ahmet-Dedeler/awesome-gta6-reverse-engineering](https://github.com/Ahmet-Dedeler/awesome-gta6-reverse-engineering) - Broad reference directory.
- [fishingpvalues/gta6-pc-port-hub](https://github.com/fishingpvalues/gta6-pc-port-hub) - Collaboration and technical blockers.
- [4lwayz/portwatch-vi](https://github.com/4lwayz/portwatch-vi) - Existing status and clone tracker.
- [hubby121/portwatch-vi](https://github.com/hubby121/portwatch-vi) - Tracker; relationship not assumed.
- [alan-r-henry/gta6-pc-tracker](https://github.com/alan-r-henry/gta6-pc-tracker) - Tracks multiple routes to PC.
- [pagiii/gta6-tracker](https://github.com/pagiii/gta6-tracker) - Tracking dashboard.

## Updates

[STATUS.md](STATUS.md) is generated daily from the GitHub API. It records repository availability, last push, stars and open issues/PRs. To refresh locally:

```sh
python scripts/update.py
```

New projects are added to the list manually. See [CONTRIBUTING.md](CONTRIBUTING.md) or open an issue if something is missing or mislabeled.

## Notes

No independently verified playable PC port was established during the initial review (2026-11-24). Repository activity does not establish that a game runs.

No game files, leaked source code, keys or executable downloads are hosted here. Do not treat linked projects or their releases as verified safe. This is an unofficial directory, independent of Rockstar Games and Take-Two Interactive.
