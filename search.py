from youtube_search import YoutubeSearch

def search(key):
    result = YoutubeSearch(search_terms=key).to_dict()
    return result
