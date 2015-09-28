import collections
import datetime
import functools
import logging
import os
import pprint

import jinja2

import asyncio
import dashi.config
import dashi.db
import dashi.time

LOGGER = logging.getLogger(__name__)

@asyncio.coroutine
def go():
    config = dashi.config.parse()
    template_loader = jinja2.FileSystemLoader(searchpath=config['paths']['template'])
    template_environment = jinja2.Environment(loader=template_loader)

    connection = dashi.db.connection()

    authors = dashi.db.get_all_authors(connection)
    return

    LOGGER.debug(repo_stats)
    try:
        os.mkdir(config['paths']['output'])
    except OSError:
        pass

    template = template_environment.get_template('index.html')
    output = template.render(repo_stats=repo_stats)

    path = os.path.join(config['paths']['output'], 'index.html')
    with open(path, 'w') as f:
        f.write(output)
