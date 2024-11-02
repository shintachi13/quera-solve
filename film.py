n = int(input())

list_film = []
for i in range(n):
    i = input()
    list_film.append(i.title())
print("\n".join(list_film))