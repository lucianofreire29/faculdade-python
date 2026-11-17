import tkinter as tk

contas = [("luciano","123"),("admin","1122")

]

root = tk.Tk()
root.title ("faculdade senac ce")
root.geometry ("1100x600")

tk.Label(root, text="aluno").pack()
aluno_entry = tk.Entry(root)
aluno_entry.pack()



tk.Label(root,text="senha").pack()
senha_entry = tk.Entry(root,show="*")
senha_entry.pack()


def login():
    aluno = aluno_entry.get()
    senha = senha_entry.get()

    if(aluno, senha) in contas:
        mensagem_label["text"] = "Aluno cadastrado com sucesso"
    else:
        mensagem_label["text"] = "Aluno não cadastrado!"

mensagem_label = tk.Label(root,text="")
mensagem_label.pack()

tk.Button(root,text="login",command=login).pack(pady=10)



root.mainloop()