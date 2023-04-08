eps = [
    {"nome": "Italo Vinicius Pereira Guimarães", "git": "italovinicius18 "},
    {"nome": "Ian Fillipe Pontes Ferreira", "git": "IanFPFerreira"},
    {"nome": "Gabriel Avelino", "git": "gabrielavelino"},
    {"nome": "Guilherme de Morais Richter", "git": "guilhermemoraisr"},
    {"nome": "Álvaro Leles Guimarães ", "git": "AlvaroLeles"},
    {"nome": "Ítalo Fernandes Sales de Serra", "git": "italofernandes13"},
    {"nome": "Gabriel Bonifácio Perez Nunes", "git": "gabrielbpn"},
]

mds = [
    {"nome": "Mariana Letícia Santos da Cruz", "git": "Marianannn"},
    {"nome": "Arthur Miranda Suares", "git": "Dyetrix"},
    {"nome": "Júlia Stefanie Santos Mendonça", "git": " juliassmendonca"},
    {"nome": "Mateus Fidelis Marinho Maia", "git": "MatsFidelis"},
    {"nome": "Amanda Gonçalves Sobrinho Abreu", "git": "Amandaaaaabreu"},
    {"nome": "Fause Carlos M Lustosa Junior", "git": "FauseSkyWalker"},
    {"nome": "Arthur Rodrigues Sousa ", "git": "arthurrsousa"},
    {"nome": "Gustavo Costa de Jesus", "git": "cwtshh"},
    {"nome": "Filipe Souto de Andrade", "git": "fillipeb50"},
    {"nome": "Gabriel Saraiva Canabrava", "git": "gabrielsarcan"},
]


def get_first_two_names(name):
    names = name.split(" ")
    return names[0] + " " + names[1]


for members in mds:
    string = f"""
        <div>
            <a href="https://github.com/{members['git']}">
                    <img style="border-radius: 50%;"         src="https://github.com/{members['git']}.png" width="100px;"/>
                    <h5 class="text-center">{get_first_two_names(members['nome'])}</h5>
            </a>       
        </div>"""
    print(string)
