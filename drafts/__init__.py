import pelican

from .generators import inject_settings, generate_drafts_page


def register():
    pelican.signals.initialized.connect(inject_settings)
    pelican.signals.article_writer_finalized.connect(generate_drafts_page)
