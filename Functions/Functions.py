import pprint as pp

description = ('Country', [
    '2011', '2012', '2013', '2014', '2015', '2016', '2017', '2018',
    '2019'
])
raw_data = [
    ('AL', [': ', ': ', ': ', ': ', ': ', ': ', ': ', '84 ', ': ']),
    ('AT', ['75 ', '79 ', '81 ', '81 ', '82 ', '85 ', '89 ', '89 ', '90 ']),
    ('BA', [': ', ': ', ': ', ': ', ': ', ': ', ': ', '69 ', '72 ']),
    ('BE', ['77 ', '78 ', '80 ', '83 ', '82 ', '85 ', '86 ', '87 ', '90 ']),
    ('BG', ['45 ', '51 ', '54 ', '57 ', '59 ', '64 ', '67 ', '72 ', '75 ']),
    ('CH', [': ', ': ', ': ', '91 ', ': ', ': ', '93 ', ': ', '96 ']),
    ('CY', ['57 ', '62 ', '65 ', '69 ', '71 ', '74 ', '79 ', '86 ', '90 ']),
    ('CZ', ['67 ', '73 ', '73 ', '78 ', '79 ', '82 ', '83 ', '86 ', '87 ']),
    ('DE', ['83 ', '85 ', '88 ', '89 ', '90 ', '92 ', '93 ', '94 ', '95 ']),
    ('DK', ['90 ', '92 ', '93 ', '93 ', '92 ', '94 ', '97 ', '93 ', '95 ']),
    ('EA', ['74 ', '76 ', '79 ', '81 ', '83 ', '85 ', '87 ', '89 ', '90 ']),
    ('EE', ['69 ', '74 ', '79 ', '83 ', '88 ', '86 ', '88 ', '90 ', '90 ']),
    ('EL', ['50 ', '54 ', '56 ', '66 ', '68 ', '69 ', '71 ', '76 ', '79 ']),
    ('ES', ['63 ', '67 ', '70 ', '74 ', '79 ', '82 ', '83 ', '86 ', '91 ']),
    ('FI', ['84 ', '87 ', '89 ', '90 ', '90 ', '92 ', '94 ', '94 ', '94 ']),
    ('FR', ['76 ', '80 ', '82 ', '83 ', '83 ', '86 ', '86 ', '89 ', '90 ']),
    ('HR', ['61 ', '66 ', '65 ', '68 ', '77 ', '77 ', '76 ', '82 ', '81 ']),
    ('HU', ['63 ', '67 ', '70 ', '73 ', '76 ', '79 ', '82 ', '83 ', '86 ']),
    ('IE', ['78 ', '81 ', '82 ', '82 ', '85 ', '87 ', '88 ', '89 ', '91 ']),
    ('IS', ['93 ', '95 ', '96 ', '96 ', ': ', ': ', '98 ', '99 ', '98 ']),
    ('IT', ['62 ', '63 ', '69 ', '73 ', '75 ', '79 ', '81 ', '84 ', '85 ']),
    ('LT', ['60 ', '60 ', '65 ', '66 ', '68 ', '72 ', '75 ', '78 ', '82 ']),
    ('LU', ['91 ', '93 ', '94 ', '96 ', '97 ', '97 ', '97 ', '93 b', '95 ']),
    ('LV', ['64 ', '69 ', '72 ', '73 ', '76 ', '77 ', '79 ', '82 ', '85 ']),
    ('ME', [': ', '55 ', ': ', ': ', ': ', ': ', '71 ', '72 ', '74 ']),
    ('MK', [': ', '58 ', '65 ', '68 ', '69 ', '75 ', '74 ', '79 ', '82 ']),
    ('MT', ['75 ', '77 ', '78 ', '80 ', '81 ', '81 ', '85 ', '84 ', '86 ']),
    ('NL', ['94 ', '94 ', '95 ', '96 ', '96 ', '97 ', '98 ', '98 ', '98 ']),
    ('NO', ['92 ', '93 ', '94 ', '93 ', '97 ', '97 ', '97 ', '96 ', '98 ']),
    ('PL', ['67 ', '70 ', '72 ', '75 ', '76 ', '80 ', '82 ', '84 ', '87 ']),
    ('PT', ['58 ', '61 ', '62 ', '65 ', '70 ', '74 ', '77 ', '79 ', '81 ']),
    ('RO', ['47 ', '54 ', '58 ', '61 ', '68 ', '72 ', '76 ', '81 ', '84 ']),
    ('RS', [': ', ': ', ': ', ': ', '64 ', ': ', '68 ', '73 ', '80 ']),
    ('SE', ['91 ', '92 ', '93 ', '90 ', '91 ', '94 ', '95 ', '93 ', '96 ']),
    ('SI', ['73 ', '74 ', '76 ', '77 ', '78 ', '78 ', '82 ', '87 ', '89 ']),
    ('SK', ['71 ', '75 ', '78 ', '78 ', '79 ', '81 ', '81 ', '81 ', '82 ']),
    ('TR', [': ', '47 ', '49 ', '60 ', '70 ', '76 ', '81 ', '84 ', '88 ']),
    ('UK', ['83 ', '87 ', '88 ', '90 ', '91 ', '93 ', '94 ', '95 ', '96 ']),
    ('XK', [': ', ': ', ': ', ': ', ': ', ': ', '89 ', '93 ', '93 ']),
]


def process_data(input_data):
    processed_data = {}

    for country in input_data:
        # as a value for each key, create a list containing dictionaries, one for each year
        coverage_per_year = []

        for index, years in enumerate(description[1]):
            # Create a dict containing year and coverage
            temp_dict = {
                'year': years,
                'coverage': country[1][index]}
            # .. and append it to the list of dictionaries
            coverage_per_year.append(temp_dict)

        # Update the dictionary with a key(country), and value(list of dictionaries)
        processed_data.update({country[0]: coverage_per_year})

    return processed_data


def group_by_year(input_data, required_year):
    list_of_countries = []
    for country in input_data:
        # print(input_data.get(country))
        for data in input_data.get(country):
            # print(data.get('year'))
            if data.get('year') == required_year:
                # print(country, data.get('coverage'))
                list_of_countries.append((country, data.get('coverage')))

    return {required_year: list_of_countries}


def group_by_country(input_data, required_country):
    coverage_by_year = []
    for country in input_data:
        # print(input_data.get(country))
        if country == required_country:
            for data in input_data.get(country):
                # print(data.get('year'))
                coverage_by_year.append((data.get('year'), data.get('coverage')))

    return {required_country: coverage_by_year}


def perform_avg(input_dataset):
    temp_sum = 0
    count = 0
    for year in input_dataset:
        if year[1] != ': ':
            temp_sum = temp_sum + int(year[1])
            count = count + 1
    return temp_sum / count


if __name__ == '__main__':
    dataset = process_data(raw_data)

    pp.pprint(dataset)

    dataset_by_year = group_by_year(dataset, '2017')

    pp.pprint(dataset_by_year)

    dataset_by_country = group_by_country(dataset, 'RO')

    pp.pprint(dataset_by_country)

    average = perform_avg(dataset_by_country['RO'])

    print(f"Average coverage for Romania is {average}")
