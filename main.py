def standardize_names(name):
    remove_blank_spaces = name.strip()
    split_words =  remove_blank_spaces.split(' ')
    words_len = len(split_words)
    if words_len == 1:
        return remove_blank_spaces
    else:
        return str('-'.join(split_words))

hero_standardized = standardize_names(" Batman     ")
print(hero_standardized)

hero_standardized = standardize_names("      Super Man")
print(hero_standardized)

##########################################################################################################################################################################

def standardize_title(title):
    return title.title()

titles = standardize_title("cinco quartos de laranja")
print(titles)   

##########################################################################################################################################################################

def standardize_text(text):
    line_text = ' '.join(text.split())
    separated_text = line_text.split('. ')
    output = []
    for sentence in separated_text:
        output.append(sentence[0].upper() + sentence[1:])
    return '. '.join(output)

text = """
a famosa atriz Constance Rattigan recebe uma encomenda
desagradável: uma lista com números de telefone de
pessoas que morreram recentemente. é uma coisa assustadora,
considerando que os nomes das poucas pessoas vivas presentes
na lista estão assinalados em vermelho com uma cruz. O da
própria Constance é um deles.
"""


normalized_text = standardize_text(text)
print(normalized_text)

#########################################################################################################################################################################

def title_creator(text):
    return standardize_title(text).center(len(text) + 40, '-')


text = "pense num deserto"

title = title_creator(text)
print(title)


##########################################################################################################################################################################

def text_merge(text_of_blog_a, text_of_blog_b):
    text_of_blog_a = text_of_blog_a[0].upper() + text_of_blog_a[1:]
    text_of_blog_b = text_of_blog_b[0].lower() + text_of_blog_b[1:]

    if text_of_blog_a[len(text_of_blog_a) - 1] == ".":
        text_of_blog_a = text_of_blog_a[:-1]

    whole_text = text_of_blog_a + " " + text_of_blog_b

    clean_text = " ".join(whole_text.split())

    lines = clean_text.split(". ")

    final_text = ""
  
    for line in lines:
            answer = line[0].capitalize() + line [1:] + ". "
            final_text += answer
        
    return final_text[:-2]

text_of_blog_a = """
na Londres do pós-guerra, a escritora     Juliet tenta encontrar
uma   trama para seu novo livro. ela recebe ajuda por meio de uma
   carta de um      desconhecido, um nativo da ilha de Guernsey,
em cujas mãos havia chegado um livro    que há tempos tinha
pertencido    a Juliet.
"""

text_of_blog_b = """
O romance "Cinco Quartos de Laranja" é como   um vinho intenso e
delicado.    usando metáforas culinárias, personagens peculiares
 e acontecimentos sobrenaturais,      Harris cria uma história
complexa e      bela ao mesmo tempo.
"""

merged_text = text_merge(text_of_blog_a, text_of_blog_b)
print(merged_text)