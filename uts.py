# Data yang diberikan
company_detail_list = [
    {'name': 'Company 1', 'domain': 'Retail', 'country': 'United States'},
    {'name': 'Company 2', 'domain': 'Technology', 'country': 'United Kingdom'},
    {'name': 'Company 3', 'domain': 'Healthcare', 'country': 'United States'}
]

employee_detail_list = [
    {'name': 'EMP-0001', 'first_name': 'John', 'last_name': 'Doe', 'full_name': 'John Doe', 'company': 'Company 1', 'nationality': 'Australia'},
    {'name': 'EMP-0002', 'first_name': 'Tom', 'last_name': 'Smith', 'full_name': 'Tom Smith', 'company': 'Company 2', 'nationality': 'United States'},
    {'name': 'EMP-0003', 'first_name': 'Andrew', 'last_name': 'Sebastian', 'full_name': 'Andrew Sebastian', 'company': 'Company 3', 'nationality': 'United States'},
    {'name': 'EMP-0005', 'first_name': 'Ying Han', 'last_name': 'Tan', 'full_name': 'Ying Han Tan', 'company': 'Company 1', 'nationality': 'Australia'},
    {'name': 'EMP-0015', 'first_name': 'Kenneth', 'last_name': 'Ng', 'full_name': 'Kenneth Ng', 'company': 'Company 3', 'nationality': 'United States'},
    {'name': 'EMP-0018', 'first_name': 'Rubby', 'last_name': 'Lee', 'full_name': 'Rubby Lee', 'company': 'Company 2', 'nationality': 'Hong Kong'},
    {'name': 'EMP-0017', 'first_name': 'Robert', 'last_name': 'White', 'full_name': 'Robert White', 'company': 'Company 1', 'nationality': 'United Kingdom'}
]

# Task 1: Dapatkan daftar semua perusahaan dan urutkan berdasarkan nama perusahaan secara terbalik
def get_sorted_companies():
    sorted_companies = sorted(company_detail_list, key=lambda x: x['name'], reverse=True)
    return [{"name": company['name']} for company in sorted_companies]

# Task 2: Cetak nilai Domain untuk setiap perusahaan
def print_company_domains():
    for company in company_detail_list:
        print(f"{company['name']}: {company['domain']} ({company['country']})")

# Task 3: Daftar semua karyawan berdasarkan domain perusahaan
def get_employees_by_domain():
    domain_employees = {}
    for company in company_detail_list:
        domain = company['domain']
        employees = [emp['full_name'] for emp in employee_detail_list if emp['company'] == company['name']]
        domain_employees[domain] = employees
    return domain_employees

# Task 4: Karyawan beserta negara perusahaan mereka
def get_employees_with_country():
    result = []
    for emp in employee_detail_list:
        company_info = next((comp for comp in company_detail_list if comp['name'] == emp['company']), None)
        if company_info:
            result.append({
                "full_name": emp['full_name'],
                "company": emp['company'],
                "country": company_info['country']
            })
    return result

# Task 5: Perusahaan dengan jumlah karyawan berdasarkan kewarganegaraan
from collections import Counter

def get_employee_nationality_count():
    result = []
    for company in company_detail_list:
        employees = [emp['nationality'] for emp in employee_detail_list if emp['company'] == company['name']]
        nationality_count = dict(Counter(employees))
        result.append({
            "company": company['name'],
            "employee_nationality": nationality_count
        })
    return result

# Menjalankan fungsi dan menampilkan hasil untuk setiap task

# Task 1
print("Task 1:", get_sorted_companies())

# Task 2
print("\nTask 2:")
print_company_domains()

# Task 3
print("\nTask 3:", get_employees_by_domain())

# Task 4
print("\nTask 4:", get_employees_with_country())

# Task 5
print("\nTask 5:", get_employee_nationality_count())
