import argparse
from datetime import date
from bibtexparser.bparser import BibTexParser
import urllib.request

parser = argparse.ArgumentParser(description='Extract conflict of interest for a given author')
parser.add_argument('--first', type=str, help='Author first name')
parser.add_argument('--last', type=str, help='Author last name')
parser.add_argument('--sy', type=int, default=date.today().year - 5, help='Start year to consider conflict of interest')
parser.add_argument('--ey', type=int, default=date.today().year, help='End year to consider conflict of interest')

args, _ = parser.parse_known_args()

if __name__ == '__main__':
    file_name = 'papers.bib'
    first_name = args.first
    last_name = args.last
    url = 'https://www.zootle.me/bib?groupID=4672801&privateKey=auSCtFH3Dy7Tz32KhwuLNtg1'

    print('Extracting conflict of interest for {}'.format(first_name + ' ' + last_name))

    # Download bibtex file
    print('Downloading bibtex file...')
    urllib.request.urlretrieve(url, file_name)
    print('Done.')

    with open(file_name) as bibtex_file:
        bibtex_str = bibtex_file.read()

    bp = BibTexParser(interpolate_strings=False)
    bib_db = bp.parse(bibtex_str)

    conflicting_authors = []
    for entry in bib_db.entries:
        authors = entry['author'].split(' and ')
        if last_name + ', ' + first_name in authors:  # conflict of interest
            if args.sy <= int(entry['year']) <= args.ey:
                conflicting_authors = conflicting_authors + authors
        else:  # not conflict of interest
            pass

    # remove duplicates from string list
    conflicting_authors = list(set(conflicting_authors))
    # remove self from list
    conflicting_authors.remove(last_name + ', ' + first_name)
    # sort list alphabetically
    conflicting_authors.sort()

    # write list of conflicting authors to file
    with open('conflicting_authors.txt', 'w') as f:
        f.write('Conflict of interest for {}'.format(first_name + ' ' + last_name) + ' from {} to {}:\n'.format(args.sy,                                                                                              args.ey))
        for author in conflicting_authors:
            f.write(author + '\n')

    print('Results written to conflicting_authors.txt')
