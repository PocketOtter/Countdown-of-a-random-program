import time

################################################################################
#                                                                              #
"                     RUN PROGRAM IF KEY != START                              "
#                                                                              #
################################################################################


key = input("Enter the key: ")

if key == "start":
    for i in reversed(range(11)):
        time.sleep(0.5)
        print("T-Minus", i)
        if i == 0:
            time.sleep(0.5)
            print("Ready to fire, sir.")


################################################################################
#                                                                              #
"                     TERMINATE PROGRAM IF KEY != START                        "
#                                                                              #
################################################################################


if key != "start":
    for i in reversed(range(11)):
        time.sleep(0.5)
        print("Terminating Program in", i)
        if i == 0:
            time.sleep(0.5)
            print("P R O G R A M  T E R M I N A T E D")
            exit()


################################################################################
#                                                                              #
"                     RUN PROGRAM IF KEY2 == FIRE                              "
#                                                                              #
################################################################################


time.sleep(0.5)
key2 = input("Enter the key: ")

if key2 == "fire":
    time.sleep(0.5)
    print("Bomb fired, sir")


################################################################################
#                                                                              #
"                     TERMINATE PROGRAM IF KEY2 != FIRE                        "
#                                                                              #
################################################################################


if key2 != "fire":
    for i in reversed(range(11)):
        time.sleep(0.5)
        print("Terminating Program in", i)
        if i == 0:
            time.sleep(0.5)
            print("P R O G R A M  T E R M I N A T E D")
            exit()