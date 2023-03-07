import tabula
from IPython.display import display
import pandas as pd
from datetime import datetime
import requests
from openpyxl import Workbook, load_workbook

# mostra o id do último grupo adicionado
def last_chat_id(token):
    try:
        url = "https://api.telegram.org/bot{}/getUpdates".format(token)
        response = requests.get(url)
        if response.status_code == 200:
            json_msg = response.json()
            for json_result in reversed(json_msg['result']):
                message_keys = json_result['message'].keys()
                if ('new_chat_member' in message_keys) or ('group_chat_created' in message_keys):
                    return json_result['message']['chat']['id']
            print('Nenhum grupo encontrado')
        else:
            print('A resposta falhou, código de status: {}'.format(response.status_code))
    except Exception as e:
        print("Erro no getUpdates:", e)

# enviar mensagens utilizando o bot para um chat específico
def send_message(token, chat_id, message):
    try:
        data = {"chat_id": chat_id, "text": msg}
        url = "https://api.telegram.org/bot{}/sendMessage".format(token)
        requests.post(url, data)
    except Exception as e:
        print("Erro no sendMessage:", e)

# token único utilizado para manipular o bot (não deve ser compartilhado)
token = #coloque seu token do bot aqui

# id do chat que será enviado as mensagens
chat_id = #coloque o seu chat id aqui

#le panilha
planilha = load_workbook("cardapio.xlsx")

aba_ativa = planilha.active

dias_da_semana = [
    'Segunda',
    'Terça',
    'Quarta',
    'Quinta',
    'Sexta'
]

#pega a coluna da tabeka de acordo com o dia da semana
if datetime.today().isoweekday() == 1:
    dia = "C"
if datetime.today().isoweekday() == 2:
    dia = "D"
if datetime.today().isoweekday() == 3:
    dia = "E"
if datetime.today().isoweekday() == 4:
    dia = "F"
if datetime.today().isoweekday() == 5:
    dia = "G"

data_e_hora_atuais = datetime.now()
data_e_hora_em_texto = data_e_hora_atuais.strftime('%d/%m')

#envia cada celula da coluna por mensagem
for celula in aba_ativa[(dia)]:
    if str(dias_da_semana[datetime.today().isoweekday()] + " " + data_e_hora_em_texto) == celula.value:
        msg = celula.value
        print("Passou")
        send_message(token, chat_id, msg)

    else:
        msg = "Cardápio ainda não foi postado"
        send_message(token, chat_id, msg)
        break

