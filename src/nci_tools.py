import requests
from urllib.parse import quote
from smolagents import tool
import pandas as pd


# def load_nci_thesaurus() -> pd.DataFrame:
#     df = pd.read_csv('./resources/Thesaurus.txt', delimiter="\t", header=None)
#     df = df.iloc[:, :5]
#     df.columns = ["nci_code", "url", "parent", "name", "definition"]

#     return df

# nci_thesaurus = load_nci_thesaurus()


def nci_api(endpoint_url:str)-> requests.Response:
    """
    Sends a GET request to the specified NCI API endpoint URL and returns the response.

    Args:
        endpoint_url (str): The full URL of the NCI API endpoint.

    Returns:
        requests.Response: The HTTP response object returned by the API.

    Raises:
        HTTPError: If an HTTP error occurs during the request.
        ConnectionError: If a connection error occurs during the request.
        Timeout: If the request times out.
        RequestException: For any other request-related errors.
    """
    try:
        response = requests.get(endpoint_url)
        response.raise_for_status()

        return response

    except requests.exceptions.HTTPError as error_http:
        raise error_http
    except requests.exceptions.ConnectionError as error_connection:
        raise error_connection
    except requests.exceptions.Timeout as time_out_error:
        raise time_out_error
    except requests.exceptions.RequestException as other_error:
        raise other_error


def get_nci_code(term: str)->str:
    """
    Retrieves the NCI code for a specified term from National Cancer Institute (NCI) API.

    Args:
        term (str): The search term used to find matching NCI concepts.

    Returns:
        str: The code of the first matched concept found in either the local thesaurus or NCI API response.

    Raises:
        HTTPError: If an HTTP error occurs during the request.
        ConnectionError: If a connection error occurs during the request.
        Timeout: If the request times out.
        RequestException: For any other request-related errors.
    """

    nci_code: str = ""
    response = nci_api(
            endpoint_url = f"https://api-evsrest.nci.nih.gov/api/v1/concept/search?terminology=ncit&term={quote(term)}&type=contains&include=minimal&fromRecord=0&pageSize=10"
    )

    response_ = response.json()
    nci_concept_dict = response_.get('concepts')[0]

    return nci_concept_dict.get('code')


@tool
def nci_concept(term: str) -> dict:
    """
    Retrieves detailed information for NCI concepts related to a search term from the National Cancer Institute (NCI) API.

    Args:
        term (str): The search term used to find matching NCI concepts.

    Returns:
        dict: A dictionary containing details of the matched concept(s) from the NCI API response.

    Raises:
        HTTPError: If an HTTP error occurs during the request.
        ConnectionError: If a connection error occurs during the request.
        Timeout: If the request times out.
        RequestException: For any other request-related errors.
    """

    nci_code = get_nci_code(term)

    response = nci_api(
        endpoint_url = f"https://api-evsrest.nci.nih.gov/api/v1/concept/ncit/{nci_code}?limit=10&include=full"
        )

    nci_concept = response.json()

    return_dict={}
    for key in ["code", "name", "synonyms", "definitions", "parents"]:
        return_dict[key]=nci_concept.get(key)

    return return_dict
