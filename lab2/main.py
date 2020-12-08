import first_part
import second_part


while True:
    print("\n\n")
    inline = input("Write CCP or CCS to change cross correlation method:\t")
    if inline.lower() == "ccp":
        first_part.CCP()
    elif inline.lower() == "ccs":
        second_part.CCS()

    elif inline.lower() == "exit":
        break
    else:
        print("Wrong input. You can write only CCP, CCS and exit.")
