import argparse
from aquosRemote.aquos import AquosTV


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-i", "--ip-address", type=str,
                        help="IP address of AQUOS TV", required=True)
    args = parser.parse_args()

    # Example/Test
    aquos = AquosTV(args.ip_address, setup=True, verbose=True)
    aquos.on()
    # aquos.delay()
    print(aquos.get_info())
    # aquos.set_volume(30)
    # aquos.delay()
    # aquos.off()


if __name__ == "__main__":
    main()
