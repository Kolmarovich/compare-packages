import re
import requests
import json


def load_packages(branch, architecture):
    try:
        url = f"https://rdb.altlinux.org/api/export/branch_binary_packages/{branch}?arch={architecture}"
        response = requests.get(url)
        response.raise_for_status()
        packages = response.json().get("packages")
        return packages
    except requests.RequestException as e:
        print(f"Ошибка при выполнении запроса: {e}")
        return []


def save_packages_to_file(packages, filename):
    try:
        with open(filename, 'w') as f:
            json.dump(packages, f)
    except IOError as e:
        print(f"Ошибка при записи в файл {filename}: {e}")


def compare_versions(version1, version2):
    parts1 = version1.split('.')
    parts2 = version2.split('.')

    for i in range(max(len(parts1), len(parts2))):
        part1 = parts1[i] if i < len(parts1) else ""
        part2 = parts2[i] if i < len(parts2) else ""

        if part1.isdigit() and part2.isdigit():
            part1 = int(part1)
            part2 = int(part2)
            if part1 < part2:
                return -1
            elif part1 > part2:
                return 1
        else:
            if part1 < part2:
                return -1
            elif part1 > part2:
                return 1

    return 0


def compare_release(release1, release2):

    if release1 == release2:
        return 0
    part1 = release1.split('.')
    part2 = release2.split('.')
    if part1[0].startswith('alt') and part2[0].startswith('alt'):
        match1 = re.findall(r'(\d+)', part1[0])
        match2 = re.findall(r'(\d+)', part2[0])
        for i in range(max(len(match1), len(match2))):
            value1 = part1[i] if i < len(part1) else ""
            value2 = part2[i] if i < len(part2) else ""
            if value1 < value2:
                return -1
            elif value1 > value2:
                return 1
    for i in range(1, max(len(part1), len(part2))):
        val1 = part1[i] if i < len(part1) else ""
        val2 = part2[i] if i < len(part2) else ""

        if val1.isdigit() and val2.isdigit():
            val1 = int(val1)
            val2 = int(val2)
            if val1 < val2:
                return -1
            elif val1 > val2:
                return 1
        else:
            if val1 < val2:
                return -1
            elif val1 > val2:
                return 1


def compare(packages1, packages2):
    unique_packages1 = []
    version_release_diff = []
    unique_packages2 = []

    for elem1 in packages1:
        contains = False
        for elem2 in packages2:
            if elem1['name'] == elem2['name']:
                contains = True
                compare_v = compare_versions(elem1['version'],
                                             elem2['version'])
                if compare_v < 0:
                    version_release_diff.append(elem2)
                elif compare_v == 0:
                    compare_r = compare_release(elem1['release'],
                                                elem2['release'])
                    if compare_r < 0:
                        version_release_diff.append(elem2)
                break
        if not contains:
            unique_packages1.append(elem1)

    for elem2 in packages2:
        contains = False
        for elem1 in packages1:
            if elem2['name'] == elem1['name']:
                contains = True
                break
        if not contains:
            unique_packages2.append(elem2)

    return unique_packages1, unique_packages2, version_release_diff
