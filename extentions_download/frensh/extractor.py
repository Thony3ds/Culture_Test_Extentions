import os, shutil

def exctraction():
    print("start....")
    file = input("test dirrectory name: ")
    langue = input("language (in english): ")
    file_analyse = os.path.dirname(os.path.abspath(__file__)) + "/Culture_Test_Extentions/extentions/" + langue + "/" + file
    try :
        print("start exctracting....")
        source_folder = file_analyse
        destination_folder = os.path.dirname(os.path.abspath(__file__))

        shutil.move(source_folder, destination_folder)
        print("extract succeful finalising....")
        dossier_a_supprimer = "Culture_Test_Extentions"

        shutil.rmtree(dossier_a_supprimer)
        print("Finish")
    except ValueError:
        print("Error")

if __name__ == "__main__":
    exctraction()