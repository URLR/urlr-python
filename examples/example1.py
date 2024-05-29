import urlr
from urlr.rest import ApiException
from pprint import pprint

# Authentification

with urlr.ApiClient() as api_client:
    authentification_api = urlr.AuthentificationApi(api_client)
    
    authentification_request = urlr.AuthentificationRequest.from_json('{"username": "","password": ""}')

    try:
        api_response = authentification_api.authentification(authentification_request=authentification_request)
    except ApiException as e:
        print("Exception when calling AuthentificationApi->authentification: %s\n" % e)
        quit()

# Link shortening

configuration = urlr.Configuration(
    access_token = api_response.token
)

with urlr.ApiClient(configuration) as api_client:
    link_api = urlr.LinkApi(api_client)
    reduce_link_request = urlr.ReduceLinkRequest.from_json('{"url": "","team_id": ""}')

    try:
        # Reduce a link
        api_response = link_api.reduce_link(reduce_link_request=reduce_link_request)
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LinkApi->reduce_link: %s\n" % e)

# Statistics

with urlr.ApiClient(configuration) as api_client:
    stats_api = urlr.StatsApi(api_client)
    stats_request = urlr.StatsRequest.from_json('{"code": ""}')

    try:
        # Reduce a link
        api_response = stats_api.stats(stats_request=stats_request)
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StatsApi->stats: %s\n" % e)