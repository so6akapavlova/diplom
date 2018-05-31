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


def main():
    quantiles = parse_quantiles_file("quantiles2.txt")
    for quant in quantiles:
        isDifferent = not all(value > 50 for value in quant["values"]) and \
                      not all(value < 50 for value in quant["values"])
        if (isDifferent) is True:
            print("The file {} with quantiles {}".format(quant['sourcefile'],
                                                         quant['values']))

    return 0

if __name__ == '__main__':
    main()