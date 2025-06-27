#dicionario parte 03


usuario = {'Nome': "Alexa Machado", 
          'Idade': 40,
          'email':"alex@gmail.com",
      'Profissão': "programador"
}

#exbir os valores

for chave, valor in usuario:
    print(f"{chave.capitalize()}: {usuario.get(chave)}")

    '''
    Quando Usar Dicionários?
Use quando precisar:

De acesso rápido a valores via chaves

Armazenar dados relacionados (como atributos de um objeto)

Agrupar dados não ordenados com chaves únicas

Se quiser, posso te mostrar exemplos práticos, como:

Um sistema de cadastro simples

Contar palavras em um texto

Tradutor básico
    
    
    '''