"""
process data
data format: Year,Country,Champion,Country,Runner-up,Score in the final
Estimate: 30 minutes
Actual:   32 minutes
"""
FILENAME = "wimbledon.csv"


def main():
    records = extract_data(FILENAME)
    name_to_instances, countries = process_records(records)
    print_records(name_to_instances, countries)


def extract_data(filename):
    """extract records from file as a list of lists [name, country]"""
    with open(filename, "r", encoding="utf-8-sig") as in_file:
        records = []
        in_file.readline()  # ignore first line of file (header line)
        for line in in_file:
            records.append([line.split(",")[1], line.split(",")[2]])
    in_file.close()
    return records


def process_records(records):
    name_to_instances = {}
    countries = set()
    for country, name in records:
        countries.add(country)
        if name in name_to_instances:
            name_to_instances[name] += 1
        else:
            name_to_instances[name] = 1
    return name_to_instances, countries


def print_records(name_to_instances, countries):
    print("Wimbledon Champions:")
    for name, number_of_instances in name_to_instances.items():
        print(name, number_of_instances)
    print(f"\nThese {len(countries)} countries have won Wimbledon: ")
    print(", ".join(countries))


main()
