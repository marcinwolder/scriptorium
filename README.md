# Scriptorium 📖

Programming language stylized after natural language - **Latin**.  

## ⚙ Requirements:

* Python 3.13
* Modules from `./reguirements.txt`

## 🎮 How to use:

### 🛠 Build (Windows)
1. Activate **venv*
```bash
$ source venv/Scripts/activate
```
2. Build project
```bash
$ cd ./Scriptorium
$ antlr4 ./Scriptorium.g4 -visitor -Dlanguage=Python3
```
3. Create file with `.st` extension
```bash
$ touch program.st
```
4. Run program
```bash
py main.py program.st
```
---
\*How to create venv:
```bash
$ py -3.13 -m venv venv
$ source venv/Scripts/activate
$ pip install -r requirements.txt
``` 

## 📑 Repository Structure
```bash
.
├───Scriptorium
│   └───Scriptorium.g4 # Grammar of the language
├───.gitignore
├───main.py # Language interpreter
├───README.md
├───requirements.txt
└───ScriptoriumVisitor.py # Language visitor
```