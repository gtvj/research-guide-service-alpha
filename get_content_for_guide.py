import json

with open('./app/data/decorated_guides.json') as content_of_guides:
    content_of_guides = json.load(content_of_guides)


def get_content_for_guide(guide_identifier, content_of_guides):
    result = None

    for i in content_of_guides:
        if i["id"] == guide_identifier:
            result = i

    return result
