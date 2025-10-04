# Taller de git

Repo para la charla de git de la hacktober week.
Incluye un modulo "calculator" sin terminar para que los participantes tengan la oportunidad de trabajar sobre un repositorio e implementar lo impartido en el taller.

# English guide

## Set up

Clone the repo:

```bash
git clone https://github.com/aulasoftwarelibre/taller-git.git taller-git
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

Push your branch to the remote repository:

```bash
git push -u origin your-new-branch
```

Then create a pull request in the repository's GitHub.



# Guía en español

## Primeros pasos

Clona el repositorio localmente:

```bash
git clone https://github.com/aulasoftwarelibre/taller-git.git taller-git
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

Haz un push de tu rama al repositorio original de github:

```bash
git push -u origin your-new-branch
```

Ya solo tienes que crear una nueva pull request desde el GitHub del repo para añadir tus cambios.
Recuerda hacer push de los cambios que hagas localmente al repositorio remoto con el comando anterior!