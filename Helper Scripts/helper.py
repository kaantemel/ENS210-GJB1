import pandas as pd

def getSeq(path, filename):
    """
    :param path: path to files
    :param filename: name of the file
    :return: dictionary that include each sequences and their names
    """
    tmp = dict()
    with open(path+filename) as file:
        lines = file.readlines()
        counter = 0
        for line in lines:
            if line[0] == ">":
                # HEADER
                name = line[1:-1]
                counter += 1
                tmp[counter] = {
                    "name": name,
                    "seq": ""
                }
            else:
                # SEQ
                tmp[counter]["seq"] += line[:-1]
    return tmp

def cleanHeader(path, blast):
    """
    take fasta file's path and clean its headers -> only species' name
    """
    output = open(path + "/header_cleaned.fasta", "w+")
    with open(path+blast) as file:
        lines = file.readlines()
        for line in lines:
            if line[0] == ">":
                splitted = line.split(" [")
                name = splitted[-1]
                line = ">" + name[:-2] + "\n"
            output.write(line)
    output.close()

def seqDict2DataFrame(data):
    """
    :param data: format that we can turn dictionary to data frame that we can analyse easily
    """
    df = pd.DataFrame(data, columns=['species', 'sequences'])
    return df

def CSV2FastaFile(df, output_path):
    """
    get CSV data frame and create new fasta file from that
    """
    output_file = open(output_path, "w+")
    # count = 0
    for i, row in df.iterrows():
        # if i > 0 and count < 49:
        output_file.write(f">{i}-{row['species']}\n")
        output_file.write(f"{row['sequences']}\n")
        # count+=1
    output_file.close()

def dropDuplicate(df):
    """
    find duplicated rows which species' name and sequences is equal
    """
    dropped = df.drop_duplicates(subset=["species", "sequences"], keep="first")
    return dropped

def properFormat(seq_dict):
    """
    get dictionary which is read from file and return proper format that could be turned to data frame
    """
    species = [seq_dict[i]["name"] for i in seq_dict]
    sequences = [seq_dict[i]["seq"] for i in seq_dict]
    return {
        "species": species,
        "sequences": sequences
    }

def getProperSpeciesName(species_name):
    """
    put "_" between species' name that is proper in clustal format
    --> clustal is not accept space seperated species name
    """
    listOfName = species_name.split()
    output_name = ""
    for i in listOfName:
        output_name += i + "_"
    return output_name[:-1]

def CSV2ClustalFile(df, path):
    """
    get dataframe and create clustal file from that
    """
    output_file = open(path, "w+")
    for i, row in df.iterrows():
        if i > 0:
            name = getProperSpeciesName(row["species"])
            output_file.write(f">{i}_{name}\t{row['sequences']}\n")
    output_file.close()

def fastaToClustal(path, fasta):
    """
    get fasta file and return its clustal format
    """
    seq_dict = getSeq(path, fasta)
    data = properFormat(seq_dict)
    df = seqDict2DataFrame(data)
    CSV2ClustalFile(df, path+"/mafft_aligned.clustal")


if __name__ == '__main__':
    # TODO Change filenames
    path = "./aligments"
    blast = "/blast.fasta"

    fastaToClustal(path, "/out.fasta")
    cleanHeader(path, blast) # DONE

    sequence = getSeq(path, "/header_cleaned.fasta")          # {"counter": {"name": species_name, "seq": aa_sequence} ...}
    data = properFormat(sequence)                             # It is just proper format that we access all species and sequences in lists
    df = seqDict2DataFrame(data)                              # Pandas dataframe that we will use in drop
    dropped = dropDuplicate(df)                               # if name1 == name2 and seq1 == seq2 --> dropped

    CSV2FastaFile(dropped, path + "/dropped.fasta")
    CSV2ClustalFile(dropped, path+"/dropped.clustal")