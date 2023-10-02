import wikipedia
from wikipedia import DisambiguationError


def suggest(query: str):
    results = wikipedia.suggest(query)
    print(results)


def search(query: str, num_results: int = 100, suggestion: bool = False):
    results = wikipedia.search(query, num_results, suggestion)
    print(results)


def summary(query: str):
    import warnings

    with warnings.catch_warnings():
        warnings.filterwarnings("ignore", message="No parser was explicitly specified")

        try:
            results = wikipedia.summary(query, auto_suggest=False)
        except DisambiguationError as e:
            results = e.options

    print(results)


def page(query: str):
    page = wikipedia.page(query)
    print(page.title)


if __name__ == '__main__':
    suggest('Bass')
    search('Bass')
    summary('Probability')
    page('Probability')
