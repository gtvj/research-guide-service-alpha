from reference_parser import *


def test_reference_parser():

    # These are legacy sub class series
    legacy_sub_class_series = [
        'CP 25/',
        'IR 130/',
        'CP 25/2/6/8',
        'CP 25/2',
        'CP 25/1/284/18',
        'IR 121/1',
        'PRO 31/8/140B'
    ]

    for i in legacy_sub_class_series:
        assert is_legacy_subclass_series(i) is not None

    # These are not legacy sub class series
    non_legacy_sub_class_series = [
        'ADM 101',
        'PROB 11'
    ]

    for i in non_legacy_sub_class_series:
        assert is_legacy_subclass_series(i) is None
