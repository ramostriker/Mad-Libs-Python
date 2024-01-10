for i in range(1, 5):
      print('Seja bem vindo ao Mad Libs!\nPara darmos continuidade no jogo, precisarei que me forneça as seguintes informações.')
      nome = str(input('Informe o nome de uma Pessoa: '))
      lugar = str(input('Informe o nome de um Lugar: '))
      lugarenig = str(input('Informe o nome de um Lugar que seja enigmático: '))
      localimag = str(input('Informe um Local Imaginário: '))
      personagem = str(input('Informe um Personagem Intrigante: '))
      objeto = str(input('Informe o nome de um Objeto: '))
      objetosing = str(input('Informe o nome de um Objeto Singular: '))
      adjetivo = str(input('Informe um Adjetivo: '))
      verbo = str(input('Informe um Verbo: '))
      momento = str(input('Informe um Momento do Dia: '))
      figura = str(input('Informe uma Figura Misteriosa: '))

      print(f'\n\nA Noite Inusitada de {nome} no(a) {lugar}\n\n')
      print(f'Naquela {momento}, {nome} decidiu explorar o(a) {lugar}.\n'
            f'Com um(a) {objeto} elegante na mão, ele(a) caminhou até {localimag} e encontrou {personagem}.\n'
            f'O(a) {personagem} olhou para {nome} com olho(os) {adjetivo} e começou a {verbo}.\n'
            f'{nome} ficou intrigado(a) e decidiu {verbo} também.\n\n'
            f'Enquanto {nome} explorava, descobriu uma entrada secreta que levava a um(a) {lugarenig}.\n'
            f'Lá, encontrou {figura} que lhe presenteou com um(a) {objetosing}.\n\n'
            f'Com o(a) {objetosing}, {nome} pôde {verbo} de uma maneira completamente nova.\n'
            f'Ao retornar para casa, {nome} compartilhou discretamente sua fascinante experiência no(a) {lugar}.\n'
            f'Desde então, sempre que alguém menciona {lugar}, {nome} relembra a noite inusitada e os detalhes surreais envolvendo o(a) {personagem} e o(a) {figura}.\n'
            '__________________________________________________________________________________________________________________________________________________________\n\n')
