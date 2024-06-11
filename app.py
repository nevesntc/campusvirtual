from flask import Flask, render_template, g
from classes import Evento
from classes import Transporte
from classes import Servico
from classes import Clube
from classes import Instalacao

app = Flask(__name__)

eventos = [
    Evento(1, 'Palestra de Abertura', '01/06/2024', 'Auditório Central', 'Márcio Tannure', 'Palestra de abertura do semestre'),
    Evento(2, 'Workshop de Python', '05/06/2024', 'Laboratório de Informática 1', 'Prof. Ana Souza', 'Introdução à programação em Python')
]
instalacoes = [
    Instalacao(1, 'Biblioteca Central', 'Bloco A, 1º andar', 'Segunda a sexta: 08:00 - 22:00', 'Salas de estudo disponíveis', 'contato@bibliotecacentral.com'),
    Instalacao(2, 'Laboratório de Química', 'Bloco B, 2º andar', 'Segunda a sexta: 09:00 - 18:00', 'Disponível para aulas práticas', 'contato@labquimica.com')
]
clubes = [
    Clube(1, 'Clube de Teatro', 'Promove atividades teatrais e peças durante o ano letivo', 'Consultar agenda do clube', 'Última peça ganhou prêmio nacional'),
    Clube(2, 'Clube de Música', 'Oferece aulas de instrumentos musicais e promove shows no campus', 'Consultar agenda do clube', 'Novo álbum sendo produzido')
]
servicos = [
    Servico(1, 'Restaurante Universitário', 'Próximo ao bloco D', 'Segunda a sexta: 11:00 - 14:00', 'Cardápio variado', 'Equipe médica disponível', 'Procedimentos de segurança em conformidade com as normas'),
    Servico(2, 'Centro de Saúde', 'Bloco E, 1º andar', 'Segunda a sexta: 08:00 - 18:00', 'Consulta médica e odontológica', 'Atendimento emergencial 24 horas', 'Procedimentos de segurança rigorosos')
]
transporte = [
    Transporte(1, 'Ônibus', 'Segunda a sexta: 07:00 - 22:00', 'Rotas internas e externas', 'Estacionamento disponível próximo aos pontos', 'Não disponível'),
    Transporte(2, 'Bicicleta', 'Acesso 24 horas', 'Rotas internas', 'Estacionamento para bicicletas disponível', 'Compartilhamento de bicicletas disponível mediante cadastro')
]

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/eventos')
def listar_eventos():
    return render_template('eventos.html', eventos=eventos)

@app.route('/instalacoes')
def listar_instalacoes():
    return render_template('instalacoes.html', instalacoes=instalacoes)

@app.route('/clubes')
def listar_clubes():
    return render_template('clubes.html', clubes=clubes)

@app.route('/servicos')
def listar_servicos():
    return render_template('servicos.html', servicos=servicos)

@app.route('/transporte')
def listar_transporte():
    return render_template('transporte.html', transporte=transporte)

@app.route('/<tipo>/<int:id>')
def detalhes_item(tipo, id):
    item = None
    if tipo == 'evento':
        lista = eventos
    elif tipo == 'instalacao':
        lista = instalacoes
    elif tipo == 'clube':
        lista = clubes
    elif tipo == 'servico':
        lista = servicos
    elif tipo == 'transporte':
        lista = transporte
    else:
        return "<h1>Ops! Tipo de item não reconhecido!</h1>"

    for i in lista:
        if i.id == id:
            return render_template(f"detalhes_{tipo}.html", item=i)

    return "<h1>Ops! Item não encontrado!</h1>"

if __name__ == '__main__':
    app.run(debug=True)
