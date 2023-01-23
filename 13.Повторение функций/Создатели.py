def creators(star_name, planets=8, alive=True):
    if alive:
        alive_text = 'Жизнь есть!'
    else:
        alive_text = 'Жизни нет.'

    creating_world = '''Система звезды {star}.
Количество планет: {planets_num}.
{alivetxt}'''

    output_world = creating_world.format(star=star_name, planets_num=planets, alivetxt=alive_text)

    return output_world
