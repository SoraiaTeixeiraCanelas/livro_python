from sys import argv
from os.path import exists

script, from_file, to_file = argv
print(f"Copying from {from_file} to {to_file}")

#juntar estes dois comandos numa linha -> usar ;
in_file = open(from_file); indata = in_file.read()

print(f"The input file is {len(indata)} bytes long")

print(f"Does the output file exist? {exists(to_file)}")
print("Ready, hit RETURN to continue, CTRL-C to abort")
input()

output_file = open(to_file, "w")
output_file.write(indata)

print("Allright, all done")

#output_file.close()
#in_file.close()
#este sript apaga tudo o que o ficheiro in_file tem e copia o conteudo do from_file
