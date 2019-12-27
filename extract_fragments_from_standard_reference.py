import re

def extract_fragments_from_standard_reference(reference = False):
    lettercode_match = re.match(r'^(\w*)(\s)?', reference)
    series_match = re.match(r'(\w+\s\d+)', reference)

    return {
        "letter_code": lettercode_match.group(1) if lettercode_match else "",
        "series": series_match.group(0) if series_match else "",
        "reference": reference
    }