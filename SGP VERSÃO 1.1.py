from tkinter import *
from datetime import datetime
import mysql.connector

'''''''''''''''''''''''''''''''''''''''    TUDO SOBRE CADASTRO, NÃO MEXE MAIS     '''''''''''''''''''''''''''''''''''''''''''''''''''

'''Tela de Cadastro começo'''
def Cad_Cliente():    
    interface2=Tk() # Container Cliente
    def inserir1():
        a=et1.get()
        b=et2.get()
        if a!="" and b!="":
            cnx = mysql.connector.connect(user='root', password='root', port='3311',
                                  host='127.0.0.1',
                                  database='sgp')
            cursor = cnx.cursor()

            query = "insert into Cliente (Nome_Cliente, Cidade_Cliente) values (%s,%s)"

            cliente=(a,b)
    

            cursor.execute(query,cliente)

            cursor.close()
            cnx.close()

            lbCad["text"]="Cadastrado com sucesso!"
        
        else:
            lbCad["text"]="Por favor preencha todos os campos!"
            
    def VoltarCli():
        interface2.destroy()

    btFec=Button(interface2,width = 10, text="Voltar", command=VoltarCli)
    btFec.place(x=100,y=160)
    
    lb2=Label(interface2,text = "Nome do Cliente:")
    lb2.place(x=100,y=200)
    
    et1=Entry(interface2,width=60)
    et1.place(x=100,y=220)

    lb3=Label(interface2,text = "Cidade:")
    lb3.place(x=100,y=240)
    
    et2=Entry(interface2,width=60)
    et2.place(x=100,y=260)

    bt5=Button(interface2,width = 50, text="CADASTRAR", command=inserir1)
    bt5.place(x=100,y=285)

    lbCad=Label(interface2,text = "")
    lbCad.place(x=100,y=320)
    
    interface2.geometry("800x500+100+100")
    interface2.mainloop()
    


def Cad_Fornecedor():
    interface3=Tk() # Container Fornecedor

    def inserir2():
        c=et3.get()
        d=et4.get()
        if c!="" and d!="":
            cnx = mysql.connector.connect(user='root', password='root', port='3311',
                                  host='127.0.0.1',
                                  database='sgp')
            cursor = cnx.cursor()

            query = "insert into Fornecedor (Nome_Forn, End_Forn) values (%s,%s)"

            forn=(c,d)
    

            cursor.execute(query,forn)

            cursor.close()
            cnx.close()

            lbCad["text"]="Cadastrado com sucesso!"        

        else:
            lbCad["text"]="Por favor preencha todos os campos!"
    def VoltarForn():
        interface3.destroy()

    btFeF=Button(interface3,width = 10, text="Voltar", command=VoltarForn)
    btFeF.place(x=100,y=160)
    
            
    lb4=Label(interface3,text = "Nome do Fornecedor:")
    lb4.place(x=100,y=200)
    
    et3=Entry(interface3,width=60)
    et3.place(x=100,y=220)

    lb5=Label(interface3,text = "Endereço:")
    lb5.place(x=100,y=240)
    
    et4=Entry(interface3,width=60)
    et4.place(x=100,y=260)

    bt6=Button(interface3,width = 50, text="CADASTRAR", command=inserir2)
    bt6.place(x=100,y=285)

    lbCad=Label(interface3,text = "")
    lbCad.place(x=100,y=320)

    interface3.geometry("800x500+100+100")
    interface3.mainloop()

