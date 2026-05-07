valorLivro = float(input("Informe o valor do livro a ser comprado: "))

desconto = input("Haverá desconto? ")

if desconto == "sim":

    descL = valorLivro*(5/100)
    final = descL+valorLivro
    print("O valor final do livro com desconto é de", final, "reais e houve um desconto de", descL, "reais")

elif desconto == "não":
    
    print("O valor do livro sem descoto é de" , valorLivro, "reais")