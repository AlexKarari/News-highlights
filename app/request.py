import urllib.request, json
from .models import News_sources, News_articles

# Getting api key
api_key = None
# Getting the movie base url
base_url = None


def get_News_sources(sources):
    '''
    Function that gets the json response to our url request
    '''
    get_sources_url = base_url.format(sources, api_key)

    with urllib.request.urlopen(get_sources_url) as url:
        get_sources_data = url.read()
        get_sources_response = json.loads(get_sources_data)

        News_sources_results = None

        if get_sources_response['results']:
            sources_results_list = get_sources_response['results']
            News_sources_results = process_results(sources_results_list)

    return News_sources_results
    

def process_results(source_list):
    '''
    Function  that processes the News_sources_results and transform them to a list of Objects

    Args:
        source_list: A list of dictionaries that contain news sources details

    Returns :
        News_sources_results: A list of news sources objects
    '''
    News_sources_results = []
    for source_item in source_list:
        source_id = source_item.get('id')
        author = source_item.get('author')
        description = source_item.get('description')
        url = source_item.get('url')
        publishedAt = source_item.get('publishedAt')

        source_object = News_sources(source_id, author, description, url, publishedAt)
        News_sources_results.append(source_object)

    return News_sources_results

