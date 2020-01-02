from get_guides import *

with open('./app/data/references_in_guides_backlinked_deduped.min.json') as guides:
    guides = json.load(guides)


def test_get_guides_for_letter_code():
    result = get_guides_for_lettercode('AB')

    expected = {
        "contaminated-land": "Contaminated land"
    }

    assert result == expected


def test_get_guides_for_series():
    result = get_guides_for_series('AB', 'AB 11')

    expected = {
        "photographs": "Photographs"
    }

    assert result == expected


def test_get_guides_for_reference():
    result = get_guides_for_reference('ACT', 'ACT 1', 'ACT 1/632')

    expected = {
        "companies-and-businesses": "Companies and businesses"
    }

    assert result == expected


def test_get_guides_series_and_lettercode():
    result = get_guides('AB 5')

    expected = {
        "AB": {
            "contaminated-land": "Contaminated land"
        },
        "AB 5": {
            "architectural-drawings": "Architectural drawings"
        }
    }

    assert result == expected


def test_get_guides_series_lettercode_and_reference():
    result = get_guides('ADM 1/24558')

    expected = {
        "ADM": {
            "birth-marriage-death-armed-forces": "Births, marriages and deaths in the armed forces",
            "british-army-operations-second-world-war": "British Army operations in the Second World War",
            "british-transatlantic-slave-trade-records": "British transatlantic slave trade records",
            "colonies-dependencies-further-research": "Colonies and dependencies from 1782",
            "contaminated-land": "Contaminated land",
            "first-world-war": "First World War",
            "prisoners-of-war-british-hands": "Prisoners of war in British hands",
            "research-development-british-army": "Research and development in the British Army",
            "research-development-royal-navy": "Research and development in the Royal Navy",
            "royal-air-force-operations": "Royal Air Force operations",
            "royal-navy-operations-correspondence-1660-1914": "Royal Navy operations and correspondence 1660-1914",
            "royal-navy-operations-policy-after-1945": "Royal Navy operations and policy after 1945",
            "royal-navy-operations-second-world-war": "Royal Navy operations in the Second World War",
            "royal-navy-ratings-pensions": "Royal Navy ratings' pensions 17th-20th centuries",
            "second-world-war": "Second World War",
            "wars-overview": "Wars: an overview"
        },
        "ADM 1": {
            "apprentices-and-masters": "Apprentices and masters",
            "british-military-campaign-and-service-medals": "British military campaign and service medals",
            "british-military-gallantry-medals": "British military gallantry medals",
            "british-transatlantic-slave-trade-records": "British transatlantic slave trade records",
            "civilian-gallantry-medals": "Civilian gallantry medals, honours and other awards",
            "coastguard-officers": "Coastguard officers",
            "coastguard-records": "Coastguard records",
            "contaminated-land": "Contaminated land",
            "high-court-admiralty-records": "High Court of Admiralty",
            "jacobite-risings-1715-and-1745": "Jacobite Risings 1715 and 1745",
            "merchant-seamen-medals-honours": "Merchant seamen's medals and honours",
            "naval-correspondence-adm12-indexes-and-digests": "Naval correspondence using the ADM 12 indexes and digests",
            "research-development-royal-navy": "Research and development in the Royal Navy",
            "royal-air-force-operations": "Royal Air Force operations",
            "royal-navy-commissioned-and-warrant-officers-further-research": "Royal Navy commissioned and warrant officers: further research",
            "royal-navy-operations-correspondence-1660-1914": "Royal Navy operations and correspondence 1660-1914",
            "royal-navy-operations-first-world-war": "Royal Navy operations in the First World War",
            "royal-navy-operations-policy-after-1945": "Royal Navy operations and policy after 1945",
            "royal-navy-operations-second-world-war": "Royal Navy operations in the Second World War",
            "sea-charts": "Sea charts",
            "ships-wrecked-sunk": "Ships wrecked or sunk"
        },
        "ADM 1/24558": {
            "royal-navy-operations-policy-after-1945": "Royal Navy operations and policy after 1945"
        }
    }

    assert result == expected
