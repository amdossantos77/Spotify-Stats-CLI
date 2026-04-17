import spotipy
from spotipy.oauth2 import SpotifyOAuth
from dotenv import load_dotenv

load_dotenv()

# Dizer ao Spotify como queremos entrar (nós definimos o "scope", que é literalmente a permissão que pedimos ao utilizador, tipo: "só quero ler dados")
forma_de_entrar = SpotifyOAuth(scope="user-read-currently-playing")

# Criamos o "controle remoto" do spotify usando a nossa forma de entrar
sp = spotipy.Spotify(auth_manager=forma_de_entrar)

# E agora fazemos o teste de fogo: vamos pedir os dados do nosso próprio perfil!
meus_dados = sp.me()
meu_nome = meus_dados["display_name"]
print("O login funcionou! Olá, " + meu_nome)