def Cad_Produto():
    interface4=Tk() # Container Produto
    
    def inserir3():
        e=et5.get()
        f=et6.get()
        g=et7.get()
        if e!="" and f!="" and g!="":        
            cnx = mysql.connector.connect(user='root', password='root', port='3311',
                                  host='127.0.0.1',
                                  database='sgp')
            cursor = cnx.cursor()

            query = "insert into Produto (Nome_Produto, Unid_Produto, Valor_Unit) values (%s,%s,%s)"

            prod=(e,f,g)
    

            cursor.execute(query,prod)

            cursor.close()
            cnx.close()
            
            lbCad["text"]="Cadastrado com sucesso!"    
        else:
            lbCad["text"]="Por favor preencha todos os campos!"
            
    def VoltarProd():
        interface4.destroy()

    btFeP=Button(interface4,width = 10, text="Voltar", command=VoltarProd)
    btFeP.place(x=100,y=160)
    

    lb6=Label(interface4,text = "Nome Produto:")
    lb6.place(x=100,y=200)
    
    et5=Entry(interface4,width=60)
    et5.place(x=100,y=220)

    lb7=Label(interface4,text = "Unid do Produto(kg/L/Qtd embalagem):")
    lb7.place(x=100,y=240)
    
    et6=Entry(interface4,width=60)
    et6.place(x=100,y=260)

    lb8=Label(interface4,text = "Valor do Produto(R$):")
    lb8.place(x=100,y=280)
    
    et7=Entry(interface4,width=60)
    et7.place(x=100,y=300)

    bt7=Button(interface4,width = 50, text="CADASTRAR", command=inserir3)
    bt7.place(x=100,y=315)

    lbCad=Label(interface4,text = "")
    lbCad.place(x=100,y=350)

    interface4.geometry("800x500+100+100")
    interface4.mainloop()
    
def Cad_Pedido():
    interface5=Tk() # Container Pedido

    def inserir4():
        h=et8.get()
        i=et9.get()
        j=et10.get()
        k=et11.get()
        l=et12.get()

        if h!="" and i!="" and j!="" and k!="" and l!="":
            cnx = mysql.connector.connect(user='root', password='root', port='3311',
                                  host='127.0.0.1',
                                  database='sgp')
            cursor = cnx.cursor()

            query = "insert into Pedido (Data_Entrega,Cod_Cliente,Cod_Forn,Cod_Produto,Qntd_Produto) values (%s,%s,%s,%s,%s)"

            ped=(datetime.strptime(h,"%d/%m/%Y").date(),i,j,k,l)
    

            cursor.execute(query,ped)

            cursor.close()
            cnx.close()
    
            lbCad["text"]="Cadastrado com sucesso!"
        else:
            lbCad["text"]="Por favor preencha todos os campos!"
    def VoltarPed():
        interface5.destroy()

    btFec=Button(interface5,width = 10, text="Voltar", command=VoltarPed)
    btFec.place(x=100,y=160)
    
    
    lb9=Label(interface5,text = "Data do Pedido(dd/mm/yyyy):")
    lb9.place(x=100,y=200)
    
    et8=Entry(interface5,width=60)
    et8.place(x=100,y=220)

    lb10=Label(interface5,text = "Código do Cliente:")
    lb10.place(x=100,y=240)
    
    et9=Entry(interface5,width=60)
    et9.place(x=100,y=260)

    lb11=Label(interface5,text = "Código do Produto:")
    lb11.place(x=100,y=280)
    
    et10=Entry(interface5,width=60)
    et10.place(x=100,y=300)

    lb12=Label(interface5,text = "Código do Fornecedor:")
    lb12.place(x=100,y=320)
    
    et11=Entry(interface5,width=60)
    et11.place(x=100,y=340)
    
    lb13=Label(interface5,text = "Quantidade do Pedido:")
    lb13.place(x=100,y=360)
    
    et12=Entry(interface5,width=60)
    et12.place(x=100,y=380)

    bt8=Button(interface5,width = 50, text="CADASTRAR", command=inserir4)
    bt8.place(x=100,y=400)

    lbCad=Label(interface5,text = "")
    lbCad.place(x=100,y=435)

    interface5.geometry("800x500+100+100")
    interface5.mainloop()
'''Tela de Cadastro fim'''
"""""""""""""""""""""""""""""""""""""""""""""""Tela de Busca"""""""""""""""""""""""""""""""""""""""""""""""

def Botao_pesquisa():    
    interface6=Tk() # Container Cliente
