import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from dotenv import load_dotenv

load_dotenv()

try:
    # ClientCredentials não precisa de login de utilizador (apenas id e secret)
    auth_manager = SpotifyClientCredentials()
    sp = spotipy.Spotify(auth_manager=auth_manager)
    
    # Fazemos uma pesquisa de teste para provar que a API está a funcionar
    resposta = sp.search(q='Eminem', limit=1)
    
    print("\n✅ SUCESSO ABSOLUTO! A Ligação à API funciona!")
    print("O Spotify respondeu, encontrámos o artista:", resposta['tracks']['items'][0]['artists'][0]['name'])

except Exception as e:
    print("Erro grave:", e)
