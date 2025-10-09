# Split-Kola

A 5x7 (30-keys) split keyboard that uses a TRRS cable for the interconnect.

* Keyboard Maintainer: [PonderSlime](https://github.com/ponderslime)

## Features
* Hotswap Keys
* RGB Backlit Keys 

## Flashing
Try running this command to flash for each half. If it doesn't work, then I probably need to change it to be different...
```
 qmk compile -kb split_kola -km default -bl uf2-split-left
```
after that, plug in the other half.
```
qmk compile -kb split_kola -km default -bl uf2-split-left
```

That being said, I don't know if this does anything. If that is the case, uncomment this line in config.h:
```
#define MASTER_LEFT
```

and comment
```
#define EE_HANDS
```

But yeah! It should work hopefully!