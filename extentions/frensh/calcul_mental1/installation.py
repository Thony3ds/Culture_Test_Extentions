import os, shutil

def exctraction():
    print("start....")
    try :
        print("start exctracting....")
        source_folder = "calcul_mental1.json"
        text = os.path.dirname(os.path.abspath(__file__))
        destination_folder = text.replace("extentions/frensh/calcul_mental1", "assets/jsons/frensh")

        shutil.move(source_folder, destination_folder)
        print("extract succeful finalising....")
        print("Finish")
    except ValueError:
        print("Error")

if __name__ == "__main__":
    question = float(input("4+4= ?: "))
    if question == 8:
        exctraction()
    else:
        print("not good answer")