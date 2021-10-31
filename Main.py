from objects import Chara as ch


def main():
    a = ch.Chara(1,"aa")
    print(a.id)
    i = ch.NomalChara(12,"ss")
    print(i.name)
    murabit = ch.NomalChara(221,"baka")
    print(murabit.id)

if __name__ == "__main__":
    main()