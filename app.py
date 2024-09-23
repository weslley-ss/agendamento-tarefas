from flask import Flask, render_template, request, jsonify
import json
# API DE AGENDAMENTO DE TAREFAS FLASK

# Função para ler e escrever dados no arquivo JSON
def read_json_file(path = 'dados.json' ):
    with open(path, 'r') as file:
        return json.load(file)
def write_json_file(json_text, path = 'dados.json'):
    with open(path, 'w') as f:
        return json.dump(json_text, f)

app = Flask(__name__)

# INDEX
@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

# TODAS TAREFAS
@app.route('/tarefas', methods=['GET'])
def get_all():
    # Leitura do arquivo json
    arq = read_json_file()
    return jsonify(arq["tarefas"])

# TAREFA BY ID 
@app.route('/tarefas/<int:id>', methods=['GET', 'PUT', 'PATCH', 'DELETE'])
def getby_id(id):
    id = str(id)
    # Leitura do arquivo json
    arq = read_json_file()

    if request.method == 'GET':
        if id in arq["tarefas"].keys():
            tarefa = arq["tarefas"][id]
            return tarefa
        else:
            return jsonify({"GET Message": "ID não encontrado!"})
        
    if request.method == 'DELETE':
        if id in arq["tarefas"].keys():
            tarefa = arq["tarefas"][id]
            del arq["tarefas"][id]
            write_json_file(arq)
            return jsonify({"DELETE Message": f"Tarefa \'{tarefa['nome']}\' removida!"})
        else:
            return jsonify({"DELETE Message": "ID não encontrado!"})
    
    if request.method == 'PUT': #Atualização completa
        dados = request.get_json()
        if dados.get('nome') is None or dados['horario'] is None:
            return jsonify({"PUT Message": "Informações de Nome e Horário não foram enviadas!"})

        if id in arq["tarefas"].keys():
            arq["tarefas"][id]['nome'] = dados['nome']
            arq["tarefas"][id]['horario'] = dados['horario']
            write_json_file(arq)
            return jsonify({"PUT Message": f"Tarefa Nº{id} atualizada para \' {arq['tarefas'][id]}\'."})
        else:
            return jsonify({"PUT Message": "ID não encontrado!"})
    
    if request.method == 'PATCH': # Atualização parcial
        dados = request.get_json()
        if dados.get('nome') is None and dados['horario'] is None:
            return jsonify({"PUT Message": "Umas das informações precisão ser enviadas!"})

        if id in arq["tarefas"].keys():
            if dados.get('nome') is not None and dados['horario'] is None:
                arq["tarefas"][id]['nome'] = dados['nome']
                write_json_file(arq)
                return jsonify({"PATCH Message": f"Nome da tarefa Nº{id} atualizado para \'{dados['nome']}\'."})
            if dados.get('nome') is None and dados['horario'] is not None:
                arq["tarefas"][id]['horario'] = dados['horario']
                write_json_file(arq)
                return jsonify({"PATCH Message": f"Horário da tarefa Nº{id} atualizado para \'{dados['horario']}\'."})
        else:
            return jsonify({"PATCH Message": "ID não encontrado!"})
    
# ADD TAREFA
@app.route('/add', methods=['POST'])
def add_tarefa():
    arq = read_json_file()
    tarefas = arq["tarefas"]
    ids = [int(key) for key in tarefas.keys()]
    new_id = str(max(ids) + 1)

    dados = request.get_json()
    if dados.get('nome') is None or dados['horario'] is None:
        return jsonify({"PUT Message": "Informações de Nome e Horário não foram enviadas!"})
    else:
        tarefas[new_id] = dados
        arq["tarefas"] = tarefas
        write_json_file(arq)
        return jsonify({"POST Message": f"Tarefa Nº{new_id} foi criada \' {arq['tarefas'][new_id]}\'."})
    
# Inicializa novamente os conjunto de dados
@app.route('/restart', methods=['GET'])
def reinicia():
    tarefas_start = {
        "tarefas":{
        "1": {"nome": "Café da manhã", "horario": "9:00"},
        "2": {"nome": "Tirar lixo", "horario": "9:30"},
        "3": {"nome": "Almoço", "horario": "12:00"},
        "4": {"nome": "Reunião de trabalho", "horario": "14:00"},
        "5": {"nome": "Lanche da tarde", "horario": "16:00"},
        "6": {"nome": "Exercício físico", "horario": "17:00"},
        "7": {"nome": "Tomar banho", "horario": "18:30"},
        "8": {"nome": "Jantar", "horario": "19:00"},
        "9": {"nome": "Tempo de lazer", "horario": "20:00"},
        "10": {"nome": "Leitura", "horario": "21:00"},
        "11": {"nome": "Preparar para dormir", "horario": "22:30"}
        }
    }
    write_json_file(tarefas_start)
    return "Conjunto de dados reiniciado!"

if __name__ == '__main__':
    app.run(debug=False)