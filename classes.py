class Evento:
    def __init__(self, id, nome, data, local, palestrante, descricao):
        self.id = id
        self.nome = nome
        self.data = data
        self.local = local
        self.palestrante = palestrante
        self.descricao = descricao

class Instalacao:
    def __init__(self, id, nome, localizacao, horario, disponibilidade, contato):
        self.id = id
        self.nome = nome
        self.localizacao = localizacao
        self.horario = horario
        self.disponibilidade = disponibilidade
        self.contato = contato

class Clube:
    def __init__(self, id, nome, descricao, agenda, noticias):
        self.id = id
        self.nome = nome
        self.descricao = descricao
        self.agenda = agenda
        self.noticias = noticias

class Servico:
    def __init__(self, id, nome, localizacao, horario, menu, info_saude, procedimentos_seguranca):
        self.id = id
        self.nome = nome
        self.localizacao = localizacao
        self.horario = horario
        self.menu = menu
        self.info_saude = info_saude
        self.procedimentos_seguranca = procedimentos_seguranca

class Transporte:
    def __init__(self, id, tipo, horario, rota, estacionamento, compartilhamento_bicicletas):
        self.id = id
        self.tipo = tipo
        self.horario = horario
        self.rota = rota
        self.estacionamento = estacionamento
        self.compartilhamento_bicicletas = compartilhamento_bicicletas
