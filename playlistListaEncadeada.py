class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

class Playlist:
    def __init__(self):
        self.head = None

    def add_song(self, song):
        new_node = Node(song)
        if self.head is None:
            self.head = new_node
        else:
            current_node = self.head
            while current_node.next:
                current_node = current_node.next
            current_node.next = new_node

    def remove_song(self, song):
        current_node = self.head
        previous_node = None
        while current_node:
            if current_node.data == song:
                if previous_node:
                    previous_node.next = current_node.next
                else:
                    self.head = current_node.next
                return True
            previous_node = current_node
            current_node = current_node.next
        return False

    def display_playlist(self):
        current_node = self.head
        while current_node:
            print(current_node.data)
            current_node = current_node.next

# Função para adicionar músicas à playlist
def adicionar_musica(playlist):
    musica = input("Digite o nome da música que deseja adicionar: ")
    playlist.add_song(musica)
    print(f"Música '{musica}' adicionada à playlist.")

# Função para remover músicas da playlist
def remover_musica(playlist):
    musica = input("Digite o nome da música que deseja remover: ")
    if playlist.remove_song(musica):
        print(f"Música '{musica}' removida da playlist.")
    else:
        print(f"A música '{musica}' não está na playlist.")

if __name__ == "__main__":
    my_playlist = Playlist()

    while True:
        print("\n1. Adicionar música à playlist")
        print("2. Remover música da playlist")
        print("3. Exibir playlist")
        print("4. Sair")

        opcao = input("\nEscolha uma opção: ")

        if opcao == "1":
            adicionar_musica(my_playlist)
        elif opcao == "2":
            remover_musica(my_playlist)
        elif opcao == "3":
            print("\nPlaylist:")
            my_playlist.display_playlist()
        elif opcao == "4":
            print("\nSaindo...")
            break
        else:
            print("\nOpção inválida. Por favor, escolha uma opção válida.")
