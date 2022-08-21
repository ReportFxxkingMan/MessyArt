import notion_client
from cred.credentials import NOTION_TOKEN


def set_notion_client(token: str = NOTION_TOKEN) -> notion_client.client.Client:
    """
    Set notion client
    Args:
        token (str)
    Returns:
        notion_client.client.Client
    """
    return notion_client.Client(auth=token)
