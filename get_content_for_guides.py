import json


def load_guide_data():
    """
    Loads guide data from JSON file and returns corresponding dict

    :return: guides
    :rtype: dict
    """
    with open('./app/data/decorated_guides.json') as content_of_guides:
        return json.load(content_of_guides)


def get_content_for_guide(guide_identifier):
    """
    Returns a dict corresponding to the passed guide identifier, otherwise None

    :param guide_identifier: a string representing the key for a guide
    :return: the corresponding guide content
    :rtype: dict
    """
    content_of_guides = load_guide_data()

    result = None

    for i in content_of_guides:
        if i["id"] == guide_identifier:
            result = i

    return result


def get_content_for_multiple_guides(guide_identifier_list):
    """
    Returns content for a number of research guides

    :param guide_identifier_list: a list of guide identifiers
    :return: a list of dicts that represent the guide content
    :rtype: list
    """

    result = []

    for i in guide_identifier_list:
        if get_content_for_guide(i):
            result.append(get_content_for_guide(i))

    return result
