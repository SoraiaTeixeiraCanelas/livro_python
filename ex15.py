from sys import argv #Chamar argumentos escritos quando se chamar este ficheiro

script, filename = argv #são estes os argumentos necessarios para iniciar o script

txt = open(filename) #cirar variavel txt que será o file que chamámos no argumento

print(f"Here's your file {filename}:")
print(txt.read()) #printar a variavel txt, lendo o seu interior

print("Type the filename again:")
file_again = input("> ")

txt_again = open(file_again)

print(txt_again.read())
