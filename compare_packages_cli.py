import argparse
from compare_packages import load_packages, save_packages_to_file, compare


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('branch1',
                        type=str,
                        help='Название первой ветки (например, p10)')
    parser.add_argument('branch2',
                        type=str,
                        help='Название второй ветки (например, sisyphus)')
    parser.add_argument('--architecture',
                        choices=['aarch64', 'armh', 'i586',
                                 'noarch', 'ppc64le', 'x86_64',
                                 'x86_64-i586'],
                        type=str, default='i586',
                        help='Архитектура пакетов (по умолчанию i586)')
    args = parser.parse_args()

    packet1 = load_packages(args.branch1, args.architecture)
    packet2 = load_packages(args.branch2, args.architecture)

    unique_packages1, unique_packages2, version_release_diff = compare(packet1,
                                                                       packet2)

    save_packages_to_file(unique_packages1, 'unique_packages1.json')
    save_packages_to_file(unique_packages2, 'unique_packages2.json')
    save_packages_to_file(version_release_diff, 'version_release_diff.json')


if __name__ == "__main__":
    main()
