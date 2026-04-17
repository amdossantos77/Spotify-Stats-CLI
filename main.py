import spotipy
from spotipy.oauth2 import SpotifyOAuth
from dotenv import load_dotenv

# Carrega as variáveis do ficheiro .env
load_dotenv()

# Configura a autenticação
# redirect_uri_port é a porta onde o nosso servidor local vai escutar
forma_de_entrar = SpotifyOAuth(
    scope="user-read-email",
    redirect_uri="http://127.0.0.1:8080/callback",
    open_browser=True
)

# Cria o cliente do Spotify
sp = spotipy.Spotify(auth_manager=forma_de_entrar)

# Vai buscar os nossos dados de perfil
meus_dados = sp.me()
meu_nome = meus_dados["display_name"]
print("O login funcionou! Olá, " + meu_nome)
