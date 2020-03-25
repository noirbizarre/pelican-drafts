import pytest

from dataclasses import dataclass
from pathlib import Path

from pelican import Pelican
from pelican.settings import read_settings

from drafts import defaults

TEST_DIR = Path(__file__).parent
DATA_PATH = TEST_DIR / 'data'


def get_settings(**kwargs):
    return read_settings(override={k: v for k, v in kwargs.items()})


@dataclass
class Workspace:
    output: 'typing.ANY'
    settings: dict
    pelican: object


@pytest.fixture
def wksp(tmpdir):
    settings = get_settings(
        PATH=DATA_PATH,
        OUTPUT_PATH=tmpdir,
        ARTICLE_PATHS=['articles'],
        PAGE_PATHS=['pages'],
        PLUGINS=['drafts'],
        THEME=DATA_PATH / 'theme',
    )
    pelican = Pelican(settings=settings)
    yield Workspace(tmpdir, settings, pelican)


def test_render_drafts_page(wksp):
    wksp.pelican.run()
    assert (wksp.output / defaults.DRAFTS_SAVE_AS).exists()


def test_pelican_registeration():
    settings = get_settings(PLUGINS=['drafts'])
    Pelican(settings)
