# Taller de git

Repo para la charla de git de la hacktober week.
Incluye un modulo "calculator" sin terminar para que los participantes tengan la oportunidad de trabajar sobre un repositorio e implementar lo impartido en el taller.

# Antes de empezar

Si no la tienes, asegurate de configurar una clave ssh, para ello:

1. Verifica si la tienes con el comando `ls -al ~/.ssh`
Si aparece `id_rsa o id_ed25519`, ya tienes una.

2. Si no tienes, genera una:

```bash
ssh-keygen -t ed25519 -C "tu_email@ejemplo.com"
```

(dale Enter a todo).

Activa el agente ssh y añade tu clave:

```bash
eval "$(ssh-agent -s)"
ssh-add ~/.ssh/id_ed25519
```

Copia tu clave pública:

```bash
cat ~/.ssh/id_ed25519.pub
```

y pégala en GitHub:
Settings > SSH and GPG Keys > New SSH key.

Prueba conexión:

```bash
ssh -T git@github.com
```


Te debe salir un mensaje tipo:
"Hi usuario! You've successfully authenticated..."

# English guide

## Set up

Clone the repo:

```bash
git clone git@github.com:aulasoftwarelibre/taller-git.git taller-git
```

Now you are able to add changes to this repository!

Create a new branch in order to start working:

```bash
git branch your-new-branch
```
(your-new-branch its an example of a name, you may choose any name you want)

Move to your new branch:

```bash
git checkout your-new-branch
```

You can also create a branch and move to it directly with the following shortcut:

```bash
git checkout -b your-new-branch
```

## Adding changes

Stage your changes:

```bash
git add changed-file-route
```

Commit your changes to your current branch:

```bash
git commit -m "changes-title"
```

Push your branch to the remote repository:

```bash
git push -u origin your-new-branch
```

Then you can create a pull request in the repository's GitHub!

If git ask you for an user/password, avoid it with ctrl+C and use the following command:

```bash
git remote set-url origin git@github.com:aulasoftwarelibre/taller-git.git
```


# Guía en español

## Primeros pasos

Clona el repositorio localmente:

```bash
git clone git@github.com:aulasoftwarelibre/taller-git.git taller-git
```

Ya puedes empezar a trabajar remotamente en el proyecto!

Crea una nueva rama para trabajar correctamente:

```bash
git branch your-new-branch
```
(your-new-branch es un nombre de ejemplo para tu nueva rama)

Muevete a tu nueva rama:

```bash
git checkout your-new-branch
```

También puedes crear una rama y moverte a ella directamente con el siguiente atajo:

```bash
git checkout -b your-new-branch
```

## Añadiendo cambios

Escoge los cambios que quieras subir:

```bash
git add changed-file-route
```

Confirma los cambios en tu rama:

```bash
git commit -m "changes-title"
```

Haz un push de tu rama al repositorio original de github:

```bash
git push -u origin your-new-branch
```

Ya solo tienes que crear una nueva pull request desde el GitHub del repo para añadir tus cambios.
Recuerda hacer push de los cambios que hagas localmente al repositorio remoto con el comando anterior!

Si git te pide un usuario/contraseña, evita el input con ctrl+C e introduce el siguiente comando:

```bash
git remote set-url origin git@github.com:aulasoftwarelibre/taller-git.git
```