from get_fragments import *
from get_fragments import extract_fragments_from_legacy_sub_class_series, extract_fragments_from_standard_reference


def test_get_fragments():

    simple_references = [
        { "reference": "ADM 104/140", "expected_letter_code": "ADM", "expected_series": "ADM 104"},
        { "reference": "AB ", "expected_letter_code": "AB", "expected_series": ""},
        {"reference": "CP 25/1/284/18", "expected_letter_code": "CP",
            "expected_series": "CP 25/1"},
        { "reference": "AB", "expected_letter_code": "AB", "expected_series": ""}
    ]

    for reference in simple_references: 

        fragments = get_fragments(reference["reference"])

        assert fragments["letter_code"] == reference["expected_letter_code"]
        assert fragments["series"] == reference["expected_series"]


def test_extract_fragments_from_legacy_subsclass_series():

    legacy_subclass_series = [
        {"reference": "CP 25/1/284/18", "expected_letter_code": "CP",
            "expected_series": "CP 25/1"}
    ]

    for example_ref in legacy_subclass_series:

        result = extract_fragments_from_legacy_sub_class_series(example_ref["reference"])

        assert result["letter_code"] == example_ref["expected_letter_code"]
        assert result["reference"] == example_ref["reference"]
        assert result["series"] == example_ref["expected_series"]


def test_extract_fragments_from_standard_reference():

    simple_references = [
        {"reference": "ADM 104/140", "expected_letter_code": "ADM",
            "expected_series": "ADM 104"},
        {"reference": "AB ", "expected_letter_code": "AB", "expected_series": ""},
        {"reference": "AB", "expected_letter_code": "AB", "expected_series": ""}
    ]

    for example_ref in simple_references:

        result = extract_fragments_from_standard_reference(example_ref["reference"])

        assert result["letter_code"] == example_ref["expected_letter_code"]
        assert result["reference"] == example_ref["reference"]
        assert result["series"] == example_ref["expected_series"]