# Função para pesquisa de cliente



    def bd_pesquisaCliente():
        lb15["text"] = ""
        lb16["text"] = ""
        lb17["text"] = ""
        lb18["text"] = ""
        lb19["text"] = ""
        lb20["text"] = ""
        lb21["text"] = ""
        lb22["text"] = ""
        lb23["text"] = ""
        lb24["text"] = ""
        lb25["text"] = ""
        lb26["text"] = ""
        lb27["text"] = ""
        lb28["text"] = ""
        
        m=et13.get() # por codigo
        n=et15.get() # por nome
 
        cnx = mysql.connector.connect(user='root', password='root', port='3311',
                                  host='127.0.0.1',
                                  database='sgp')
        if m!="":
            cursor = cnx.cursor()
            query = "select * from Cliente where Cod_Cliente ="+ m

    

            cursor.execute(query)

            linha = cursor.fetchone()
            count = cursor.rowcount
            
            if count>0:
                lb15["text"] = linha [0]
                lb16["text"] = linha [1]
                lb17["text"] = linha [2]

                lb22["text"] = "Código do Cliente:"
                lb23["text"] = "Nome do Cliente:"
                lb24["text"] = "Cidade do Cliente:"
                cursor.close()
            else:
                lb20["text"] = "Erro! Cliente não encontrado"
            cnx.close()
        if n!="":
            cursor = cnx.cursor()
            query = "select * from Cliente where Nome_Cliente like '%" + n + "%'"

    

            cursor.execute(query)

            linha = cursor.fetchone()
            count = cursor.rowcount
            if count>0:
                lb15["text"] = linha [0]
                lb16["text"] = linha [1]
                lb17["text"] = linha [2]
                
                lb22["text"] = "Código do Cliente:"
                lb23["text"] = "Nome do Cliente:"
                lb24["text"] = "Cidade do Cliente:"
                
                cursor.close()
            else:
                lb21["text"] = "Erro! Cliente não encontrado"
            cnx.close()
        global o
        global p
        global q
        o="Cliente"
        p="Cod_Cliente"
        q=str(lb15["text"])
        print(o+', '+p+', '+q)
#função para pesquisa de fornecedor
    def bd_pesquisaFornecedor():
        lb15["text"] = ""
        lb16["text"] = ""
        lb17["text"] = ""
        lb18["text"] = ""
        lb19["text"] = ""
        lb20["text"] = ""
        lb21["text"] = ""
        lb22["text"] = ""
        lb23["text"] = ""
        lb24["text"] = ""
        lb25["text"] = ""
        lb26["text"] = ""
        lb27["text"] = ""
        lb28["text"] = ""        
        m=et13.get() # por codigo
        n=et15.get() # por nome
 
        cnx = mysql.connector.connect(user='root', password='root', port='3311',
                                  host='127.0.0.1',
                                  database='sgp')
        if m!="":
            cursor = cnx.cursor()
            query = "select * from Fornecedor where Cod_Forn ="+ m

    

            cursor.execute(query)

            linha = cursor.fetchone()
            count = cursor.rowcount
            
            if count>0:
                lb15["text"] = linha [0]
                lb16["text"] = linha [1]
                lb17["text"] = linha [2]
                
                lb22["text"] = "Código do Fornecedor:"
                lb23["text"] = "Nome do Fornecedor:"
                lb24["text"] = "Endereço do Forncedor:"
                cursor.close()
            else:
                lb20["text"] = "Erro! Fornecedor não encontrado"
            cnx.close()
        if n!="":
            cursor = cnx.cursor()
            query = "select * from Fornecedor where Nome_Forn like '%" + n + "%'"

    

            cursor.execute(query)

            linha = cursor.fetchone()
            count = cursor.rowcount
            if count>0:
                lb15["text"] = linha [0]
                lb16["text"] = linha [1]
                lb17["text"] = linha [2]
                lb22["text"] = "Código do Fornecedor:"
                lb23["text"] = "Nome do Fornecedor:"
                lb24["text"] = "Endereço do Forncedor:"
                cursor.close()
            else:
                lb21["text"] = "Erro! Fornecedor não encontrado"
            cnx.close()
        global o
        global p
        global q
        o = "Fornecedor"
        p = "Cod_Forn"
        q = str(lb15["text"])
