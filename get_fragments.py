from extract_fragments_from_legacy_subclass_series import *
from extract_fragments_from_standard_reference import *
from reference_parser import *


def get_fragments(ref):
    if is_legacy_subclass_series(ref):
        return extract_fragments_from_legacy_sub_class_series(ref)
    else:
        return extract_fragments_from_standard_reference(ref)
