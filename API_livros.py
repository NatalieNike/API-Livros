#API é um lugar para disponibilizar recursos e/ou funcionalidades
#1. Objetivo - Criar um api que disponibiliza a consulta, criação, edição e exclusão de livros.
#2. URL base - localhost.com
#3. Endpoints - (localhost/livros - GET), (localhost/livros - POST), (localhost/livros/id - PUT), (localhost/livros/id - DELETE)


from flask import Flask, jsonify, request

app = Flask(__name__)

livros = [
    {
        'id': 1,
        'título': 'O Senhor do Anéis - A Sociedade do Anel',
        'autor': 'J.R.R Tolkien'
    },
    {
        'id': 2,
        'título': 'Harry Potter e a Pedra Filosofal',
        'autor': 'J.K. Rowlling'
    },
    {
        'id': 3,
        'título': 'Hábitos Atomicos',
        'autor': 'James Clear'
    },
    {
        'id': 4,
        'título': 'Noites Brancas',
        'autor': 'Fiódor Dostoiévski',
    },
    {
        'id': 5,
        'título': 'A Metamorfose',
        'autor': 'Franz Kafka',
    }
]

# Consultar todos - GET (Read)
#Em Flask, o @app.route() é um decorator que diz ao framework:
#“Quando alguém acessar essa URL, execute essa função.”
@app.route('/livros', methods=['GET'])
def obter_livros():
    return jsonify(livros)

# Consultar por ID - GET (Read)
@app.route('/livros/<int:id>', methods=['GET'])
def obter_livro_por_id(id):
    for livro in livros: 
        if livro['id'] == id:
            return jsonify(livro)
    return jsonify({'mensagem': 'Livro não encontrado'}), 404

# Criar novo livro - POST (Create)
@app.route('/livros', methods=['POST'])
def adicionar_livro():
    novo_livro = request.get_json()
    livros.append(novo_livro)
    return jsonify(livros), 201

# Atuallizar um livro existente - PUT (Update)
@app.route('/livros/<int:id>', methods=['PUT'])
def editar_livro(id):
    dados_atualizados = request.get_json()
    for livro in livros:
        if livro['id'] == id:
            # Atualiza apenas os campos título e autor (mantém o id)
            livro['título'] = dados_atualizados.get('título', livro['título'])
            livro['autor'] = dados_atualizados.get('autor', livro['autor'])
            return jsonify(livro)
    return jsonify({'mensagem': 'Livro não encontrado'}), 404

    

# Excluir um livro existente - DELETE (Delete)
@app.route('/livros/<int:id>', methods=['DELETE'])
def excluir_livro(id):
    for indice, livro in enumerate(livros): 
        if livro['id'] == id:
            del livros[indice]
            return jsonify({'mensagem': 'Livro excluído com sucesso!'}), 404
        
if __name__ == '__main__':
    app.run(debug=True)
