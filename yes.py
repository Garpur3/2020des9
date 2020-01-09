class Tiem:
    tiems = {}

    def __init__(self):
        pass

    def set(id):
        if id in Tiem.tiems.keys():
            print("ID in use")
        else:
            Tiem.tiems[id] = get_time()

    def delta(id):
        if id in Tiem.times.keys():
            return get_time() - Tiem.tiems[id]
        else:
            print("ID not in use")