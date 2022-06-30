from bibtexparser.bparser import BibTexParser
import urllib.request
from datetime import date
from flask import Flask, request, send_file
import tempfile


def parse(first, last, start, end):
    url = 'https://vcg.seas.harvard.edu/publications.bib'

    print('Extracting conflict of interest for {}'.format(first + ' ' + last))

    # Download bibtex file
    print('Downloading bibtex file...')
    data = urllib.request.urlopen(url)
    print('Done.')

    # read bibtex string from url
    bibtex_str = data.read().decode('utf-8')

    bp = BibTexParser(interpolate_strings=False)
    bib_db = bp.parse(bibtex_str)

    conflicting_authors = []
    for entry in bib_db.entries:
        authors = entry['author'].split(' and ')
        if last + ', ' + first in authors:  # conflict of interest
            if start <= int(entry['year']) <= end:
                conflicting_authors = conflicting_authors + authors
        else:  # not conflict of interest
            pass

    # remove duplicates from string list
    conflicting_authors = list(set(conflicting_authors))
    # remove self from list
    conflicting_authors.remove(last + ', ' + first)
    # sort list alphabetically
    conflicting_authors.sort()

    # create csv file with conflicting authors
    print('Creating csv file...')
    with open(tempfile.gettempdir() + '/conflict_of_interest.csv', 'w') as f:
        for author in conflicting_authors:
            f.write(author + '\n')
    print('Done.')

    # return file as response
    return send_file('conflict_of_interest.csv', as_attachment=True)

    # authors = "Conflicting authors for {} {} between {} and {}. ".format(first, last, start, end)
    # for author in conflicting_authors:
    #     authors += author + '; \n'
    # return authors


def compile_conflict_of_interest(request):
    """Responds to any HTTP request.
    Args:
        request (flask.Request): HTTP request object.
    Returns:
        The response text or any set of values that can be turned into a
        Response object using
        `make_response <http://flask.pocoo.org/docs/1.0/api/#flask.Flask.make_response>`.
    """

    current_year = date.today().year

    if request.method == 'GET' and 'first' in request.args and 'last' in request.args:
        first = request.args.get('first')
        last = request.args.get('last')
        if 'from' in request.args and 'to' in request.args:
            start = int(request.args.get('from'))
            end = int(request.args.get('to'))
            return parse(first, last, start, end)
        else:
            return parse(first, last, current_year - 5, current_year)

    else:
        return f'Please specify a first and last name'

