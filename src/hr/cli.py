from argparse import ArgumentParser

def create_parser():
    parser = ArgumentParser(description="""
    CLI utility to export users system information.
    """)

    parser.add_argument("--format", "-f", help="Export format in json or csv", default='json', choices=['json', 'csv'], type=str.lower)
    parser.add_argument("--path", "-p", help="Path to export file")

    return parser

def main():
    import sys
    from hr import export
    from hr import users as u

    args = create_parser().parse_args()
    users = u.fetch_users()

    if args.path:
        file = open(args.path, 'w', newline='')
    else:
        file = sys.stdout

    if args.format == 'json':
        export.to_json_file(file, users)
    else:
        export.to_csv_file(file, users)
