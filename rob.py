import requests
import time

print('Robson has awaken')

webhook = 'https://discordapp.com/api/webhooks/513499673038684177/Sx3NinnQ9rjxwI8NXAo9SCFw9dxyRbR54XUlnvszz3DNSlMbTeLqmnSLLSwVYczFjpDZ'
anilist = 'https://graphql.anilist.co'

query = '''
query ($id: Int!) {
  Media(id: $id, type: ANIME) {
    airingSchedule {
      nodes {
        id
        airingAt
        timeUntilAiring
        episode
      }
    }
  }
}
'''

# ------------------------------------------------------------------------------------------------------------------------------#

animedict = {
    'alicization': {
        'id': 100182,
        'name': 'Sword Art Online: Alicization',
        'link': 'http://bit.ly/Harmony-SAOAlicization'
    },
    'goblinslayer': {
        'id': 101165,
        'name': 'Goblin Slayer',
        'link': 'http://bit.ly/Harmony-GoblinSlayer'
    },
    'bunnygirl': {
        'id': 101291,
        'name': 'Bunny Girl',
        'link': 'http://bit.ly/Harmony-BunnyGirl'
    },
    'slime': {
        'id': 101280,
        'name': 'Tensei Shitara Slime Datta Ken',
        'link': 'bit.ly/Harmony-Slime'
    },
    'blackclover': {
        'id': 97940,
        'name': 'Black Clover',
        'link': 'http://bit.ly/Harmony-BlackClover'
    },
    'test': {
        'id': 101316,
        'name': 'Irozuku Sekai no Ashita kara',
        'link': 'BETA TESTING'
    }
}

# ------------------------------------------------------------------------------------------------------------------------------#

ncount = 0

for anime in animedict:

    print('\n', 'Inicializando verificação de {}'.format(animedict[anime]['name']))

    req = requests.post(anilist, json={'query': query, 'variables': animedict[anime]})
    schedule = req.json()

    for a in schedule['data']['Media']['airingSchedule']['nodes']:
        untilTime = a['timeUntilAiring']
        episode = a['episode']

        if untilTime <= 21600 and untilTime >= -64801:
            if untilTime > 0:
                tm = untilTime / 3600

                msg = '''@Oráculo
Episódio {} de {} vai sair em aproximadamente {:.0f} horas.

Link: {}
{}'''.format(a['episode'], animedict[anime]['name'], tm, animedict[anime]['link'], '-=-'*20)

                requests.post(webhook, data={'username': 'Robson',
                                             'avatar_url': 'https://i.imgur.com/6QqIRB8.png',
                                             'content': msg})
                print('Notificação enviada.')
                ncount += 1

            else:
                tm = untilTime / 3600

                msg = '''@Oráculo
Episódio {} de {} saiu a aproximadamente {:.0f} horas.

Link: {}
{}'''.format(a['episode'], animedict[anime]['name'], -tm, animedict[anime]['link'], '-=-'*20)

                requests.post(webhook, data={'username': 'Robson',
                                             'avatar_url': 'https://i.imgur.com/6QqIRB8.png',
                                             'content': msg})
                print('Notificação enviada.')
                ncount += 1
        else:
            pass

    print('Veificação concluida com sucesso.')
print('\n')
