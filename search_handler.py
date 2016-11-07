from pdb import set_trace
import urllib
from lxml import etree

from core.config import Configuration as CoreConfiguration
from config import config as search_handler_config

class Configuration(CoreConfiguration):
    @classmethod
    def load(cls):
        cls.instance = search_handler_config
        return cls.instance

config = Configuration.load()


from core.opensearch import OpenSearchDocument
from core.util.opds_writer import AtomFeed, OPDSFeed
from core.external_search import ExternalSearchIndex

def search_handler(event, context):
    search_url = ""
    input = event.get('input')
    if input:
        request_headers = input.get('Headers')
        if request_headers:
            protocol = request_headers.get('X-Forwarded-Proto', '')
            host = request_headers.get('Host', '')
            path = input.get('path', '')
            search_url = protocol + '://' + host + path

    query = None
    queryStringParameters = event.get('queryStringParameters')
    if queryStringParameters:
        query = event.get('queryStringParameters').get("q")
    if not query:
        return dict(
            statusCode=200,
            headers={},
            body=OpenSearchDocument.for_lane(None, search_url)
        )

    integration = Configuration.integration(
        Configuration.ELASTICSEARCH_INTEGRATION)
    url = integration[Configuration.URL]
    works_index = integration[Configuration.ELASTICSEARCH_INDEX_KEY]
    search_engine = ExternalSearchIndex(url, works_index)

    this_url = search_url + "?q=" + urllib.quote(query.encode('utf8'))
    title = "Search results for %s" % query

    results = search_engine.query_works(
        query, None, None, None, None,
        None, None, None,
        fields=['_id', 'opds_entry'])

    feed = OPDSFeed(title, this_url)

    for result in results['hits']['hits']:
        fields = result['fields']
        entry = fields['opds_entry'][0]
        feed.feed.append(etree.fromstring(entry))

    return dict(
        statusCode=200,
        headers={},
        body=unicode(feed)
    )