#função pesquisa de produto            
    def bd_pesquisaProduto():
        lb15["text"] = ""
        lb16["text"] = ""
        lb17["text"] = ""
        lb18["text"] = ""
        lb19["text"] = ""
        lb20["text"] = ""
        lb21["text"] = ""
        lb22["text"] = ""
        lb23["text"] = ""
        lb24["text"] = ""
        lb25["text"] = ""
        lb26["text"] = ""
        lb27["text"] = ""
        lb28["text"] = "" 
        
        m=et13.get() # por codigo
        n=et15.get() # por nome
 
        cnx = mysql.connector.connect(user='root', password='root', port='3311',
                                  host='127.0.0.1',
                                  database='sgp')
        if m!="":
            cursor = cnx.cursor()
            query = "select * from Produto where Cod_Produto ="+ m

    

            cursor.execute(query)

            linha = cursor.fetchone()
            count = cursor.rowcount
            
            if count>0:
                lb15["text"] = linha [0]
                lb16["text"] = linha [1]
                lb17["text"] = linha [2]
                lb18["text"] = linha [3]
                lb22["text"] = "Código do Produto:"
                lb23["text"] = "Nome do Produto:"
                lb24["text"] = "Unidade do Produto(kg/L/Qtd embalagem):"
                lb25["text"] = "Valor do Produto:                    R$"
                cursor.close()
            else:
                lb20["text"] = "Erro! Produto não encontrado"
            cnx.close()
        if n!="":
            cursor = cnx.cursor()
            query = "select * from Produto where Nome_Produto like '%" + n + "%'"

    

            cursor.execute(query)

            linha = cursor.fetchone()
            count = cursor.rowcount
            if count>0:
                lb15["text"] = linha [0]
                lb16["text"] = linha [1]
                lb17["text"] = linha [2]
                lb18["text"] = linha [3]
                lb22["text"] = "Código do Produto:"
                lb23["text"] = "Nome do Produto:"
                lb24["text"] = "Unidade do Produto(kg/L/Qtd embalagem):"
                lb25["text"] = "Valor do Produto:                    R$"
                cursor.close()
            else:
                lb21["text"] = "Erro! Produto não encontrado"
            cnx.close()
        global o
        global p
        global q
        o="Produto"
        p="Cod_Produto"
        q=str(lb15["text"])
        

    def bd_pesquisaPedido():
        lb15["text"] = ""
        lb16["text"] = ""
        lb17["text"] = ""
        lb18["text"] = ""
        lb19["text"] = ""
        lb20["text"] = ""
        lb21["text"] = ""
        lb22["text"] = ""
        lb23["text"] = ""
        lb24["text"] = ""
        lb25["text"] = ""
        lb26["text"] = ""
        lb27["text"] = ""
        lb28["text"] = "" 

        m=et13.get() # por codigo
        n=et15.get() # por nome
 
        cnx = mysql.connector.connect(user='root', password='root', port='3311',
                                  host='127.0.0.1',
                                  database='sgp')
        if m!="":
            cursor = cnx.cursor()
            query = "select a.Cod_Pedido, a.Data_Entrega, b.Nome_Cliente, c.Nome_Forn, d.Nome_Produto, a.Qntd_Produto,(a.Qntd_Produto*d.Valor_Unit) from Pedido a, Cliente b, Fornecedor c, Produto d where a.Cod_Pedido ="+ m +" and a.Cod_Cliente = b.Cod_Cliente and a.Cod_Forn =c.Cod_Forn and a.Cod_Produto = d.Cod_Produto;"


    

            cursor.execute(query)

            linha = cursor.fetchone()
            count = cursor.rowcount
            
            if count>0:
                lb15["text"] = linha [0]
                lb16["text"] = linha [1]
                lb17["text"] = linha [2]
                lb18["text"] = linha [3]
                lb19["text"] = linha [4]
                lb20["text"] = linha [5]
                lb21["text"] = linha [6]
                lb22["text"] = "Código do Pedido:"
                lb23["text"] = "Data da Entrega(Y/M/D):"
                lb24["text"] = "Nome do Cliente:"
                lb25["text"] = "Nome do Fornecedor:"
                lb26["text"] = "Nome do Produto:"
                lb27["text"] = "Quantidade do Pedido:"
                lb28["text"] = "Valor Total do Pedido:                    R$"
                cursor.close()
            else:
                lb15["text"] = "Erro! Não é possível pesquisar pedido"
            cnx.close()

        if n!="":
                lb15["text"] = "Erro! Não é possível pesquisar pedido por nome"

                lb16["text"] = ""
                lb17["text"] = ""
                lb18["text"] = ""
                lb19["text"] = ""
                lb20["text"] = ""
                lb21["text"] = ""
                lb22["text"] = ""
                lb23["text"] = ""
                lb24["text"] = ""
                lb25["text"] = ""
                lb26["text"] = ""
                lb27["text"] = ""
        global o
        global p
        global q
        o="Pedido"
        p="Cod_Pedido"
        q=str(lb15["text"])

        print(o+', '+p+', '+q)

