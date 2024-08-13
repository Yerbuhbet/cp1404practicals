import wikipedia
from wikipedia.exceptions import DisambiguationError, PageError

def search_wikipedia():
    while True:
        search_phrase = input("Enter page title: ")
        if not search_phrase:
            print("Thank you.")
            break

        try:
            page = wikipedia.page(search_phrase)
            print(f"{page.title}\n{page.summary[:500]}...\n{page.url}\n")
        except DisambiguationError as e:
            print(f"We need a more specific title. Try one of the following, or a new search:\n{e.options}\n")
        except PageError:
            print(f"Page id \"{search_phrase}\" does not match any pages. Try another id!\n")

if __name__ == "__main__":
    search_wikipedia()
