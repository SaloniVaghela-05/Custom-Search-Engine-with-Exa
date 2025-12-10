from exa_py import Exa
import sys

EXA_API_KEY = 'e5256fdd-3d23-4821-8ad5-18111c6a5c29'
INSTAGRAM_DOMAIN = 'https://www.instagram.com'
DEFAULT_RESULTS = 20

def search_instagram_profiles(search_query: str, num_results: int = DEFAULT_RESULTS) -> list:
   
    if not EXA_API_KEY or EXA_API_KEY == 'YOUR_API_KEY_HERE':
        print("Error: API Key is missing or invalid. Please update EXA_API_KEY.")
        return []

    if not search_query:
        print("Error: Search query cannot be empty.")
        return []
    
    try:
        exa = Exa(EXA_API_KEY)
    except Exception as e:
        print(f"Error initializing Exa client: {e}")
        return []
    
    modified_query = f"{search_query} instagram profile" 
    
    print(f"Searching for '{modified_query}' on Instagram...")

    try:
        response = exa.search(
            query=modified_query,
            num_results=num_results,
            type='keyword',
            include_domains=[INSTAGRAM_DOMAIN],
        )
        
        results_list = []
        if response and response.results:
            for result in response.results:
                results_list.append({
                    'title': result.title,
                    'url': result.url
                })
        return results_list

    except Exception as e:
        print(f"An error occurred during the search: {e}")
        return []

if __name__ == '__main__':
    user_query = input('🔍 Enter the name or topic to search on Instagram: ')

    found_results = search_instagram_profiles(user_query)

    print("\n--- 💖 Search Results ---")
    if found_results:
        for i, result in enumerate(found_results):
            print(f'({i+1}) Title: **{result["title"]}**')
            print(f'    URL: {result["url"]}')
            try:
                username = result['url'].split(INSTAGRAM_DOMAIN + '/')[1].strip('/')
                print(f'    *Username Candidate*: @{username}')
            except:
                pass 
            print("-" * 20)
    else:
        print("No results found or an error occurred. Try a different query!")
    
    print("--------------------------\n")