__version__ = 0.1

import requests
import urllib2
import argparse
from bs4 import BeautifulSoup


def get_best_torrent(query):
    query = urllib2.quote(query)
    r = requests.get('http://kat.cr/usearch/{}/'.format(query))
    soup = BeautifulSoup(r.content)
    torrents = soup.find('table', class_='data').find_all(has_class_odd_or_even, limit=5)
    for torrent in torrents:
        name = torrent.find('a', class_='cellMainLink').text.encode('utf-8')
        print "Name: {}".format(name)
        size = torrent.find(class_='nobr center').text
        print "Size: {}".format(size)
        verified = bool(torrent.find('i', class_='ka ka-verify'))
        if verified:
            print "Verified Uploader: True"
        else:
            print "Verified: False"
        seeds = torrent.find(class_='green center').text
        print "Seeds: {}".format(seeds)
        leeches = torrent.find(class_='red lasttd center').text
        print "Leeches: {}".format(leeches)
        try:
            seed_to_leech = float(seeds) / float(leeches)
        except ZeroDivisionError:
            seed_to_leech = int(seeds)
        print "Seed to leech ratio: {}".format(seed_to_leech)
        magnet = torrent.find(class_='iaconbox').find('a', class_='imagnet')['href']
        print "Magnet: \n{}\n".format(magnet)


def has_class_odd_or_even(tag):
    if tag.has_attr('class'):
        if 'odd' in tag.attrs['class'] or 'even' in tag.attrs['class']:
            return True
    return False


def command_line_runner():
    parser = argparse.ArgumentParser(description='Get magnet links for torrents from the CLI')
    parser.add_argument('name', type=str, nargs='*', help='Name of the torrent you are looking for')
    args = parser.parse_args()
    if not args.name:
        parser.print_help()
    else:
        get_best_torrent(' '.join(args.name))


if __name__ == '__main__':
    command_line_runner()
