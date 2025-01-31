from imap_tools import MailBox, A

# Dados para conexão
username = "seu_email@gmail.com" #Digite seu email
senha = "sua_senha_de_app" #Digite sua senha

# Especificar o remetente
remetente_especifico = "remetente@exemplo.com" #Digite o email do remetente à ser excluido

# Conectar ao servidor IMAP
with MailBox("imap.gmail.com").login(username, senha, 'INBOX') as meu_email:
    # Buscar e-mails do remetente específico
    emails_para_excluir = meu_email.fetch(A(from_=remetente_especifico))

    for email in emails_para_excluir:
        print(f"Excluindo: {email.subject} de {email.from_}")
        # Excluir o e-mail
        meu_email.delete(email.uid)

    print("Processo de exclusão concluído.")