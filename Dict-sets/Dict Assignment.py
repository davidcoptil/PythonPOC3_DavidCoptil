raw_data = [
    ('Belgium', 2017, 'M', 32.9),
    ('Belgium', 2018, 'M', 30.7),
    ('Bulgaria', 2017, 'M', 24.4),
    ('Bulgaria', 2018, 'M', 22.4),
    ('Czechia', 2017, 'M', 22.8),
    ('Czechia', 2018, 'M', 21.9),
    ('Denmark', 2017, 'M', 27.3),
    ('Denmark', 2018, 'M', 27.3),
    ('Germany', 2017, 'M', 19.8),
    ('Germany', 2018, 'M', 18.5),
    ('Estonia', 2017, 'M', 11.4),
    ('Estonia', 2018, 'M', 9.9),
    ('Ireland', 2017, 'M', 44.8),
    ('Ireland', 2018, 'M', 44.7),
    ('Greece', 2017, 'M', 47.0),
    ('Greece', 2018, 'M', 47.9),
    ('Spain', 2017, 'M', 20.2),
    ('Spain', 2018, 'M', 23.6),
    ('France', 2017, 'M', 27.1),
    ('France', 2018, 'M', 24.9),
    ('Croatia', 2017, 'M', 32.1),
    ('Croatia', 2018, 'M', 32.4),
    ('Italy', 2017, 'M', 14.5),
    ('Italy', 2018, 'M', 15.8),
    ('Cyprus', 2017, 'M', 49.7),
    ('Cyprus', 2018, 'M', 46.4),
    ('Latvia', 2017, 'M', 4.8),
    ('Latvia', 2018, 'M', 7.6),
    ('Lithuania', 2017, 'M', 9.0),
    ('Lithuania', 2018, 'M', 9.1),
    ('Luxembourg', 2017, 'M', 23.9),
    ('Luxembourg', 2018, 'M', 23.8),
    ('Hungary', 2017, 'M', 20.5),
    ('Hungary', 2018, 'M', 18.7),
    ('Malta', 2017, 'M', 29.9),
    ('Malta', 2018, 'M', 26.0),
    ('Netherlands', 2017, 'M', 24.6),
    ('Netherlands', 2018, 'M', 27.4),
    ('Austria', 2017, 'M', 34.3),
    ('Austria', 2018, 'M', 33.1),
    ('Poland', 2017, 'M', 18.3),
    ('Poland', 2018, 'M', 17.0),
    ('Portugal', 2018, 'M', 11.9),
    ('Portugal', 2018, 'M', 10.7),
    ('Romania', 2018, 'M', 31.5),
    ('Romania', 2018, 'M', 30.2),
    ('Belgium', 2017, 'F', 29.0),
    ('Belgium', 2018, 'F', 26.8),
    ('Bulgaria', 2017, 'F', 19.3),
    ('Bulgaria', 2018, 'F', 17.2),
    ('Czechia', 2017, 'F', 18.6),
    ('Czechia', 2018, 'F', 18.3),
    ('Denmark', 2017, 'F', 24.1),
    ('Denmark', 2018, 'F', 24.3),
    ('Germany', 2017, 'F', 17.3),
    ('Germany', 2018, 'F', 17.3),
    ('Estonia', 2017, 'F', 12.8),
    ('Estonia', 2018, 'F', 9.9),
    ('Ireland', 2017, 'F', 45.1),
    ('Ireland', 2018, 'F', 44.8),
    ('Greece', 2017, 'F', 42.1),
    ('Greece', 2018, 'F', 43.8),
    ('Spain', 2017, 'F', 17.3),
    ('Spain', 2018, 'F', 20.5),
    ('France', 2017, 'F', 23.1),
    ('France', 2018, 'F', 22.3),
    ('Croatia', 2017, 'F', 27.1),
    ('Croatia', 2018, 'F', 27.6),
    ('Italy', 2017, 'F', 11.4),
    ('Italy', 2018, 'F', 12.8),
    ('Cyprus', 2017, 'F', 47.3),
    ('Cyprus', 2018, 'F', 43.4),
    ('Latvia', 2017, 'F', 3.1),
    ('Latvia', 2018, 'F', 5.1),
    ('Lithuania', 2017, 'F', 6.6),
    ('Lithuania', 2018, 'F', 6.0),
    ('Luxembourg', 2017, 'F', 22.2),
    ('Luxembourg', 2018, 'F', 22.2),
    ('Hungary', 2017, 'F', 14.3),
    ('Hungary', 2018, 'F', 14.2),
    ('Malta', 2017, 'F', 25.9),
    ('Malta', 2018, 'F', 21.8),
    ('Netherlands', 2017, 'F', 20.7),
    ('Netherlands', 2018, 'F', 20.7),
    ('Austria', 2017, 'F', 32.9),
    ('Austria', 2018, 'F', 32.2),
    ('Poland', 2017, 'F', 14.6),
    ('Poland', 2018, 'F', 14.3),
    ('Portugal', 2017, 'F', 8.6),
    ('Portugal', 2018, 'F', 8.3),
    ('Romania', 2017, 'F', 24.5),
    ('Romania', 2018, 'F', 23.0),
    ('Finland', 2017, 'F', 19.0),
    ('Finland', 2018, 'F', 16.5),
    ('Sweden', 2017, 'F', 27.9),
    ('Sweden', 2018, 'F', 27.0),
    ('Iceland', 2017, 'F', 36.6),
    ('Iceland', 2018, 'F', 34.6),
    ('Norway', 2017, 'F', 28.6),
    ('Norway', 2018, 'F', 28.1),
    ('Switzerland', 2017, 'F', 33.9),
    ('Switzerland', 2018, 'F', 34.6),
    ('United Kingdom', 2017, 'F', 34.0),
    ('United Kingdom', 2018, 'F', 32.6)
]


