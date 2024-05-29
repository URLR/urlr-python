import urlr
from urlr.rest import ApiException
from pprint import pprint

# Access Tokens

with urlr.ApiClient() as api_client:
    access_tokens_api = urlr.AccessTokensApi(api_client)
    
    access_tokens_request = urlr.AccessTokensRequest.from_json('{"username": "","password": ""}')

    try:
        api_response = access_tokens_api.create_access_token(access_tokens_request=access_tokens_request)
    except ApiException as e:
        print("Exception when calling AccessTokensApi->create_access_token: %s\n" % e)
        quit()

# Link shortening

configuration = urlr.Configuration(
    access_token = api_response.token
)

with urlr.ApiClient(configuration) as api_client:
    link_api = urlr.LinksApi(api_client)
    create_link_request = urlr.CreateLinkRequest.from_json('{"url": "","team_id": ""}')

    try:
        api_response = link_api.create_link(create_link_request=create_link_request)
        pprint(api_response)
    except Exception as e:
        pprint("Exception when calling LinksApi->create_link: %s\n" % e)

# Statistics

with urlr.ApiClient(configuration) as api_client:
    statistics_api = urlr.StatisticsApi(api_client)
    statistics_request = urlr.StatisticsRequest.from_json('{"link_id": ""}')

    try:
        api_response = statistics_api.statistics(statistics_request=statistics_request)
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StatisticsApi->statistics: %s\n" % e)