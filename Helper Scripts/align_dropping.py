from seq_duplicated import getSeq
import random

def getListOfDifferentDomains(mafft_dict):
    normal = list()
    abnormal = list()
    other = list()
    for i in mafft_dict:
        if mafft_dict[i]["seq"][:55] == "------------------------------------------------------M":
            normal.append(mafft_dict[i]["name"])
        elif mafft_dict[i]["seq"][:4] == "---M":
            abnormal.append(mafft_dict[i]["name"])
        else:
            other.append(mafft_dict[i])

    return normal, abnormal, other

def listHave(species, liste):
    for i in liste:
        print(i)
        if i["name"] == species:
            return i
    return None



def createFastaFileFromNewList(seq_dict, liste, path):

    output_file = open(path, "w+")
    for i in seq_dict:
        if seq_dict[i]["name"] in liste:
            output_file.write(f">{seq_dict[i]['name']}\n")
            output_file.write(f"{seq_dict[i]['seq']}\n")


def getRandomSpecies(species_dictionary):
    """
    print random species from different groups that clustering in big tree
    """
    normal, abnormal, other = getListOfDifferentDomains(species_dictionary)

    print("\n\nABNORMAL ONES")
    abnormal_random = random.sample(range(1, 85), 5)
    for i in abnormal_random:
        print(normal[i])

    print("\n\nNORMAL ONES")
    normal_random = random.sample(range(1, 883), 5)
    for j in normal_random:
        print(normal[j])

    print("\n\nOTHERS")
    for k in other:
        print(k)



if __name__ == '__main__':
    # TODO: change filenames
    path = "./aligments"
    mafft = "/mafft_aligned.fasta"

    mafft_dict = getSeq(path, mafft)

    # In order to coloured tree
    getRandomSpecies(mafft_dict)

    # Seperate clusters to different fasta files
    normal, abnormal, other = getListOfDifferentDomains(mafft_dict)
    seq_dict = getSeq(path, "/blast_dropped283.fasta")
    createFastaFileFromNewList(seq_dict, normal, path+"/normal_883.fasta")
    createFastaFileFromNewList(seq_dict, abnormal, path+"/abnormal_85.fasta")






