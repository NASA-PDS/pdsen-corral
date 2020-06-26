import argparse

from pdsen_corral.output.summary import write_build_summary
from pdsen_corral.output.root_index import update_root_index


def main():
    parser = argparse.ArgumentParser(description='Create new snapshot release')
    parser.add_argument('--output', dest='output',
                        default='output',
                        help='markdown output file name')
    parser.add_argument('--token', dest='token',
                        help='github personal access token')
    parser.add_argument('--dev', dest='dev',
                        action='store_true',
                        default=False,
                        help='if present we search for dev versions, otherwise stable versions are returned')
    args = parser.parse_args()

    output_dir = write_build_summary(root_dir=args.output, token=args.token, dev=args.dev)
    print(output_dir)




if __name__ == "__main__":
    main()

