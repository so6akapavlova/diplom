#script to analyse quantiles of jitter calculated with different methods


def parse_quantiles_file(filename):
    quantiles = []
    with open(filename, "r") as infile:
        for line in infile:
            quant_dict = {}
            quant_dict["sourcefile"] = line.split()[0]
            quant_dict["values"] = [float(x) for x in line.split()[1:]]
            quantiles.append(quant_dict)
    return quantiles

def check_borders(quantiles):
    borders = []
    for quant in quantiles:
        isDifferent = not all(value > 50 for value in quant["values"]) and \
                      not all(value < 50 for value in quant["values"])
        if (isDifferent) is True:
            borders.append(quant)
            print("The file {} with quantiles {}".format(quant['sourcefile'],
                                                         quant['values']))
    return borders


def get_quantiles(quantiles, filenames):
    for filename in filenames:
        for quant in quantiles:
            if quant["sourcefile"] == filename:
                print("The file {} with quantiles {}".format(quant['sourcefile'],
                                                         quant['values']))
    return 0

def main():
    quantiles = parse_quantiles_file("quantiles2.txt")
    filenames = [
        "peeramidion.irisa.fr.txt",
        "pl1.cs.montana.edu.txt",
        "pl1.rcc.uottawa.ca.txt",
        "pl2.rcc.uottawa.ca.txt",
        "planetlab-n1.wand.net.nz.txt",
        "planetlab-n2.wand.net.nz.txt",
        "planetlab3.wail.wisc.edu.txt"
    ]
    get_quantiles(quantiles, filenames)
    # check_borders(quantiles)

    return 0


if __name__ == '__main__':
    main()