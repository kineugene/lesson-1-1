from collections import namedtuple

if __name__ == '__main__':
    company_count = int(input("Введите количество предприятий: \n"))
    Company = namedtuple('Company', 'name, year_income')

    companies = list()

    for company_number in range(company_count):
        name = input(f"Введите название компании {company_number + 1}:\n")

        year_income = 0
        for quarter in range(4):
            income = int(input(f"Введите прибыль за {quarter + 1} квартал: \n"))
            year_income += income
        companies.append(Company(name, year_income))

    avg_income = sum(company.year_income for company in companies) / len(companies)
    print(f"Средняя прибыль за год: {avg_income}")

    higher_companies = ', '.join([company.name for company in companies if company.year_income >= avg_income])
    print(f'Компании с прибылью выше среднего: {higher_companies}')

    lower_companies = ', '.join([company.name for company in companies if company.year_income < avg_income])
    print(f'Компании с прибылью ниже среднего: {lower_companies}')