#Função deletar
    def Delete():
        lb15["text"] = ""
        lb16["text"] = ""
        lb17["text"] = ""
        lb18["text"] = ""
        lb19["text"] = ""
        lb20["text"] = ""
        lb21["text"] = ""
        lb22["text"] = ""
        lb23["text"] = ""
        lb24["text"] = ""
        lb25["text"] = ""
        lb26["text"] = ""
        lb27["text"] = ""
        lb28["text"] = ""   
        Certeza=Tk()
        def Sim():
            
            global o
            global p
            global q
            print(o+', '+p+', '+q)
        
            cnx = mysql.connector.connect(user='root', password='root', port='3311',
                                        host='127.0.0.1',
                                          database='sgp')
            cursor = cnx.cursor()


            query = "delete from "+ o +" where "+ p +" = " + q

            cursor.execute(query)

            


            cursor.close()
            cnx.close()
            lbCer1["text"] =  o +" deletado com sucesso do Banco de Dados do SGP."
        def Nao():
            Certeza.destroy()
        lbCer=Label(Certeza,text = "Tem Certeza?")
        lbCer.place(x=10,y=10)
        
        lbCer1=Label(Certeza,text = "")
        lbCer1.place(x=10,y=65)

        btCY=Button(Certeza,width = 10, text="Sim", command=Sim)
        btCY.place(x=10,y=40)

        btCN=Button(Certeza,width = 10, text="Não", command=Nao)
        btCN.place(x=100,y=40)

        
        Certeza.geometry("340x125+100+100")
        Certeza.mainloop()

        

#Função Editar
    def Editar():
        
        global o
        global p
        global q
        print(o+', '+p+', '+q)
        lb15["text"] = ""
        lb16["text"] = ""
        lb17["text"] = ""
        lb18["text"] = ""
        lb19["text"] = ""
        lb20["text"] = ""
        lb21["text"] = ""
        lb22["text"] = ""
        lb23["text"] = ""
        lb24["text"] = ""
        lb25["text"] = ""
        lb26["text"] = ""
        lb27["text"] = ""
        lb28["text"] = "" 
        if o == "Cliente":
#Função de Alterar Cliente
            AltCliente=Tk() 
            def AltCli():
                global o
                global p
                global q
                aC=etC1.get()
                bC=etC2.get()
                if aC!="" and bC!="":
                    cnx = mysql.connector.connect(user='root', password='root', port='3311', host='127.0.0.1', database='sgp')
                    cursor = cnx.cursor()

                    query =  "update "+ o +" set Nome_Cliente = %s, Cidade_Cliente = %s where "+ p +" = "+ q 

                    cliente=(aC,bC)
    

                    cursor.execute(query,cliente)

                    cursor.close()
                    cnx.close()

                    lbC5["text"]="Dados Alterados!"
                else:
                    lbC5["text"]="Por favor preencha todos os campos!"
            def VoltarAC():
                AltCliente.destroy()

            btFac=Button(AltCliente,width = 10, text="Voltar", command=VoltarAC)
            btFac.place(x=100,y=150)
    
                
            lbC1=Label(AltCliente,text = "Digite os novos dados:")
            lbC1.place(x=100,y=180)
                      
            lbC3=Label(AltCliente,text = "Nome do Cliente:")
            lbC3.place(x=100,y=200)
    
            etC1=Entry(AltCliente,width=60)
            etC1.place(x=100,y=220)

            lbC4=Label(AltCliente,text = "Cidade:")
            lbC4.place(x=100,y=240)
    
            etC2=Entry(AltCliente,width=60)
            etC2.place(x=100,y=260)

            lbC5=Label(AltCliente,text = "")
            lbC5.place(x=100, y=310)

            btC5=Button(AltCliente,width = 50, text="Alterar", command=AltCli)
            btC5.place(x=100,y=285)
            AltCliente.geometry("800x500+100+100")
            AltCliente.mainloop()
