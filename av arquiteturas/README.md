# AV2 — Arquitetura de Computadores: guia completo para Ubuntu Server

**Aluno:** Luciano Alves Freire Neto  
**Professor:** Tibério Bezerra Soares  
**Base:** arquivo `AV2-Arquitetura de Computadores_Noite.docx.pdf`, com 3 páginas.  
**Guia atualizado em:** 26/11/2026.

Este material explica como montar a máquina virtual, instalar o sistema, configurar o acesso remoto, criar os scripts e instalar dois serviços. Os comandos são para você executar no seu laboratório e conferir os resultados. Criar este guia no GitHub não cria nem configura a VM do seu computador.

## 1. O que precisa ser entregue

| Parte | O que fazer | Pontuação informada |
| --- | --- | --- |
| 1 | VM com 4 GB de RAM, pelo menos 4 CPUs, disco de 20 GB e sistema instalado | 5 pontos |
| Identificação obrigatória | Nome completo na VM e pasta com o nome completo dentro de Documentos do computador hospedeiro | Incluída nas exigências |
| Segurança | Instalar com LVM e criptografia LUKS; informar a senha ao professor na conferência | +1 ponto extra |
| 2 | OpenSSH ativo e automático; dois scripts executáveis na home do usuário | 3 pontos |
| 3 | Dois serviços funcionando, iniciando com o sistema e arquivo de evidência | 2 pontos |

**Sistema definido para esta atividade: Ubuntu Server**, conforme a orientação atual de Luciano. Todo o roteiro usa o instalador do Ubuntu Server, seus repositórios, `apt` e `systemd`.

Também há uma diferença na expressão “/scripts na home”. Dentro da home, o caminho correto é **`~/scripts`**, por exemplo `/home/luciano/scripts`. O caminho **`/scripts`** sozinho fica na raiz do Linux. Neste guia, todos os arquivos ficam em `~/scripts`, atendendo à indicação de usar a home.

### Caminho escolhido para a Parte 3

| Programa | Categoria | Método | Como será testado |
| --- | --- | --- | --- |
| Nginx | Servidor web | Nativo, com `apt` | HTTP na porta 80 da VM |
| PostgreSQL | Banco de dados | Nativo, com `apt` | Consulta SQL local e verificação da porta 5432 |

O enunciado permite instalação nativa ou Docker. Aqui vamos usar instalação nativa para reduzir a quantidade de etapas e trabalhar diretamente com os serviços do Linux. O SSH é exigido na Parte 2 e não será contado como um dos dois programas da Parte 3.

## 2. Antes de começar: onde fazer cada coisa

| Local | O que você fará nele |
| --- | --- |
| Windows do computador físico | Criar a pasta em Documentos, usar o VirtualBox e testar SSH pelo PowerShell |
| Janela da máquina virtual | Instalar o Linux, desbloquear o disco e executar os comandos Linux |
| Navegador do Windows | Abrir a página do Nginx para comprovar acesso |
| GitHub | Consultar este guia; não guardar senhas nem o disco virtual |

**Hospedeiro** é o computador físico. **Convidado** é o Linux dentro da VM.

Nos exemplos, o usuário do Linux será `luciano` e o servidor terá o nome `financeiro-lab`. Se você escolher outro usuário, substitua `luciano` nos comandos SSH. `~` e `$HOME` representam a home do usuário atualmente conectado.

Não digite os marcadores de blocos de código nem um eventual símbolo `$` do terminal. Digite somente os comandos apresentados.

### O que separar

1. VirtualBox instalado no computador hospedeiro, ou outro virtualizador autorizado pelo professor.
2. ISO do **Ubuntu Server**, arquitetura **amd64** para PC Intel/AMD de 64 bits. A imagem de instalação pode conter `live-server` no nome; ela é própria para instalar o servidor. Escolha a edição Server para acompanhar este roteiro.
3. Recursos físicos suficientes para reservar 4 GB de RAM e 4 CPUs para a VM sem deixar o hospedeiro sem recursos.
4. Internet para instalar os pacotes.
5. Uma senha para o usuário Linux e uma frase-senha para o disco criptografado.

