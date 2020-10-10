formatter = "{} {} {} {}" #criação de variave formatter com 4 slots de variavies que podem ser preenchidas de diferentes maneiras
print(formatter.format(1, 2, 3, 4))
print(formatter.format("one", "two", "Three", "four"))
print(formatter.format( True, False, False, True))
print(formatter.format(formatter, formatter, formatter, formatter))
print(formatter.format(
      "As rosas são vermelhas",
      "O Ceu é azul",
      "Cenas diversas",
      "Não tenho jeito para isto"
))