#Função Alterar Fornecedor
        if o == "Fornecedor":
            AltFornecedor=Tk() # Container Cliente
            def AltForn():
                global o
                global p
                global q
                aF=etF1.get()
                bF=etF2.get()
                if aF!="" and bF!="":
                    cnx = mysql.connector.connect(user='root', password='root', port='3311', host='127.0.0.1', database='sgp')
                    cursor = cnx.cursor()

                    query =  "update "+ o +" set Nome_Forn = %s, End_Forn = %s where "+ p +" = "+ q 

                    cliente=(aF,bF)
    

                    cursor.execute(query,cliente)

                    cursor.close()
                    cnx.close()

                    lbF6["text"]="Dados Alterados!"
                else:
                    lbF6["text"]="Por favor preencha todos os campos"

            def VoltarAF():
                AltFornecedor.destroy()

            btFaf=Button(AltFornecedor,width = 10, text="Voltar", command=VoltarAF)
            btFaf.place(x=100,y=150)
        
            lbF1=Label(AltFornecedor,text = "Digite os novos dados:")
            lbF1.place(x=100,y=180)
                      
            lbF4=Label(AltFornecedor,text = "Nome do Fornecedor:")
            lbF4.place(x=100,y=200)
    
            etF1=Entry(AltFornecedor,width=60)
            etF1.place(x=100,y=220)

            lbF5=Label(AltFornecedor,text = "Endereço:")
            lbF5.place(x=100,y=240)
    
            etF2=Entry(AltFornecedor,width=60)
            etF2.place(x=100,y=260)

            btF6=Button(AltFornecedor,width = 50, text="Alterar", command=AltForn)
            btF6.place(x=100,y=285)

            lbF6=Label(AltFornecedor,text = "")
            lbF6.place(x=100, y=310)

            AltFornecedor.geometry("800x500+100+100")
            AltFornecedor.mainloop()
        
#Função Alterar Produto

        if o == "Produto":
            AltProduto=Tk() # Container Cliente
            def AltProd():
                global o
                global p
                global q
                aP=etP1.get()
                bP=etP2.get()
                cP=etP3.get()
                if aP!="" and bP!="" and cP!="":
                    cnx = mysql.connector.connect(user='root', password='root', port='3311', host='127.0.0.1', database='sgp')
                    cursor = cnx.cursor()

                    query =  "update "+ o +" set Nome_Produto = %s, Unid_Produto = %s, Valor_Unit = %s where "+ p +" = "+ q 

                    cliente=(aP,bP,cP)
    

                    cursor.execute(query,cliente)

                    cursor.close()
                    cnx.close()

                    lbP6["text"]="Dados Alterados!"
                else:
                    lbP6["text"]="Por favor preencha todos os dados!"

            def VoltarAP():
                AltProduto.destroy()

            btFap=Button(AltProduto,width = 10, text="Voltar", command=VoltarAP)
            btFap.place(x=100,y=150)
        
            lbP1=Label(AltProduto,text = "Digite os novos dados:")
            lbP1.place(x=100,y=180)
                      
            lbP2=Label(AltProduto,text = "Nome do Produto:")
            lbP2.place(x=100,y=200)
    
            etP1=Entry(AltProduto,width=60)
            etP1.place(x=100,y=220)

            lbP3=Label(AltProduto,text = "Unidade do Produto(kg/L/Qtd embalagem):")
            lbP3.place(x=100,y=240)
    
            etP2=Entry(AltProduto,width=60)
            etP2.place(x=100,y=260)

            lbP4=Label(AltProduto,text = "Valor Unitário(R$):")
            lbP4.place(x=100,y=280)
    
            etP3=Entry(AltProduto,width=60)
            etP3.place(x=100,y=300)

            btP6=Button(AltProduto,width = 50, text="Alterar", command=AltProd)
            btP6.place(x=100,y=325)

            lbP6=Label(AltProduto,text = "")
            lbP6.place(x=100, y=350)

            AltProduto.geometry("800x500+100+100")
            AltProduto.mainloop()

