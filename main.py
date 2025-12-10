from exa_py import Exa

exa = Exa('e5256fdd-3d23-4821-8ad5-18111c6a5c29')

query = input('Search here: ')

response = exa.search(
  query,
  num_results=10,
  type='keyword',
  include_domains=['https://www.instagram.com'],
)
for result in response.results:
  print(f'Title: {result.title}')
  print(f'URL: {result.url}')
  print()