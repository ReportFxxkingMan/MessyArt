from typing import Any, Dict, Tuple
from dataclasses import dataclass
import notion_client


def _get_col(contents: Dict[str, Any], key: str,) -> Any:
    """
    Get item from contents
    Args:
        contents (Dict[str, Any])
        key (str)
    Returns:
        Any
    """
    try:
        return contents[key]
    except:
        return None


def _get_title(contents: Dict[str, Any], key_name: str,) -> str:
    """
    Get title of notion page
    Args:
        contents (Dict[str, Any])
        key_name (str)
    Return:
        str
    """
    title = _get_col(_get_col(_get_col(contents, "properties"), key_name), "title")
    if len(title) == 0:
        return ""
    else:
        return _get_col(title[0], "plain_text")


def _get_data(client: notion_client.client.Client, database_id: str,) -> Dict[str, Any]:
    """
    Get database contents
    Args:
        client (notion_client.client.Client)
        database_id (str)
    Returns
        Dict[str, Any]
    """
    contents = client.databases.query(**{"database_id": database_id,})
    return contents


def _get_data_keys(
    contents: Dict[str, Any], key_name: str = None,
) -> Tuple(Dict[str, Any], str):
    """
    Get database keys
    Args:
        contents (Dict[str, Any])
        key_name (str)
    Returns:
        Tuple(Dict[str, Any], str)
    """
    _results = _get_col(contents, "results")
    if key_name is None:
        properties_search = _get_col(_results[0], "properties").items()
        for _key, _item in properties_search:
            if _item["id"] == "title":
                key_name = _key
                break

    database_keys = {}
    for _result in _results:
        page_title = _get_title(_result, key_name)
        database_keys.update(
            {page_title: _result["id"],}
        )
    return database_keys, key_name


class GetNotionDatabase:
    def __init__(
        self,
        client: notion_client.client.Client,
        database_id: str,
        key_name: str = None,
    ):
        self.contents = _get_data(client=client, database_id=database_id,)
        self.keys = _get_data_keys(contents=self.contents, key_name=key_name,)

    def __call__(self):
        return {
            "contents": self.contents,
            "keys": self.keys,
        }
