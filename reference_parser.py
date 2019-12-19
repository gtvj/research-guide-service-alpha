import re

def is_legacy_subclass_series(reference):
    return re.search('^(CP 2[456]\/?|IR (12[14-9]|13[0-5])\/?|PRO (3[01]|41|66)\/?)', reference)