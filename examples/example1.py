import os
import urlr
from urlr.rest import ApiException

username = os.getenv("URLR_API_USERNAME")  # to define on your end
password = os.getenv("URLR_API_PASSWORD")  # to define on your end


# Access Tokens

configuration = urlr.Configuration()

with urlr.ApiClient(configuration) as api_client:
    access_token_api = urlr.AccessTokensApi(api_client)

    create_access_token_request = urlr.CreateAccessTokenRequest(
        username=username,
        password=password,
    )

    try:
        api_response = access_token_api.create_access_token(
            create_access_token_request=create_access_token_request)
    except ApiException as e:
        print("Exception when calling AccessTokensApi->create_access_token: %s\n" % e)
        quit()

configuration.access_token = api_response.token

# Workspaces - get workspace id

with urlr.ApiClient(configuration) as api_client:
    workspaces_api = urlr.WorkspacesApi(api_client)
    try:
        workspaces = workspaces_api.get_teams()
        workspace_id = workspaces.teams[0].id
    except Exception as e:
        print("Exception when calling WorkspacesApi->get_teams: %s\n" % e)

# Create a link

with urlr.ApiClient(configuration) as api_client:
    links_api = urlr.LinksApi(api_client)
    create_link_request = urlr.CreateLinkRequest(
        url="https://github.com/URLR",
        team_id=workspace_id
    )

    try:
        link = links_api.create_link(
            create_link_request=create_link_request)
    except Exception as e:
        print("Exception when calling LinksApi->create_link: %s\n" % e)

# Get statistics

with urlr.ApiClient(configuration) as api_client:
    statistics_api = urlr.StatisticsApi(api_client)
    get_statistics_request = urlr.GetStatisticsRequest(link_id=link.id)

    try:
        api_response = statistics_api.get_statistics(
            get_statistics_request=get_statistics_request)
        print(api_response)
    except Exception as e:
        print("Exception when calling StatisticsApi->get_statistics: %s\n" % e)
