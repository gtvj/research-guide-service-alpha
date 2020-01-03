import re

"""
This module gets fragments (lettercode, series and reference) from a given reference
"""

def is_legacy_subclass_series(reference):
    """
    Determines whether the given reference is a legacy subclass series
    :param reference: a reference
    :rtype: bool
    """
    return re.search(r'^(CP 2[456]\/?|IR (12[14-9]|13[0-5])\/?|PRO (3[01]|41|66)\/?)', reference)

def get_fragments(reference):
    """
    Returns fragments for a given reference

    :param reference: a reference
    :return: a dict representing the fragments
    :rtype: dict
    """
    if is_legacy_subclass_series(reference):
        return extract_fragments_from_legacy_sub_class_series(reference)
    else:
        return extract_fragments_from_standard_reference(reference)


def extract_fragments_from_legacy_sub_class_series(reference):
    """
    Returns fragments from a legacy sub class series
    :param reference: a reference
    :return: a dict representing the fragments
    :rtype: dict
    """

    lettercode_match = re.match(r'^(\w*)(\s)?', reference)
    series_match = re.match(r'(\w+\s\d+\/\d+)', reference)

    return {
        "letter_code": lettercode_match.group(1) if lettercode_match else "",
        "series": series_match.group(0) if series_match else "",
        "reference": reference
    }


def extract_fragments_from_standard_reference(reference = False):
    """
    Returns fragments from a standard series
    :param reference: a reference
    :return: a dict representing the fragments
    :rtype: dict
    """
    lettercode_match = re.match(r'^(\w*)(\s)?', reference)
    series_match = re.match(r'(\w+\s\d+)', reference)

    return {
        "letter_code": lettercode_match.group(1) if lettercode_match else "",
        "series": series_match.group(0) if series_match else "",
        "reference": reference
    }