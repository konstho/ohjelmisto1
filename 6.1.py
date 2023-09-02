import random
def noppa():
    return random.randint(1,6)
def main():
    while True:
        luku = noppa()
        print("heitto" , luku)
        if luku == 6:
            break
