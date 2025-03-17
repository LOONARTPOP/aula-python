// Função para exibir o menu de escolha de acesso
void displaymenu(){
  printf("Escolha a sua forma de acesso:\n");
  printf("1. Administrador\n");
  printf("2. Usuário\n");
  printf("3. Visitante\n");
}

int main(){
  // Configura o locale para exibir mensagens em português
  setlocale(LC_ALL, "Portuguese_Brazil");

  int opcao; // Variável para armazenar a opção escolhida pelo usuário
  char nome[30]; // Variável para armazenar o nome digitado pelo usuário
  char senha[20]; // Variável para armazenar a senha digitada pelo usuário
  int acesso_permitido = 0; // Variável para controlar se o acesso foi permitido ou não

  // Exibe o menu de escolha de acesso
  displaymenu();

  // Solicita ao usuário que escolha uma opção e armazena a escolha na variável 'opcao'
  printf("Opção:");
  scanf("%d", &opcao);

  // Loop para garantir que o acesso seja permitido antes de prosseguir
  while(!acesso_permitido){
    switch(opcao){
      case 1:
        // Solicita ao administrador que insira seu nome
        printf("Insira seu nome de administrador:\n");
        scanf("%s", nome);
        // Solicita ao administrador que insira sua senha
        printf("Insira sua senha:\n");
        scanf("%s", senha);
        // Verifica se o nome e a senha fornecidos estão corretos para o administrador
        if(strcmp(nome, "admin") == 0 && strcmp(senha,"admin123") == 0){
          // Se as credenciais estiverem corretas, exibe uma mensagem de boas-vindas para o administrador
          printf("Acesso permitido. Bem-vindo administrador!\n");
          // Define 'acesso_permitido' como verdadeiro para sair do loop
          acesso_permitido = 1;
        } else {
          // Se as credenciais estiverem incorretas, exibe uma mensagem de acesso negado e solicita que o usuário tente novamente
          printf("Acesso negado. As credenciais informadas estão incorretas.\n");
          printf("Por favor, tente novamente.\n");
          printf("Opção: ");
          // Solicita uma nova opção de acesso ao usuário
          scanf("%d", &opcao);
        }
        break;
      case 2:
        // Solicita ao usuário que insira seu nome
        printf("Insira seu nome de usuário:\n");
        scanf("%s", nome);
        // Solicita ao usuário que insira sua senha
        printf("Insira sua senha:\n");
        scanf("%s", senha);
        // Verifica se o nome e a senha fornecidos estão corretos para o usuário
        if(strcmp(nome, "usuario1") == 0 && strcmp(senha, "senha123") == 0){
          // Se as credenciais estiverem corretas, exibe uma mensagem de boas-vindas para o usuário
          printf("Acesso permitido. Bem-vindo usuário!\n");
          // Define 'acesso_permitido' como verdadeiro para sair do loop
          acesso_permitido = 1;
        } else {
          // Se as credenciais estiverem incorretas, exibe uma mensagem de acesso negado e solicita que o usuário tente novamente
          printf("Acesso negado. As credenciais informadas estão incorretas.\n");
          printf("Por favor, tente novamente.\n");
          printf("Opção: ");
          // Solicita uma nova opção de acesso ao usuário
          scanf("%d", &opcao);
        }
        break;
      case 3:
        // Solicita ao visitante que insira seu nome
        printf("Insira seu nome de visitante:\n");
        scanf("%s", nome);
        // Solicita ao visitante que insira sua senha
        printf("Insira a senha:\n");
        scanf("%s", senha);
        // Verifica se o nome e a senha fornecidos estão corretos para o visitante
        if(strcmp(nome, "visitante") == 0 && strcmp(senha, "visitante123") == 0){
          // Se as credenciais estiverem corretas, exibe uma mensagem de boas-vindas para o visitante
          printf("Acesso permitido. Bem-vindo visitante!\n");
          // Define 'acesso_permitido' como verdadeiro para sair do loop
          acesso_permitido = 1;
        } else {
          // Se as credenciais estiverem incorretas, exibe uma mensagem de acesso negado e solicita que o visitante tente novamente
          printf("Acesso negado. As credenciais informadas estão incorretas.\n");
          printf("Por favor, tente novamente.\n");
          printf("Opção: ");
          // Solicita uma nova opção de acesso ao visitante
          scanf("%d", &opcao);
        }
        break;
      default:
        // Se o usuário escolher uma opção inválida, exibe uma mensagem de erro e solicita que o usuário escolha novamente
        printf("Por favor, escolha uma opção válida.\n");
        printf("Opção: ");
        // Solicita uma nova opção de acesso ao usuário
        scanf("%d", &opcao);
    }
  }

  return 0;
}

