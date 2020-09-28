import discord

quotes = ["Mais nada vai sair do armário pra assustar você",

"Aquela coisa é uma arma de matar! Aposto que está só esperando nós dormir, e então nhaque!",

"As crianças de hoje em dia não se assustam como antigamente.",

"Claro que aprendi com o melhor.",

"Cuidarei bem da criança.",

"Deixe uma porta aberta e uma criança poderá entrar nesta fábrica. No mundo dos monstros!",

"Ele arruinou minha vida, e pelo quê? Pela droga de uma criança!",

"Está ficando mais difícil assustar crianças humanas.",

"Estou muito bem hoje. Vou assustar para valer.",

"Estou prestes a revolucionar a indústria dos sustos.",

"Eu sou tão romântico às vezes, que eu acho que eu deveria me casar comigo mesmo.",

"Há um futuro brilhante na Monstros S.A.",

"Isto pode parecer loucura, mas não acho que essa criança seja perigosa.",

"Monstros assustadores não têm placa.",

"Não deixe a criança tocar em você.",

"Não há nada mais tóxico ou fatal que uma criança humana.",

"Não se deve dar nomes. Quando se dá um nome, se fica apegado.",

"Nossa cidade depende de vocês para coletar os gritos das crianças. Sem gritos não temos energia.",

"Preciso de assustadores confiantes, determinados, durões, intimidadores.",

"Sabe, a vida oferece mais coisa além de assustar.",

"Se as testemunhas forem confiáveis, uma criança passou pela segurança pela primeira vez na história dos monstros.",

"Sinto muito não estar ao seu lado antes, mas agora estou. Estou me abrindo aqui. Poderia pelo menos prestar atenção!",

"Você é o chefe, você é o grande chefe peludo.",
]


# var name == command name
close = 'Tchau monstros! Até mais...🧟‍♂️😞'
policy = 'Meu compromisso é com a transparência e o código aberto, caso queira ver os registros de auditoria/log de mensagem é só ir no respectivo canal que você o verá.🧐🧐🧐 \n github repo: https://github.com/faelbreseghello/Monsters-Bot'
setup = 'Pronto! O jogo já vai começar!'
fun = 'Olha essa daqui!:'
trakinas = 'APOIE, APOIE TRAKINAS LIMÃO.🍪🍪🍪🍪'

# minigame msg
winmsg1 = 'O monstro ' # pt1
winmsg2 = ' venceu a rodada.\n -------------------------------' # pt2
startmsg = 'Assustadores, preparem-se! Chegou a hora de assustar!\n VALENDO!'
ptsmsg = 'tem'
ptserror = 'Provavelmente não iniciou o jogo ainda :('
emojis = {'vermelho': '🔴',
          'verde' : '🟢',
          'azul' : '🔵',
          'amarelo' : '🟡'}

#help embed
helpmsg = discord.Embed(title='Comandos:', colour = discord.Colour.blue())
helpmsg.set_author(name='Ajuda')
helpmsg.set_thumbnail(url='https://cdn.discordapp.com/avatars/747449463861149737/38b60ffd2fce04ea1e607179acf70a79.png')
helpmsg.add_field(name='*policy', value='Minha forma monstruosa de pensar.', inline=True)
helpmsg.add_field(name='*setup', value='Definir o canal que será utilizado para o minigame. Recomenda-se que apenas o eu possa enviar mensagens por lá.', inline=False)
helpmsg.add_field(name='*fun', value='Pequenos trechos dos monstros conversando. Quem precisa de autoajuda quando se tem monstroterapia?', inline=True)
helpmsg.add_field(name='*meme', value='Um meme aleatório da nossa base MONSTRUOSA 🧟‍♂️🧟‍♂️.', inline=False)
helpmsg.add_field(name='*pts', value='Uma dm com os pontos da pessoa mencionada do minigame.', inline=True)
helpmsg.add_field(name='*trakinas', value='Campanha de caridade :100% sério:', inline=False)
helpmsg.add_field(name='Minigame', value='De tempos em tempos há uma chance de ser enviada uma mensagem em que o primeiro monstro que reagir ganha pontos. No final do mês o melhor ganha um prêmio.', inline=True)
helpmsg.set_footer(text='*todos os comandos, por padrão acompanham o prefixo *. Mas você pode mudar em config.py')

react = ' Reaja com'

# other
statusmsg = ['Feito com ❤️ por faelbreseghello#3092', 'Me siga no twitter: @faelbreseghello', 'Meu código é aberto!', 'Veja os comandos com *help...']
welcomemsg = 'Bem vindo ao server, eu sou o Monsters Bot. Se quiser saber mais sobre mim acesse meu repositorio no github : https://github.com/faelbreseghello/Monsters-Bot.\n As regras do minigame são simples: Seja o primeiro assustador e ganhe pontos. Depois tente ser o melhor de todos! 🧟‍♂️🧟‍♂️🧟‍♂️🧟‍♂️'
month = 'mês'
giferror = 'Algo deu errado :('
