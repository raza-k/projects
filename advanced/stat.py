kills = {
    "raza": 123,
    "hadi": 109,
    "yayah": 512,
    "raed": 4
}

games = {
    "raza": 5,
    "hadi": 23,
    "yayah": 543,
    "raed": 1293
}

deaths = {
    "raza": 9,
    "hadi": 23,
    "yayah": 43,
    "raed": 9898
}

x = [23, 54, 678, 123]


def stats(name):
    kd = kills[name] / deaths[name]
    print(f"{name} has k/d of {kd}")


stats("raed1")

