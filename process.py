import warts
from warts.traceroute import Traceroute
from os import listdir, makedirs, path


def make_pings_file(warts_dir, filename):
    directory = 'rtt_files'
    rtt_filename = filename.replace('.warts', '.txt')
    print("{} is broken".format(filename))
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
                    print('the hop address is {} and rtt is {}'.format(record.hops[-1].address, record.hops[-1].rtt))
                    print(type(record.hops[-1].rtt))
                    outfile.write(str(record.hops[-1].rtt) + '\n')
            except Exception:
                continue
    return 0


def main():
    warts_dir = 'warts_files'
    warts_files = ['peeramidion.irisa.fr.warts',
                   'pluto.cs.brown.edu.warts',
                   'planetlab2.ics.forth.gr.warts',
                   'planetlab1.cesnet.cz.warts',
                   'planetlab2.utt.fr.warts',
                   'pl1.6test.edu.cn.warts',
                   'planetlab-n1.wand.net.nz.warts',
                   'planetlab1.virtues.fi.warts',
                   'pl2.sos.info.hiroshima-cu.ac.jp.warts']
    for warts_file in listdir(warts_dir):
        make_pings_file(warts_dir, warts_file)
    return 0


if __name__ == "__main__":

    main()
