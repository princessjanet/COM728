def welcome():
    print(f"\n-----------------------"
          "\nCOVID-19 (January) Data"
          "\n-----------------------")


welcome()


def error(msg):
    print("'Error!'" + msg)

error("error_msg")

def progress(operation, value):
    print(f"{operation} status")

    if value == 0:
        print("has started")
    if value >0<100:
        print("is in progress ({value}%) completed")
    if value == 100:
        print("has completed")

progress("calculation", 50)

