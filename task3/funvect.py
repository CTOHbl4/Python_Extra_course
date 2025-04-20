def superposition(funmod, funseq):
    res = []
    for fun in funseq:
        # в замыкание может попасть только funmod, он общий
        # в каждом новом объекте new_f связываем текущий fun
        # значением по умолчанию аргумента.
        # каждый fun связан соотв. new_f.
        def new_f(x, inner_func=fun):
            # в closure положили только имя funmod
            return funmod(inner_func(x))
        res.append(new_f)
    return res
    # заполнили имя funmod ссылкой на объект, на который в этот
    # момент указывает имя funmod.
# сначала в замыкании только имя.
# значение, соответствующее имени кладётся только
# при выходе из определения внешней функции.
