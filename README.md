1 - Clonar o projeto do GitHub.

2 - Cria o ambiente de trabalho e ativa ele.

3 - Instala os requirements 'pip install -r requirements-dev.txt'

4 - Faz as migrações do db

5 - Cria o usuariosuperuser

6 - Roda o sistema 'runserver'

7 - Acessa o sistema "http://localhost:8000/sistema/"

8 - Apos acessar, faz os cadastro dos medicos, postos, folgas, escalas e faz as validações.

9 - Validações:

    A - Só poderá preencher a escala se não houver folga para o médico naquele dia da semana.

    B - Não poderá ser cadastrada folga se houver escala definida para o médico naquele dia da semana.

    C - Não permitindo multiplos cadastros (unique_together).

    d- Validação do formato das datas.