def group_data_by_country():
    data_2017_m = {
        country: [sex, health_index]
        for country, year, sex, health_index in raw_data
        if year == 2017 and sex == 'M'}

    data_2018_m = {
        country: [sex, health_index]
        for country, year, sex, health_index in raw_data
        if year == 2018 and sex == 'M'}

    data_2017_f = {
        country: [sex, health_index]
        for country, year, sex, health_index in raw_data
        if year == 2017 and sex == 'F'}

    data_2018_f = {
        country: [sex, health_index]
        for country, year, sex, health_index in raw_data
        if year == 2018 and sex == 'F'}

    print("-----Male Health index for 2017 by country-----")
    print(data_2017_m)
    print("-----Female Health index for 2017 by country-----")
    print(data_2017_f)
    print("-----Male Health index for 2018 by country-----")
    print(data_2018_m)
    print("-----Female Health index for 2018 by country-----")
    print(data_2018_f)


def group_germany():

    germany_health_index = {
        year: [sex, health_index]
        for (country, year, sex, health_index) in raw_data
        if country == 'Germany' and sex == 'F'}

    print("-----Germany Heath index by year, for Female gender-----")
    print(germany_health_index)

def display_above_five_percent(grouped_country_and_year):
    print('-----Only higher than 5%-----')
    for country, data in grouped_country_and_year.items():
        if data[2] > 5:
            print(f'{country}, Health Index: {data[2]}')

def group_country_and_year():
    grouped_countries = {
        country+"_"+str(year): [year, sex, health_index]
        for (country, year, sex, health_index) in raw_data
        if sex == 'F'}

    print("-----Grouped by country and year, for Female Gender-----")
    print(grouped_countries)
    print()

    display_above_five_percent(grouped_countries)
    print()


def sets():
    print('--------SETS-------')
    first_set = {3, 5, 7, 1, 3, 5, 7, 3, 8, 9}
    second_set = {3, 5, 7, 3, 8, 4, 5, 6, 8, 9}
    print(first_set)
    print(second_set)
    print()

    print('Unite the sets')
    united_set = first_set.union(second_set)
    print(united_set)
    print()

    print('Intersect the sets')
    intersected_set = first_set.intersection(second_set)
    print(intersected_set)
    print()

    print('Differences in sets')
    differences = first_set.difference(second_set)
    print(differences)
    print()

    print('Symmetric difference in sets')
    symmetric_set = first_set.symmetric_difference(second_set)
    print(symmetric_set)
    print()


if __name__ == '__main__':

    group_data_by_country()
    print()

    group_germany()
    print()

    group_country_and_year()

    sets()



