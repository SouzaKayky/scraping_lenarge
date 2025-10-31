Você pode criar uma pasta chamada, por exemplo:

vscode-setup/
│
├── extensions.txt
├── settings.json

a) Exportar extensões instaladas

No VS Code, abra o terminal e rode:

code --list-extensions > vscode-setup/extensions.txt

Isso gera um arquivo extensions.txt com todas as extensões instaladas.
Como usar a pasta em outro computador
Copie a pasta vscode-setup/ para o novo computador.
Instale todas as extensões do extensions.txt de forma automática no Windows, se estiver usando PowerShell:

Get-Content extensions.txt | ForEach-Object { code --install-extension $_ }