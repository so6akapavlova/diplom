import warts
from warts.traceroute import Traceroute
from os import listdir, makedirs, path
from sys import argv


# method for warts file conversion to format used by R processing script
def make_pings_file(warts_dir, filename):
    directory = 'rtt_files_last_hop'
    rtt_filename = filename.replace('.warts', '.txt')
    if not path.exists(directory):
        makedirs(directory)
    if path.exists(path.join(directory, rtt_filename)):
        print("{} exists".format(rtt_filename))
        return 1
    with open(path.join(warts_dir, filename), 'r') as fd,\
            open(path.join(directory, rtt_filename), 'w') as outfile:
        while True:
            try:
                record = warts.parse_record(fd)
                if record is None:
                    break
                if isinstance(record, Traceroute) and record.hops:
                    try:
                        used_hop
                    except:
                        used_hop = record.hops[-1].address
                        outfile.write(str(record.hops[-1].rtt) + '\n')
                    else:
                        if record.hops[-1].address == used_hop:
                            print('the hop address is {} and rtt is {}'.format(record.hops[-1].address, record.hops[-1].rtt))
                            outfile.write(str(record.hops[-1].rtt) + '\n')
                        else:
                            print("Route has been changed from {norm} to {changed}".format(norm=used_hop, changed=record.hops[-1].address))
            except Exception:
                continue
    return 0


def main():

    warts_dir = argv[1]
    # warts_files = ["ebb.colgate.edu.warts"]
    warts_files = listdir(warts_dir)
    for warts_file in warts_files:
        make_pings_file(warts_dir, warts_file)
    return 0


if __name__ == "__main__":

    main()
