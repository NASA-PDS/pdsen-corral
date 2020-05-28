import argparse

from pdsen_corral.summary import write_build_summary


def main():
    parser = argparse.ArgumentParser(description='Create new snapshot release')
    parser.add_argument('--output', dest='output',
                        help='markdown output file name')
    parser.add_argument('--token', dest='token',
                        help='github personal access token')
    parser.add_argument('--dev', dest='dev',
                        action='store_true',
                        default=False,
                        help='if present we search for dev versions, otherwise stable versions are returned')
    args = parser.parse_args()

    output_dir = write_build_summary(output_file_name=args.output, token=args.token, dev=args.dev)

    print(output_dir)


if __name__ == "__main__":
    main()