#Função Alterar Pedido
            
        if o == "Pedido":
            AltPedido=Tk() 
            def AltPed():
                global o
                global p
                global q
                aPe=etPe1.get()
                bPe=etPe2.get()
                cPe=etPe3.get()
                dPe=etPe4.get()
                ePe=etPe5.get()
                if aPe!="" and bPe!="" and cPe!="" and dPe!="" and ePe!="":
                    cnx = mysql.connector.connect(user='root', password='root', port='3311', host='127.0.0.1', database='sgp')
                    cursor = cnx.cursor()

                    query =  "update "+ o +" set Data_Entrega = %s,Cod_Cliente = %s,Cod_Forn = %s,Cod_Produto = %s,Qntd_Produto = %s where "+ p +" = "+ q 

                    ped=(datetime.strptime(aPe,"%d/%m/%Y").date(),bPe,cPe,dPe,ePe)
    

                    cursor.execute(query,ped)

                    cursor.close()
                    cnx.close()

                    lbPe7["text"]="Dados Alterados!"
                else:
                    lbPe7["text"]="Por favor Preencha todos os campos!"

            def VoltarAPe():
                AltPedido.destroy()

            btFape=Button(AltPedido,width = 10, text="Voltar", command=VoltarAPe)
            btFape.place(x=100,y=150)
            
            lbPe1=Label(AltPedido,text = "Digite os novos dados:")
            lbPe1.place(x=100,y=180)
                      
            lbPe2=Label(AltPedido,text = "Data_Entrega(dd/mm/yyyy):")
            lbPe2.place(x=100,y=200)
    
            etPe1=Entry(AltPedido,width=60)
            etPe1.place(x=100,y=220)

            lbPe3=Label(AltPedido,text = "Código do Cliente:")
            lbPe3.place(x=100,y=240)
    
            etPe2=Entry(AltPedido,width=60)
            etPe2.place(x=100,y=260)

            lbPe4=Label(AltPedido,text = "Código do Fornecedor:")
            lbPe4.place(x=100,y=280)
    
            etPe3=Entry(AltPedido,width=60)
            etPe3.place(x=100,y=300)

            lbPe5=Label(AltPedido,text = "Código do Produto:")
            lbPe5.place(x=100,y=320)
    
            etPe4=Entry(AltPedido,width=60)
            etPe4.place(x=100,y=340)

            lbPe6=Label(AltPedido,text = "Quantidade do Pedido:")
            lbPe6.place(x=100,y=360)
    
            etPe5=Entry(AltPedido,width=60)
            etPe5.place(x=100,y=380)

            btPe6=Button(AltPedido,width = 50, text="Alterar", command=AltPed)
            btPe6.place(x=100,y=405)

            lbPe7=Label(AltPedido,text = "")
            lbPe7.place(x=100, y=425)

            AltPedido.geometry("800x500+100+100")
            AltPedido.mainloop()
    def VoltarBus():
        interface6.destroy()
    #Botão - Voltar
    btFBus=Button(interface6,width = 10, text="Voltar", command=VoltarBus)
    btFBus.place(x=100,y=100)
    
    #Botão - Edição
    btP=Button(interface6,width = 25, text="EDITAR",command = Editar)
    btP.place(x=500,y=200)

    #Botão - Deletar
    btD=Button(interface6,width = 25, text="DELETAR",command = Delete)
    btD.place(x=500,y=300)
        
    lb14=Label(interface6,text = "Buscar por Codigo:")
    lb14.place(x=100,y=160)
    
    et13=Entry(interface6,width=60)
    et13.place(x=100,y=180)

    lb14=Label(interface6,text = "Buscar por Nome ( Exceto Pedido):")
    lb14.place(x=100,y=200)
    
    et15=Entry(interface6,width=60)
    et15.place(x=100,y=220)

    bt9=Button(interface6,width = 50, text="CLIENTE", command = bd_pesquisaCliente)
    bt9.place(x=100,y=250)
    
    bt10=Button(interface6,width = 50, text="FORNECEDOR", command = bd_pesquisaFornecedor)
    bt10.place(x=100,y=275)

    bt11=Button(interface6,width = 50, text="PRODUTO", command = bd_pesquisaProduto)
    bt11.place(x=100,y=300)

    bt12=Button(interface6,width = 50, text="PEDIDO",command = bd_pesquisaPedido)
    bt12.place(x=100,y=325)

    lb15=Label(interface6,text = "")
    lb15.place(x=300,y=360)

    lb16=Label(interface6,text = "")
    lb16.place(x=300,y=380)

    lb17=Label(interface6,text = "")
    lb17.place(x=300,y=400)

    lb18=Label(interface6,text = "")
    lb18.place(x=300,y=420)

    lb19=Label(interface6,text = "")
    lb19.place(x=300,y=440)

    lb20=Label(interface6,text = "")
    lb20.place(x=300,y=460)

    lb21=Label(interface6,text = "")
    lb21.place(x=300,y=480)    

    lb22=Label(interface6,text = "")
    lb22.place(x=10,y=360)

    lb23=Label(interface6,text = "")
    lb23.place(x=10,y=380)

    lb24=Label(interface6,text = "")
    lb24.place(x=10,y=400)

    lb25=Label(interface6,text = "")
    lb25.place(x=10,y=420)

    lb26=Label(interface6,text = "")
    lb26.place(x=10,y=440)

    lb27=Label(interface6,text = "")
    lb27.place(x=10,y=460)

    lb28=Label(interface6,text = "")
    lb28.place(x=10,y=480)

    
    interface6.geometry("800x500+100+100")
    interface6.mainloop()