**Versão do Ubuntu Server:** use a versão estável mais recente da [página oficial](https://ubuntu.com/download/server), conforme o enunciado. Na consulta em 26/11/2026, a página apresenta **26.10** como versão mais recente e **26.04.1 LTS** como LTS mais recente. Se o professor tiver definido uma versão LTS para o laboratório, siga essa versão. Os nomes das telas podem variar um pouco.

## 3. Parte 1 — Criar a máquina virtual

### 3.1. Criar a pasta obrigatória no Windows

1. Abra o **Explorador de Arquivos**.
2. Entre em **Documentos**. Em alguns computadores essa pasta fica dentro do OneDrive.
3. Crie uma pasta chamada **Luciano Alves Freire Neto**.
4. Abra essa pasta e copie o caminho mostrado na barra de endereço.

Um caminho possível é `C:\Users\Aluno\Documents\Luciano Alves Freire Neto`. Use o caminho real da sua pasta Documentos; o nome do usuário do Windows pode ser diferente.

### 3.2. Criar a VM no VirtualBox

1. Abra o **VirtualBox** e clique em **Novo**.
2. Em **Nome**, coloque **Luciano Alves Freire Neto**.
3. Em **Pasta da máquina**, selecione a pasta que você criou dentro de Documentos.
4. Selecione a ISO de instalação do Ubuntu Server.
5. Confira o tipo **Linux** e a versão **Ubuntu (64-bit)**, ou opção equivalente.
6. Marque **Pular instalação desassistida / Skip Unattended Installation**, se essa opção aparecer. Faremos a instalação manual para escolher a criptografia.
7. Defina a memória como **4096 MB**, equivalente à configuração de 4 GB usada neste laboratório.
8. Defina **4 CPUs/processadores virtuais**. Quatro é o mínimo pedido; mais é permitido se houver recursos físicos.
9. Crie um disco virtual novo de **20 GB**.
10. Use **VDI** e alocação dinâmica, caso o assistente apresente essas opções.
11. Conclua a criação.

Se o assistente não mostrar a quantidade de CPUs, configure depois em **Configurações → Sistema → Processador**, com a VM desligada. A alocação dinâmica muda o espaço ocupado no hospedeiro, mas a capacidade do disco virtual deve continuar sendo 20 GB.

O VirtualBox pode criar uma subpasta adicional com o nome da VM. Isso é aceitável desde que os arquivos continuem dentro da pasta identificada em Documentos.

### 3.3. Configurar a rede: NAT com duas portas

Usaremos **NAT**, que permite à VM acessar a internet. Para o Windows acessar SSH e Nginx da VM, crie dois redirecionamentos.

1. Com a VM desligada, abra **Configurações → Rede**.
2. No **Adaptador 1**, mantenha a placa habilitada e selecione **NAT**.
3. Confira se **Cabo conectado** está marcado.
4. Abra **Avançado → Redirecionamento de Portas**, ou opção equivalente.
5. Cadastre as regras abaixo.

| Nome | Protocolo | IP do hospedeiro | Porta do hospedeiro | IP do convidado | Porta do convidado |
| --- | --- | --- | --- | --- | --- |
| SSH | TCP | 127.0.0.1 | 2222 | Deixar vazio | 22 |
| WEB | TCP | 127.0.0.1 | 8080 | Deixar vazio | 80 |

Assim, `127.0.0.1:2222` no Windows será encaminhado para a porta 22 da VM, e `127.0.0.1:8080` para a porta 80. Essas regras permitem acesso pelo próprio hospedeiro. A VM precisa estar ligada e com o sistema iniciado.

Não é necessário redirecionar PostgreSQL: o exercício aceita comprovação de acesso local ao serviço.

**Se você já usa rede em modo Bridge:** pode manter esse modo se a rede do laboratório permitir. Nesse caso, descubra o IP da VM com `hostname -I`, conecte com `ssh luciano@IP_DA_VM` e abra `http://IP_DA_VM`. Não misture esses endereços com as portas do método NAT.

### 3.4. Conferir antes da instalação

Confira nas configurações da VM:

- Nome: Luciano Alves Freire Neto.
- Pasta: dentro de Documentos/Luciano Alves Freire Neto.
- RAM: 4096 MB.
- CPUs: pelo menos 4.
- Disco virtual: capacidade de 20 GB.
- ISO: Ubuntu Server, arquitetura amd64.

**Evidência sugerida:** capture a tela com nome e recursos da VM e outra com a localização dos arquivos no Explorador.

## 4. Instalar Ubuntu Server com LVM e criptografia

### 4.1. Iniciar e navegar no instalador

1. Inicie a VM.
2. No menu da ISO, escolha **Try or Install Ubuntu Server**, ou opção equivalente.
3. Selecione o idioma disponível que preferir.
4. Se aparecer uma atualização do instalador, siga a opção disponível conforme a conexão do laboratório.
5. Confira o teclado. Para teclado brasileiro, selecione o layout brasileiro adequado, normalmente ABNT2.
6. Se aparecer a escolha do tipo de instalação, mantenha **Ubuntu Server** padrão.

O instalador usa telas de texto. Navegue com **setas** e **Tab**, marque opções com **Espaço** e confirme com **Enter**. Ubuntu Server não precisa instalar uma área de trabalho gráfica para esta atividade.

### 4.2. Rede, proxy e espelho de pacotes

1. Na configuração de rede, mantenha o endereço automático por **DHCP**.
2. Confira se a interface recebeu um endereço IP.
3. Na tela de proxy, deixe vazio se a instituição não forneceu um endereço.
4. Mantenha o espelho de pacotes padrão se o teste de conexão funcionar.
5. Se a rede falhar, confira **NAT** e **Cabo conectado** no VirtualBox antes de continuar.

### 4.3. Configurar LVM e criptografia LUKS

Esta etapa atende ao **ponto extra**. A criptografia deve ser configurada durante a instalação.

1. Na tela **Guided storage configuration**, escolha **Use an entire disk / Usar disco inteiro**.
2. Selecione o **disco virtual de 20 GB** criado para a atividade.
3. Marque **Set up this disk as an LVM group**.
4. Marque **Encrypt the LVM group with LUKS**, ou opção equivalente.
5. Defina e confirme uma **frase-senha do disco** que você consiga digitar no layout escolhido.
6. Avance para o resumo e confira o disco e os volumes propostos.
7. Confirme as alterações **somente no disco virtual desta VM**.

Marcar somente LVM não ativa criptografia: confira também a opção **LUKS**.

**LVM** organiza os volumes lógicos; **LUKS** protege os dados em repouso. Na configuração padrão, partições necessárias ao boot, como EFI e `/boot`, podem ficar sem criptografia, enquanto o sistema e os dados ficam no volume criptografado.

A partição raiz pode ter menos de 20 GB por causa das partições de boot, dos metadados e do espaço reservado no LVM. A exigência de 20 GB corresponde à capacidade do disco virtual; não é necessário alterar manualmente a raiz para fazê-la ocupar esse valor.

Guarde a frase-senha para informar ao professor na conferência, como o enunciado solicita. Não a coloque no GitHub nem no arquivo de evidência dos serviços.

**Evidência sugerida:** opções LVM/LUKS e resumo de armazenamento, sem revelar a frase-senha.

### 4.4. Criar o perfil do usuário

Na tela **Profile setup**, preencha:

| Campo | Valor sugerido |
| --- | --- |
| Your name / Seu nome | Luciano Alves Freire Neto |
| Your server's name / Nome do servidor | financeiro-lab |
| Pick a username / Nome de usuário | luciano |
| Choose a password / Senha | Defina a sua |
| Confirm your password | Repita a senha |

O nome completo da **VM no VirtualBox** é obrigatório. O hostname do Ubuntu tem outra função e pode ser `financeiro-lab`, sem espaços.

O usuário criado pelo instalador do Ubuntu Server normalmente já tem acesso administrativo com `sudo`. A instalação padrão não pede que você configure uma senha separada de root.

A senha do usuário serve para login e `sudo`. A frase-senha LUKS libera o disco antes de o sistema iniciar.

### 4.5. Ubuntu Pro e OpenSSH

1. Se aparecer a oferta de **Ubuntu Pro**, avance sem adesão, salvo orientação do professor.
2. Na tela **SSH configuration**, marque **Install OpenSSH server**.
3. Se houver a opção **Allow password authentication over SSH**, habilite-a para testar o usuário criado.
4. Não é necessário importar chave pública para seguir este caminho de login por senha.
5. Avance para continuar.

### 4.6. Serviços opcionais e instalação

1. Na tela de **Featured server snaps**, se aparecer, deixe os serviços opcionais desmarcados.
2. Continue e aguarde a instalação terminar.
3. Instalaremos Nginx e PostgreSQL manualmente nas seções 10 e 11, com `apt`.
4. Não selecione outro servidor web nessa etapa, para manter a porta 80 disponível ao Nginx.

### 4.7. Reiniciar e fazer o primeiro login

1. Quando a instalação terminar, selecione **Reboot Now / Reiniciar agora**.
2. Quando solicitado, remova a ISO da unidade óptica virtual e pressione Enter.
3. No boot, digite a **frase-senha LUKS** para desbloquear o disco.
4. Aguarde a tela de login do Ubuntu.
5. Entre como `luciano` e use a **senha do usuário**.

Se o instalador abrir novamente, desligue a VM normalmente, remova a ISO em **Configurações → Armazenamento** e inicie pelo disco instalado.

**Comportamento esperado:** depois do desbloqueio, aparece o login em modo texto do Ubuntu Server. A senha do disco e a senha do usuário são usadas em momentos diferentes.

## 5. Primeiros comandos e conferência da VM

**Execute dentro do Ubuntu Server da VM.** Ao digitar a senha de `sudo`, normalmente nada aparece na tela, nem asteriscos. Digite a senha do usuário e pressione Enter.

### 5.1. Conferir o acesso sudo

Conectado como o usuário criado na instalação, execute:

```bash
whoami
id
sudo -v
```

Digite a **senha do usuário**. Se a validação terminar sem erro, siga para a seção 5.2. No Ubuntu Server padrão, o primeiro usuário criado no instalador normalmente já pertence ao grupo `sudo`.

Se outro usuário estiver conectado e aparecer que ele não está no sudoers, entre com a conta administrativa criada na instalação. **Somente nessa conta que já tem sudo**, você pode autorizar o usuário desejado:

```bash
sudo usermod -aG sudo luciano
```

Substitua `luciano` pelo usuário que precisa de acesso. Depois encerre a sessão desse usuário e faça login novamente para carregar o grupo. Confira com `id` e `sudo -v`.

Esse comando não funciona a partir de uma conta que já está sem permissão. Se você não tiver acesso a nenhuma conta administrativa, peça ao professor/administrador para preparar o usuário antes de continuar. Não use `su -` supondo uma senha de root: no Ubuntu padrão, essa conta fica bloqueada para login por senha.

### 5.2. Conferir sistema e recursos

```bash
whoami
pwd
cat /etc/os-release
nproc
free -h
lsblk -o NAME,SIZE,TYPE,FSTYPE,MOUNTPOINTS
```

| Comando | O que conferir |
| --- | --- |
| `whoami` | Usuário usado na instalação |
| `pwd` | Diretório atual, normalmente `/home/luciano` após login |
| `cat /etc/os-release` | Deve identificar Ubuntu e a versão instalada |
| `nproc` | Pelo menos 4 CPUs disponíveis |
| `free -h` | RAM próxima do valor configurado; uma parte fica reservada ao sistema |
| `lsblk ...` | Disco com capacidade configurada, partição `crypto_LUKS`, mapeamento `crypt` e volumes LVM |

### 5.3. Instalar as ferramentas usadas pelo guia

Atualize a lista de pacotes e instale as ferramentas dos repositórios do Ubuntu:

```bash
sudo apt update
sudo apt install -y openssh-server nano curl procps iproute2
```

Se quiser atualizar os pacotes já instalados, execute `sudo apt upgrade` e leia o que será atualizado antes de confirmar. Essa atualização geral não substitui nenhuma exigência da avaliação.

**Evidência sugerida:** versão do Linux, RAM, CPUs e estrutura do disco. Não execute comandos de formatação para demonstrar criptografia; `lsblk` basta para inspecionar a estrutura.

## 6. Parte 2 — Acesso remoto por SSH

### 6.1. Ativar e habilitar a inicialização automática

Na VM:

```bash
sudo systemctl enable --now ssh
systemctl is-enabled ssh
systemctl is-active ssh
sudo systemctl status ssh --no-pager
```

O esperado é **`enabled`** e **`active`**, com o servidor disponível. Para conferir a porta:

```bash
sudo ss -ltnp 'sport = :22'
```

Deve haver um processo escutando na porta 22. Os comandos acima administram **`ssh.service`**. Algumas versões do Ubuntu usam também **`ssh.socket`** para ativação sob demanda; nesse caso, confira `systemctl status ssh.socket --no-pager` e `systemctl is-enabled ssh.socket`. O teste de conexão da seção 6.4 confirma que o acesso está funcionando.

### 6.2. Conferir autenticação do usuário

```bash
sudo /usr/sbin/sshd -t
sudo /usr/sbin/sshd -T | grep -E '^(passwordauthentication|permitrootlogin|pubkeyauthentication) '
```

`sshd -t` sem saída e sem erro indica que a configuração é válida. Para este caminho com senha, confira `passwordauthentication yes` e faça login como `luciano`.

**Somente se o login por senha estiver desabilitado**, crie a configuração abaixo. Se o acesso já funciona, avance para o teste.

```bash
sudo nano /etc/ssh/sshd_config.d/00-av-arquitetura.conf
```

Conteúdo:

```text
PasswordAuthentication yes
PermitRootLogin no
```

No Nano, salve com **Ctrl+O**, confirme com **Enter** e saia com **Ctrl+X**. Depois:

```bash
sudo /usr/sbin/sshd -t
```

Se não houver erro, aplique:

```bash
sudo systemctl restart ssh
sudo /usr/sbin/sshd -T | grep -E '^(passwordauthentication|permitrootlogin) '
```

Se ainda aparecer `passwordauthentication no`, verifique a ordem das configurações e possíveis regras `Match` no arquivo principal antes de continuar. Mantenha a janela da VM acessível enquanto testa SSH.

### 6.3. Firewall, caso já esteja ativo

Se o comando `ufw` existir, consulte:

```bash
sudo ufw status
```

Se mostrar **active**, permita SSH:

```bash
sudo ufw allow 22/tcp
```

Se estiver inativo, não é preciso ativá-lo para concluir esta etapa. A regra libera a porta **22 da VM**, mesmo quando o Windows usa a porta 2222 no NAT.

### 6.4. Conectar pelo PowerShell do Windows

**Agora abra o PowerShell no Windows hospedeiro**, mantendo a VM ligada e desbloqueada.

```powershell
ssh -p 2222 luciano@127.0.0.1
```

1. Na primeira conexão, o SSH perguntará sobre a chave do servidor. Confira que está acessando sua VM e confirme com `yes`.
2. Digite a senha do usuário `luciano`.
3. Após entrar, rode:

```bash
whoami
hostname
pwd
```

O esperado é o usuário `luciano`, o hostname escolhido e a home do Linux. Isso comprova que o terminal do Windows abriu uma sessão dentro da VM.

Para sair da sessão remota:

```bash
exit
```

No PuTTY/MobaXterm, use host `127.0.0.1`, porta `2222` e usuário `luciano` para o mesmo modo NAT. Se o PowerShell informar que `ssh` não existe, use uma dessas ferramentas ou habilite o Cliente OpenSSH do Windows.

**Evidência sugerida:** PowerShell conectado, com `whoami` e `hostname`, além do SSH ativo e habilitado na VM.

## 7. Criar a pasta dos scripts

De volta à VM, ou dentro de uma sessão SSH conectada a ela, execute como seu usuário normal:

```bash
mkdir -p "$HOME/scripts"
cd "$HOME/scripts"
pwd
```

Para o usuário de exemplo, deve aparecer `/home/luciano/scripts`. Não use `sudo mkdir` nessa pasta; o próprio usuário deve ser dono dos scripts e do arquivo de logs.

## 8. Script 1 — coletar_logs.sh

### 8.1. Criar o arquivo

```bash
nano "$HOME/scripts/coletar_logs.sh"
```

Copie o conteúdo completo:

```bash
#!/bin/bash
set -euo pipefail

# Salva os logs na mesma pasta do script, mesmo se ele for chamado de outra pasta.
PASTA_SCRIPT="$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")" && pwd)"
ARQUIVO_LOG="$PASTA_SCRIPT/logs_sistema.txt"

# Cria o arquivo ou apaga o conteúdo anterior.
: > "$ARQUIVO_LOG"

# sudo permite consultar o journal completo do sistema.
# A redireção é feita pelo usuário normal, que continua sendo dono do arquivo.
if sudo journalctl --quiet --no-pager -n 50 -o short > "$ARQUIVO_LOG"; then
    echo "Logs coletados com sucesso!"
    echo "Arquivo: $ARQUIVO_LOG"
else
    echo "Erro: não foi possível coletar os logs do sistema." >&2
    exit 1
fi
```

Salve com **Ctrl+O → Enter → Ctrl+X**.

### 8.2. Entender o código

| Trecho | Função |
| --- | --- |
| `#!/bin/bash` | Executa o arquivo com Bash |
| `set -euo pipefail` | Ajuda a interromper a execução em erros e uso de variáveis indefinidas |
| `PASTA_SCRIPT=...` | Descobre a pasta onde o script está salvo |
| `: > "$ARQUIVO_LOG"` | Cria ou esvazia `logs_sistema.txt` |
| `sudo journalctl` | Lê o journal do sistema com permissão administrativa |
| `-n 50` | Solicita as 50 entradas mais recentes |
| `--quiet --no-pager -o short` | Evita avisos de cabeçalho/paginador e usa saída curta |
| `> "$ARQUIVO_LOG"` | Grava a saída substituindo o conteúdo anterior |
| `if ...; then` | Só mostra sucesso se a coleta terminar corretamente |

O enunciado fala em “50 linhas”; o `journalctl -n 50` seleciona 50 entradas. Mensagens que contêm quebras de linha podem ocupar mais linhas físicas, e um sistema com menos de 50 entradas terá menos conteúdo. O arquivo não recebe um cabeçalho adicional do script.

### 8.3. Dar permissão e executar

```bash
chmod u+x "$HOME/scripts/coletar_logs.sh"
"$HOME/scripts/coletar_logs.sh"
```

Digite a senha do usuário se `sudo` pedir. Não é necessário executar o script inteiro com `sudo`; ele já solicita a permissão no comando que precisa dela.

### 8.4. Conferir o resultado

```bash
ls -l "$HOME/scripts/coletar_logs.sh" "$HOME/scripts/logs_sistema.txt"
wc -l "$HOME/scripts/logs_sistema.txt"
tail -n 5 "$HOME/scripts/logs_sistema.txt"
```

O script deve exibir a mensagem de sucesso, e o arquivo deve conter os registros. Executá-lo novamente substitui os registros anteriores.

**Evidência sugerida:** execução com mensagem de sucesso, permissão de execução e algumas linhas do arquivo gerado.

## 9. Script 2 — monitoramento.sh

### 9.1. Criar o arquivo

```bash
nano "$HOME/scripts/monitoramento.sh"
```

Conteúdo completo:

```bash
#!/bin/bash
set -euo pipefail

echo "=============================================="
echo "        MONITORAMENTO DO SISTEMA"
echo "=============================================="
printf 'Servidor: %s\n' "$(hostname)"
printf 'Data: %s\n' "$(date '+%d/%m/%Y %H:%M:%S')"

printf '\n--- DISCO: total, usado e disponível ---\n'
df -h --total -x tmpfs -x devtmpfs

printf '\n--- MEMÓRIA RAM ---\n'
free -h

printf '\n--- CPU: carga média ---\n'
printf 'CPUs disponíveis: %s\n' "$(nproc)"
LC_ALL=C uptime
echo "As três cargas correspondem aos últimos 1, 5 e 15 minutos."
echo "Carga média não é porcentagem de uso da CPU."

printf '\n==============================================\n'
```

Salve com **Ctrl+O → Enter → Ctrl+X**.

### 9.2. Dar permissão e executar

```bash
chmod u+x "$HOME/scripts/monitoramento.sh"
"$HOME/scripts/monitoramento.sh"
```

Esse script não precisa de `sudo`.

### 9.3. Como ler as informações

| Informação | Comando | Como interpretar |
| --- | --- | --- |
| Disco | `df -h ...` | Cada sistema de arquivos mostra tamanho, usado, disponível e ponto de montagem |
| RAM | `free -h` | Na linha `Mem:`, veja `total`, `used` e `available`; o Linux também usa RAM como cache |
| CPU | `nproc` e `uptime` | Mostra CPUs disponíveis e carga média de 1, 5 e 15 minutos |

Em uma VM com 4 CPUs, carga média próxima de 4 significa uma demanda média aproximadamente equivalente a quatro tarefas executando ou aguardando determinados recursos. Essa medida também pode incluir espera por I/O; não equivale a uma leitura exata de 100% de CPU. O enunciado aceita **carga atual ou porcentagem**, por isso usamos a carga média.

O disco mostrado por `df` é o espaço dos sistemas de arquivos montados, não a capacidade total bruta do disco virtual. Para capacidade do disco, consulte também `lsblk` e o VirtualBox.

**Evidência sugerida:** saída organizada com disco, RAM e CPU na mesma execução.

### 9.4. Conferir os dois scripts

```bash
bash -n "$HOME/scripts/coletar_logs.sh"
bash -n "$HOME/scripts/monitoramento.sh"
ls -l "$HOME/scripts/"*.sh
```

`bash -n` verifica a sintaxe sem executar. Nenhuma saída normalmente indica sintaxe válida. Na listagem, a permissão do dono deve incluir `x`, como `-rwxr--r--`.

O PDF não pede agendamento com `cron`. “Automação” nesta tarefa está contemplada pelos scripts executáveis; não é necessário criar uma rotina periódica para atender aos itens descritos.

## 10. Parte 3 — Instalar o Nginx

### 10.1. Instalação e início automático

Dentro da VM:

```bash
sudo apt update
sudo apt install -y nginx
sudo systemctl enable --now nginx
```

### 10.2. Testar configuração, estado e acesso HTTP

```bash
sudo nginx -t
systemctl is-enabled nginx
systemctl is-active nginx
sudo systemctl status nginx --no-pager
curl -I http://127.0.0.1
```

O esperado é configuração válida, `enabled`, `active` e resposta HTTP de sucesso, normalmente **`200 OK`**. Para ver o conteúdo HTML:

```bash
curl http://127.0.0.1
```

Para conferir a porta:

```bash
sudo ss -ltnp 'sport = :80'
```

Se o UFW já estiver ativo, permita HTTP:

```bash
sudo ufw allow 80/tcp
```

### 10.3. Abrir no navegador do Windows

Com a regra NAT da seção 3.3, abra no **navegador do hospedeiro**:

```text
http://127.0.0.1:8080
```

Deve aparecer a página padrão **Welcome to nginx!**. Na VM, o serviço continua na porta 80; a porta 8080 é a entrada no Windows.

**Evidência sugerida:** página no navegador e serviço ativo/habilitado.

## 11. Instalar e testar o PostgreSQL

### 11.1. Instalação e início automático

```bash
sudo apt install -y postgresql postgresql-contrib
sudo systemctl enable --now postgresql
```

### 11.2. Conferir o cluster real

```bash
systemctl is-enabled postgresql
sudo systemctl status postgresql --no-pager
pg_lsclusters
```

No Ubuntu, `postgresql.service` pode aparecer como **`active (exited)`** porque é uma unidade que organiza os clusters. Isso, sozinho, não comprova que o banco está aceitando consultas.

Na saída de `pg_lsclusters`, confira:

- A versão instalada pelos repositórios do Ubuntu em uso.
- O cluster, normalmente chamado `main`.
- A porta, normalmente `5432` numa instalação nova.
- O estado **`online`**.

Se estiver `down`, inicie o cluster real, substituindo `VERSAO` pelo número mostrado:

```text
sudo pg_ctlcluster VERSAO main start
```

O arquivo `/etc/postgresql/VERSAO/main/start.conf` deve indicar `auto` para a inicialização automática do cluster no boot. Confira com:

```text
cat /etc/postgresql/VERSAO/main/start.conf
```

Se estiver `manual`, edite esse arquivo com `sudo nano`, ajuste para `auto`, salve e rode `sudo systemctl daemon-reload`. Em uma instalação nativa nova, normalmente ele já vem como `auto`.

### 11.3. Fazer uma consulta SQL de verdade

```bash
sudo -u postgres psql -c "SELECT version();"
sudo -u postgres psql -c "SELECT current_user, current_database(), now();"
```

O esperado é a versão do PostgreSQL e uma linha com usuário `postgres`, banco `postgres` e data/hora. Esses comandos usam a conta administrativa local do PostgreSQL; não exigem criar uma senha de banco para esta demonstração.

### 11.4. Conferir disponibilidade na rede local da VM

```bash
pg_isready -h 127.0.0.1 -p 5432
sudo ss -ltnp 'sport = :5432'
```

O esperado no primeiro comando é **`accepting connections`**. Ele comprova que o servidor responde na porta, enquanto a consulta SQL anterior comprova execução de consultas com autenticação local.

Se o cluster estiver em outra porta, use a porta exibida em `pg_lsclusters` e ajuste também o arquivo de evidência.

O exercício aceita acesso **local ou externo**. Portanto, não é necessário alterar `listen_addresses`, abrir a porta 5432 para outras máquinas nem mudar a autenticação do banco para cumprir este roteiro.

**Evidência sugerida:** cluster `online`, consulta SQL com resultado e teste `pg_isready`.

## 12. Criar servicos_instalados.txt

O arquivo precisa estar na **mesma pasta dos scripts** e conter os dois programas, o método de instalação e comandos exatos para testar.

Execute o bloco abaixo inteiro na VM. A linha final `EOF` precisa ficar sozinha, sem espaços antes dela.

```bash
cat > "$HOME/scripts/servicos_instalados.txt" <<'EOF'
AV2 - Arquitetura de Computadores
Aluno: Luciano Alves Freire Neto
Sistema operacional: Ubuntu Server

1. Programa: Nginx
Categoria: Servidor Web
Metodo: Nativo, instalado pelo apt.
Inicializacao automatica: sudo systemctl enable --now nginx
Verificar inicializacao: systemctl is-enabled nginx
Verificar estado: sudo systemctl status nginx --no-pager
Testar configuracao: sudo nginx -t
Testar HTTP dentro da VM: curl -I http://127.0.0.1
Resultado esperado: resposta HTTP de sucesso, normalmente 200 OK.
Testar no navegador do hospedeiro com NAT: http://127.0.0.1:8080
Porta do servico na VM: 80/TCP.

2. Programa: PostgreSQL
Categoria: Banco de Dados
Metodo: Nativo, instalado pelo apt.
Inicializacao automatica: sudo systemctl enable --now postgresql
Verificar inicializacao: systemctl is-enabled postgresql
Verificar clusters: pg_lsclusters
Resultado esperado do cluster: online; inicio configurado como auto.
Testar consulta: sudo -u postgres psql -c "SELECT version();"
Resultado esperado da consulta: versao do PostgreSQL exibida.
Testar porta local: pg_isready -h 127.0.0.1 -p 5432
Resultado esperado da porta: accepting connections.
Porta local prevista nesta instalacao: 5432/TCP.
Observacao: postgresql.service pode mostrar active (exited).
A comprovacao do banco e feita pelo cluster online e pela consulta SQL.
EOF
```

Confira:

```bash
cat "$HOME/scripts/servicos_instalados.txt"
ls -lh "$HOME/scripts"
```

O `>` substitui o conteúdo se o arquivo já existir. O texto registra o roteiro escolhido; os resultados devem ser conferidos na sua VM antes da entrega. Ajuste porta e endereço se sua configuração for diferente.

Ao final, a pasta deve conter:

| Arquivo em `~/scripts` | Finalidade |
| --- | --- |
| `coletar_logs.sh` | Script executável de coleta |
| `monitoramento.sh` | Script executável de monitoramento |
| `logs_sistema.txt` | Saída gerada pela coleta |
| `servicos_instalados.txt` | Evidência textual exigida na Parte 3 |

## 13. Reiniciar e fazer a conferência final

É preciso testar o boot para confirmar tanto o desbloqueio quanto a inicialização dos serviços.

1. Salve os arquivos abertos.
2. Reinicie pela VM:

```bash
sudo reboot
```

3. Se estiver conectado por SSH, a sessão será encerrada.
4. Abra a janela da VM no VirtualBox e digite a frase-senha do disco.
5. Aguarde o Linux iniciar e faça login.
6. Confira os serviços e execute os scripts novamente:

```bash
systemctl is-enabled ssh nginx postgresql
systemctl is-active ssh nginx
pg_lsclusters
pg_isready -h 127.0.0.1 -p 5432
sudo -u postgres psql -c "SELECT version();"
curl -I http://127.0.0.1
"$HOME/scripts/coletar_logs.sh"
"$HOME/scripts/monitoramento.sh"
cat "$HOME/scripts/servicos_instalados.txt"
```

7. No Windows, teste de novo `ssh -p 2222 luciano@127.0.0.1` e a página `http://127.0.0.1:8080`.

**Atenção ao funcionamento da criptografia:** “iniciar automaticamente” significa que os serviços sobem quando o sistema consegue iniciar. Com a senha de disco deste roteiro, você precisa desbloquear a VM no console a cada boot antes de SSH, Nginx e PostgreSQL ficarem disponíveis.

### Checklist de entrega

- [ ] VM nomeada **Luciano Alves Freire Neto**.
- [ ] Arquivos da VM dentro da pasta com nome completo em **Documentos** do hospedeiro.
- [ ] **4 GB de RAM**, **pelo menos 4 CPUs** e **disco virtual de 20 GB**.
- [ ] Ubuntu Server instalado e versão conferida.
- [ ] Usuário criado na instalação com acesso sudo funcionando.
- [ ] Para o ponto extra: LVM com LUKS e pedido de senha no boot.
- [ ] Frase-senha disponível para conferência do professor.
- [ ] OpenSSH instalado, disponível e habilitado no boot.
- [ ] Login remoto com o usuário criado na instalação funcionando.
- [ ] Pasta `~/scripts` criada na home correta.
- [ ] `coletar_logs.sh` executável e gerando `logs_sistema.txt`.
- [ ] `monitoramento.sh` executável e mostrando disco, RAM e CPU.
- [ ] Nginx ativo, automático e respondendo HTTP.
- [ ] PostgreSQL com cluster online, início automático e consulta SQL funcionando.
- [ ] `servicos_instalados.txt` com programas, método e comandos de teste.
- [ ] Todos os testes repetidos após reiniciar e desbloquear o disco.

### Ordem sugerida para demonstrar ao professor

1. Mostrar no VirtualBox o nome, a pasta e os recursos da VM.
2. Mostrar a tela de desbloqueio do disco, se for apresentar o ponto extra.
3. Entrar no Linux e mostrar versão e estrutura do armazenamento.
4. Fazer login por SSH pelo Windows.
5. Executar os dois scripts e mostrar o arquivo de logs.
6. Abrir o Nginx no navegador.
7. Executar a consulta SQL do PostgreSQL.
8. Abrir `servicos_instalados.txt`.

O PDF não define quantidade obrigatória de prints nem exige relatório separado. As capturas sugeridas neste guia ajudam na organização e não substituem a VM funcionando.

## 14. Conferir os repositórios do Ubuntu se o apt falhar

Normalmente o instalador configura os repositórios de rede automaticamente. Se `sudo apt update` já funciona, não é necessário editar esses arquivos.

Primeiro confira a versão do Ubuntu e os arquivos existentes:

```bash
cat /etc/os-release
ls -l /etc/apt/sources.list.d/
```

Ubuntu recente costuma usar **`/etc/apt/sources.list.d/ubuntu.sources`**. Instalações mais antigas também podem usar `/etc/apt/sources.list`. A ausência de `sources.list` não significa que os repositórios estejam faltando.

Para localizar entradas de mídia e conferir os espelhos:

```bash
grep -R -n -E 'cdrom:|^deb |^URIs:|^Suites:' /etc/apt/sources.list /etc/apt/sources.list.d/ 2>/dev/null
```

Se houver uma entrada ativa `deb cdrom:` em arquivo `.list`, e o apt estiver pedindo a mídia removida, abra **esse arquivo** com `sudo nano` e coloque `#` no início apenas dessa linha. No formato `.sources`, um bloco de mídia pode ser desativado com `Enabled: no` no bloco correspondente. Preserve os repositórios de rede e repita `sudo apt update`.

Se houver erro de resolução de nomes, confira antes a rede:

```bash
ip -br addr
ip route
getent hosts archive.ubuntu.com
```

As entradas de pacotes devem corresponder ao Ubuntu instalado, conforme `VERSION_CODENAME` em `/etc/os-release`. Se não houver espelho de rede configurado, consulte o professor e a [documentação de gerenciamento de pacotes do Ubuntu](https://ubuntu.com/server/docs/how-to/software/package-management/) antes de editar a configuração.

## 15. Problemas comuns e como resolver

| Problema | Conferência e solução |
| --- | --- |
| VirtualBox não permite 4 CPUs ou não oferece sistema de 64 bits | Verifique os recursos do hospedeiro e a virtualização VT-x/AMD-V; em PC do laboratório, peça ao responsável para conferir. Não reduza o requisito para entregar. |
| A senha não aparece quando digito | É normal no terminal; digite e pressione Enter. Confira o layout se não aceitar. |
| `cd ~` não funcionou | Use `cd "$HOME"` e confira com `pwd`. Para a pasta dos scripts, use `cd "$HOME/scripts"`. |
| `Permission denied` ao executar script | Rode `chmod u+x "$HOME/scripts/"*.sh` e confira se você é dono dos arquivos. |
| Não consigo salvar os arquivos na minha pasta | Se você os criou com sudo, confira `ls -ld "$HOME/scripts"` e `ls -l "$HOME/scripts"`. Corrija apenas o dono dos arquivos/pasta desta atividade; evite alterar permissões gerais do sistema. |
| `sudo: command not found` ou usuário não está no sudoers | Siga a seção 5.1 antes de tentar instalar pacotes; precisa haver acesso administrativo autorizado. |
| `Temporary failure resolving...` no apt | Confira NAT, cabo conectado, endereço em `ip -br addr` e resolução com `getent hosts archive.ubuntu.com`. Corrija a rede antes de repetir `sudo apt update`. |
| O apt pede o CD/DVD ou `sources.list` não existe | Veja a seção 14; o Ubuntu recente costuma usar `/etc/apt/sources.list.d/ubuntu.sources`. |
| Script de coleta pede senha | É o sudo consultando os logs do sistema; use a senha do usuário Linux. |
| Log tem menos de 50 entradas | Pode haver poucos registros na VM; confira `sudo journalctl --no-pager -n 50`. |
| SSH dá `Connection refused` | Confira VM ligada/desbloqueada, porta NAT 2222 → 22, `systemctl status ssh` e listener na porta 22. |
| SSH fica aguardando e expira | Confira redirecionamento, IP usado e firewall; no NAT deste guia, o Windows usa 127.0.0.1 e porta 2222. |
| SSH dá `Permission denied` | Confira nome de usuário, senha e autenticação efetiva com `sshd -T`. A senha do disco não substitui a senha do usuário. |
| Porta 2222 ou 8080 já está ocupada no Windows | Escolha outra porta do hospedeiro, por exemplo 2223 ou 8081, e ajuste o comando SSH ou URL; mantenha as portas 22 e 80 do convidado. |
| Nginx funciona na VM, mas não abre no Windows | Confira a regra NAT 8080 → 80 e use `http://127.0.0.1:8080`; confira UFW caso esteja ativo. |
| Nginx não inicia por porta ocupada | Veja `sudo ss -ltnp 'sport = :80'`; outro servidor web pode estar usando a porta. Identifique o serviço antes de alterar a configuração. |
| PostgreSQL aparece `active (exited)` | Confira `pg_lsclusters`, `pg_isready` e consulta SQL; veja a seção 11. |
| `psql` mostra `could not change directory` | Se a home atual não é acessível ao usuário postgres, rode `cd /tmp` e repita a consulta; isso não troca a pasta onde os scripts foram salvos. |
| Após reboot não consigo conectar em nenhum serviço | Abra o console da VM: o sistema pode estar aguardando a frase-senha do LUKS. |
| Script colado do Windows dá erro com `\r` ou `bad interpreter` | Salve no Nano da VM ou configure finais de linha **LF** no editor; não use CRLF no `.sh`. |

### Comandos rápidos para diagnóstico

Execute conforme o problema; não é um instalador automático:

```bash
ip -br addr
sudo systemctl status ssh nginx postgresql --no-pager
sudo journalctl -u ssh -n 20 --no-pager
sudo journalctl -u nginx -n 20 --no-pager
pg_lsclusters
sudo ss -ltnp
df -h
```

## 16. Referências para consultar

- Enunciado fornecido: `AV2-Arquitetura de Computadores_Noite.docx.pdf`, páginas 1 a 3.
- [Ubuntu Server: download e versões](https://ubuntu.com/download/server).
- [Instalador Ubuntu: telas da instalação](https://canonical-subiquity.readthedocs-hosted.com/en/latest/tutorial/screen-by-screen.html).
- [Instalador Ubuntu: configuração de armazenamento e LUKS](https://canonical-subiquity.readthedocs-hosted.com/en/latest/howto/configure-storage.html).
- [Ubuntu Server: usuários e privilégios administrativos](https://ubuntu.com/server/docs/how-to/security/user-management/).
- [Ubuntu Server: OpenSSH](https://ubuntu.com/server/docs/how-to/security/openssh-server/).
- [Ubuntu Server: instalação de Nginx](https://ubuntu.com/server/docs/how-to/web-services/install-nginx/).
- [Ubuntu Server: instalação e configuração do PostgreSQL](https://ubuntu.com/server/docs/how-to/databases/install-postgresql/).
- [Ubuntu Server: gerenciamento de pacotes](https://ubuntu.com/server/docs/how-to/software/package-management/).

Para consultar a documentação instalada na própria VM: `man journalctl`, `man df`, `man free`, `man uptime` e `man systemctl`. Pressione **q** para sair das páginas de manual.
