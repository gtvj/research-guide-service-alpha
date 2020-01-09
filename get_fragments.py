from urllib import parse
import requests


def get_fragments(reference):
    """"
    Returns fragments for a given reference. Uses the resolver service. See the API docs for the resolver service at:

    https://alpha.nationalarchives.gov.uk/idresolver/apidocs/

    The commit history for this file also has a version that does this parsing without any external dependency.

    :param reference: a reference
    :return: a dict representing the fragments
    :rtype: dict
    """

    url = "https://alpha.nationalarchives.gov.uk/idresolver/lookup/%s" % parse.quote(reference.strip())

    r = requests.get(url)
    data = r.json()

    result = {}

    try:
        result['reference'] = data['canonical'][0]['catalogue_ref']
        result['letter_code'] = data['canonical'][0]['letter_code']

        if data['canonical'][0]['path']['Series']:
            result['series'] = '%s %s' % (data['canonical'][0]['letter_code'], data['canonical'][0]['path']['Series'])
        else:
            result['series'] = ''
            
    except KeyError:
        result['error'] = 'There was a KeyError'

    return result