""""""""""""""""""""""""""""""""""""""""""""""" Fim da Tela de Busca"""""""""""""""""""""""""""""""""""""""""""""""    


'''Definição dos botões da tela de cadastro 1 '''

#Variáveis Globais
o=""
q=""
p=""


def Botao_cadastro():
    interface1 = Tk()  # Container Tela Principal
    #TK  - CLASSE PRINCIPAL
    interface1.title("SGP- Sistema de Gerenciamento de Produtos")
    
    def VoltarCad():
        interface1.destroy()

    btFCad=Button(interface1,width = 10, text="Voltar", command=VoltarCad)
    btFCad.place(x=200,y=20)


    #Botão 1- Cadastro de Clientes
    bt1=Button(interface1,width = 50, text="Cliente", command=Cad_Cliente)
    bt1.place(x=200,y=100)

    #Botão 2- Cadastro de Fornecedores
    bt2=Button(interface1,width = 50, text="Fornecedor",command=Cad_Fornecedor)
    bt2.place(x=200,y=200)

    #Botão 3- Cadastro de Produto
    bt3=Button(interface1,width = 50, text="Produto",command=Cad_Produto)
    bt3.place(x=200,y=300)

    #Botão 4- Cadastro de Pedidos
    bt4=Button(interface1,width = 50, text="Pedido",command=Cad_Pedido)
    bt4.place(x=200,y=400)



    #LxA+E+T ( largura x altura+Esquerda+Topo)
    interface1.geometry("800x500+100+100")

    lb1=Label(interface1, text = "O que você gostaria de cadastrar?")
    lb1.place(x=200,y=50)

    interface1.mainloop ()
'''''''''''''''''''''''''''''''''''''''    ACABOU INTERFACES DE Cadastro.    '''''''''''''''''''''''''''''''''''''''''''''''''''




'''''''''''Tela Principal'''''''''
interface=Tk()
interface.title("SGP- Sistema de Gerenciamento de Produtos")

#Botão - Sair
def Sair():
    CertezaSair=Tk()
    def SN():
        CertezaSair.destroy()
    def SY():
        quit()
    #Botão - Voltar
    lbS=Label(CertezaSair, text = "Tem certeza que deseja sair?")
    lbS.place(x=10,y=20)

    btSN=Button(CertezaSair,width = 10, text="Não", command=SN)
    btSN.place(x=100,y=40)
    
    btSY=Button(CertezaSair,width = 10, text="Sim", command=SY)
    btSY.place(x=10,y=40)
    

    CertezaSair.geometry("340x125+100+100")
    CertezaSair.mainloop()

    
btS=Button(interface,width = 10, text="Sair", command=Sair)
btS.place(x=100,y=300)

#Botão - Cadastro 
btC=Button(interface,width = 50, text="CADASTRAR", command=Botao_cadastro)
btC.place(x=200,y=100)

#Botão - Busca
btP=Button(interface,width = 50, text="BUSCA",command=Botao_pesquisa)
btP.place(x=200,y=200)




#LxA+E+T ( largura x altura+Esquerda+Topo)
interface.geometry("800x500+100+100")

lbI=Label(interface, text = "BEM VINDO AO SGP!!")
lbI.place(x=100,y=50)
lbII=Label(interface, text = "CLIQUE EM UMA OPÇÃO PARA REALIZAR UMA AÇÃO")
lbII.place(x=100,y=70)

interface.mainloop()


