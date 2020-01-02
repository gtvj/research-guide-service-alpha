from get_content_for_guide import *
import json

with open('./app/data/decorated_guides.json') as content_of_guides:
    content_of_guides = json.load(content_of_guides)


def test_get_content_for_guide():
    result = get_content_for_guide('british-army-officers-up-to-1913-further-research', content_of_guides)

    expected = {
        "guide_href": "http://www.nationalarchives.gov.uk/help-with-your-research/research-guides/british-army-officers-up-to-1913-further-research/",
        "name": "British Army officers up to 1913: further research",
        "summary": [
            "This guide covers both: commissioned officers officers who were promoted through the ranks You might find it useful to read the blog Isaac Chetham: From \u2018Scum of the Earth\u2019 to Commissioned Officer in Wellington\u2019s Army which explains the process of researching an Officer in this period.",
            "Selected birth, marriage and death certificates for British Army officers (1755-1908) Browse: WO 32/8903-8920 (1777-1868) for baptismal certificates for British Army officers WO 42 (1755-1908) for certificates of marriage, birth of children, death and burial There are index books in the reading rooms at The National Archives at Kew to identify relevant records.",
            "The supporting documents often contain statements of service, certificates of baptism and letters of recommendation HO 51 (1758-1855) for military entry books WO 103 (1809, 1871-1914) for original submissions and entry books of submissions to the Sovereign of recommendations for staff and senior appointments, and for commissions and appointments Use the index IND 1/8914 to locate records of commissions in SP 44/164 (1679-1782)."
        ],
        "bigrams": [
            [
                [
                    "Army",
                    "officers"
                ],
                7
            ],
            [
                [
                    "British",
                    "Army"
                ],
                11
            ],
            [
                [
                    "WO",
                    "25"
                ],
                5
            ],
            [
                [
                    "half",
                    "pay"
                ],
                6
            ]
        ],
        "references": [
            "WO25",
            "WO25",
            "WO25",
            "PMG3",
            "PMG14",
            "PMG4",
            "PMG4",
            "WO24",
            "WO23",
            "WO61",
            "WO42",
            "WO32",
            "WO42",
            "WO25",
            "WO25",
            "WO31",
            "HO51",
            "WO103",
            "IND1",
            "SP44",
            "WO4",
            "WO74"
        ],
        "trigrams": [
            [
                [
                    "Army",
                    "officers",
                    "1913"
                ],
                3
            ],
            [
                [
                    "British",
                    "Army",
                    "officers"
                ],
                7
            ],
            [
                [
                    "certificates",
                    "British",
                    "Army"
                ],
                3
            ]
        ],
        "id": "british-army-officers-up-to-1913-further-research"
    }

    assert result == expected


def test_get_content_for_guide_which_does_not_exist():
    result = get_content_for_guide('this-guide-is-nonexistent', content_of_guides)

    expected = None

    assert result == expected
