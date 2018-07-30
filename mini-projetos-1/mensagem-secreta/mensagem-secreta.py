import os
def rename_file():
    
    file_list = os.listdir(r"C:\Users\yuri_\Desktop\GIT\Udacity\Fundamentos-da-Web\mini-projetos-1\mensagem-secreta\arquivos\prank")

    saved_path = os.getcwd()
    print("diretorio atual"+saved_path)
    os.chdir(r"C:\Users\yuri_\Desktop\GIT\Udacity\Fundamentos-da-Web\mini-projetos-1\mensagem-secreta\arquivos\prank")

    for file_name in file_list :
        os.rename(file_name, file_name.translate(None, "0123456789"))
    os.chdir(saved_path)
rename_file()
