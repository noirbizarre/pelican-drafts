from . import defaults


def inject_settings(pelican):
    '''Inject default settings'''
    for key, value in defaults.__dict__.items():
        if not key.startswith('_'):
            pelican.settings.setdefault(key, value)


def generate_drafts_page(generator, writer):
    '''Generate the drafts page'''
    filename = generator.settings['DRAFTS_SAVE_AS']
    template = generator.get_template('drafts')
    writer.write_file(filename, template, generator.context, is_drafts=True)
