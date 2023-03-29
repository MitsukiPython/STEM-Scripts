from math import log



def main():
    while True:
        try:
            rateofdecay = input("Annual Rate of Decay:  ")

            if not rateofdecay.strip().endswith("%") and rateofdecay.strip("%").isdigit():
                raise ValueError


            rateofdecay = 1-(float(rateofdecay.strip().strip("%"))/100)
            half_life = round(log(0.5, rateofdecay), 3)
            print(half_life, " years")


        except EOFError:
            break
        except:
            print("Please input a number")



if __name__ == "__main__":
    main()
