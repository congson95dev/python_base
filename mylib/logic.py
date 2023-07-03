"""
This module defines the main entry point of the program.
"""
import wikipedia


def wiki(name="War Goddess", length=1):
    """
    Get a summary of a Wikipedia page.

    Args:
        name (str): The title of the Wikipedia page.
        length (int): The number of sentences to return in the summary.

    Returns:
        str: A summary of the Wikipedia page.
    """
    my_wiki = wikipedia.summary(name, length)
    return my_wiki

def search_wiki(name):
    """Search Wikipedia for Names"""

    results = wikipedia.search(name)
    return results
