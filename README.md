# Pelican Drafts

[![Build Status](https://travis-ci.com/noirbizarre/pelican-drafts.svg?tag=0.1.1)](https://travis-ci.com/noirbizarre/pelican-drafts)

Add a browsable drafts listing fr your Pelican website


## Requirements

Pelican Drafts works with Pelican 4.2+ and Python 3.7+

## Getting started

Install `pelican-drafts` with pip:

```shell
pip install pelican-drafts
```

And enable the plugin in you `pelicanconf.py` (or any configuration file you want to use):

```Python
PLUGINS = [
    '...',
    'drafts',
    '...',
]
```

## Settings

### `SHOW_DRAFTS`

Wether or not to show the drafts page (**default**:  `True`, set it to `False` in your `publishconf.py`)

### `DRAFTS_URL`

URL on which you can consult the drafts page (**default**: `'drafts/'`)

### DRAFTS_SAVE_AS

Path to save the drafts page. It should be consistent with the `DRAFTS_URL` setting (**default**: `'drafts/index.html'`)

## Theming
