from trello import TrelloClient

key = "b5cc81c7387b32a6d48949d2e84613b6"
secret = "f8c0a67ad9db3f2e0db2bb27050e6d51b38cabb74bb17ea202122e67541e3fe1"

client = TrelloClient(api_key=key, api_secret=secret)
print(client.list_boards())