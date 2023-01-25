def startup():
    print("-------------------------------------------------------")
    print("-------------- Welcome to Scene Control ---------------")
    print("-------------------------------------------------------")
    print("")
    print("           Are you using multiple Screens ?")
    print("")
    print("===============  ===============   ||   ===============")
    print("|             |  |             |   ||   |             |")
    print("|             |  |             |   or   |             |")
    print("|             |  |             |   ||   |             |")
    print("===============  ===============   ||   ===============")
    print("")
    multiple_screens = input("(y/n):")
    print("")
    print("      Are you remotely accessing these instances ?")
    print("")
    remote_access = input("(y/n):")
    print("")

    if multiple_screens == "y" and remote_access == "y":
        setup = 1
    elif multiple_screens == "n" and remote_access == "y":
        setup = 2
    elif multiple_screens == "y" and remote_access == "n":
        setup = 3
    else:
        setup = 4

    print("                  Setup Version:", setup)
    print("")

def create_arrays():
    """ Create array and assign default values """
    scans = 0
    processed = []
    registered = []
    aligned = []
    point_cloud = []
    exported = []
