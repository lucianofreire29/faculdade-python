import streamlit as st
import pandas as pd
import numpy as np


st.header("Faculdade Senac CE 2026.2")



if st.sidebar.checkbox("Exibir tabelas"):
    st.header("Tabelas")

    turma_a = {
        "matricula":[100,200,300,400,500],
        "aluno":["Victor Hugo","Natalia","Eric","Rafael", "Denner"],
        "curso":["IA","ADS","SI","IA","ADS"],
        "notas":[10.00,5.55,8.5,9.0,7.5]
    }

    turma_b = {
        "matricula":[600,700,800,900,1000],
        "aluno":["Jose","Marcelo","Rodrigo","Rafaela","Sonia"],
        "curso":["ADS","IA","IA","ADS","SI"],
        "contato":["56314-545","58232-114","5674-445","4562-227","4778-842"],
        "notas":[10.00,6.5,7.8,7.4,8.0]
    }

    df_turma_a = pd.DataFrame(turma_a)
    st.dataframe(df_turma_a)

    df_turma_b = pd.DataFrame(turma_b)
    st.dataframe(df_turma_b)

if st.sidebar.checkbox("Todos os Alunos"):
    st.header("Tabelas")

    dados = pd.concat([df_turma_a,df_turma_b], ignore_index=True)
    st.subheader("Todos Alunos SENAC")
    st.dataframe(dados)


    st.subheader("Top 5 alunos(Ordenados por notas)")
    top_5_notas = dados.sort_values(by="notas",ascending=False).head(5)
    st.dataframe(top_5_notas)


if st.sidebar.checkbox("Exibir graficos"):
    st.header("Gráfico")

    df = pd.DataFrame(
        np.random.rand(2, 3),
        columns=["Aluno", "Cursos", "Semestre"]
    )

    st.dataframe(df)
    st.subheader("Visualização em gráfico")
    st.bar_chart(df)
