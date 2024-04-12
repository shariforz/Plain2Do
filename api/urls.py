from django.urls import path
from .views import *

urlpatterns = [
    path('siteconfig/<int:pk>/', SiteConfigAPIView.as_view(), name='site_config_one'),
    path('siteconfig/', SiteConfigAPIView.as_view(), name='site_config'),
    path('permitdoc/cat/<int:pk>/', PermitDocCategoryAPIView.as_view(), name='permit_doc_cat_one'),
    path('permitdoc/cat/', PermitDocCategoryAPIView.as_view(), name='permit_doc_cat'),
    path('citizenship/<int:pk>/', CitizenshipAPIView.as_view(), name='citizenship_one'),
    path('citizenship/', CitizenshipAPIView.as_view(), name='citizenship'),
    path('document-type/<int:pk>/', DocumentTypeAPIView.as_view(), name='doctype_one'),
    path('document-type/', DocumentTypeAPIView.as_view(), name='doctype_one'),
    path('gendt/doctype/<int:pk>/', Gen_DT_DocumentTypeAPIView.as_view(), name='gen_dt_doctype_one'),
    path('gendt/doctype/', Gen_DT_DocumentTypeAPIView.as_view(), name='gen_dt_doctype'),
    path('gendt-country/<int:pk>/', Gen_DT_CountryAPIView.as_view(), name='gen_dt_country_one'),
    path('gendt-country/', Gen_DT_CountryAPIView.as_view(), name='gen_dt_country'),
    path('gendt/discipline/<int:pk>/', Gen_DT_DisciplineAPIView.as_view(), name='gen_dt_discipline_one'),
    path('gendt/discipline/', Gen_DT_DisciplineAPIView.as_view(), name='gen_dt_discipline'),
    path('gendt/employee/<int:pk>/', Gen_DT_EmpLevelAPIView.as_view(), name='get_dt_employee_one'),
    path('gendt/employee/', Gen_DT_EmpLevelAPIView.as_view(), name='get_dt_employee'),
    path('gendt/emp-class/<int:pk>/', Gen_DT_EmpClassAPIView.as_view(), name='gen_dt_empclass_one'),
    path('gendt/emp-class/', Gen_DT_EmpClassAPIView.as_view(), name='gen_dt_empclass'),
    path('gendt/job-title/<int:pk>/', Gen_DT_JobTitleAPIView.as_view(), name='gen_dt_job_title_one'),
    path('gendt/job-title/', Gen_DT_JobTitleAPIView.as_view(), name='gen_dt_job_title'),
    path('gendt-currency/<int:pk>/', Gen_DT_CurrencyAPIView.as_view(), name='gen_dt-currency_one'),
    path('gendt-currency/', Gen_DT_CurrencyAPIView.as_view(), name='gen_dt-currency'),
    path('gendt/cbr-rates/<int:pk>/', Gen_DT_CBR_RatesAPIView.as_view(), name='gen_dt_cbr_rates_one'),
    path('gendt/cbr-rates/', Gen_DT_CBR_RatesAPIView.as_view(), name='gen_dt_cbr_rates'),
    path('gendt/counter-party/<int:pk>/', Gen_DT_CounterPartyAPIView.as_view(), name='gen_dt_counter_party_one'),
    path('gendt/counter-party/', Gen_DT_CounterPartyAPIView.as_view(), name='gen_dt_counter_party'),
    path('gendt/subject-rf/<int:pk>/', Gen_DT_SubjectOfRFAPIView.as_view(), name='gen_dt_subject_rf_one'),
    path('gendt/subject-rf/', Gen_DT_SubjectOfRFAPIView.as_view(), name='gen_dt_subject_rf'),
    path('gendt/project/<int:pk>/', Gen_DT_ProjectAPIView.as_view(), name='gen_dt_project_one'),
    path('gendt/project/', Gen_DT_ProjectAPIView.as_view(), name='gen_dt_project'),
    path('gendt/counter-party-type/<int:pk>/', Gen_DT_CounterPartyTypeAPIView.as_view(), name='gen_dt_counter_party_type_one'),
    path('gendt/counter-party-type/', Gen_DT_CounterPartyTypeAPIView.as_view(), name='gen_dt_counter_party_type'),
    path('gendt/contract-type/<int:pk>/', Gen_DT_ContractTypeAPIView.as_view(), name='gen_dt_contract_type_one'),
    path('gendt/counter-type/', Gen_DT_ContractTypeAPIView.as_view(), name='gen_dt_contract_type'),
    path('gendt/vat-rate/<int:pk>/', Gen_DT_VAT_RateAPIView.as_view(), name='gen_dt_vat_rate_one'),
    path('gendt/vat-rate/', Gen_DT_VAT_RateAPIView.as_view(), name='gen_dt_vat_rate'),
    path('gendt/uom/<int:pk>/', Gen_DT_UoMAPIView.as_view(), name='gen_dt_uom_one'),
    path('gendt/uom/', Gen_DT_UoMAPIView.as_view(), name='gen_dt_uom_rate'),
    path('gendt/budget-data/<int:pk>/', Gen_DT_BudgetDataAPIView.as_view(), name='gen_dt_budget_data_one'),
    path('gendt/budget-data/', Gen_DT_BudgetDataAPIView.as_view(), name='gen_dt_budget_data'),
    path('gendt/budget-data-history/<int:pk>/', Gen_DT_BudgetDataHistoryAPIView.as_view(), name='gen_dt_budget_data_history_one'),
    path('gendt/budget-data-history/', Gen_DT_BudgetDataHistoryAPIView.as_view(), name='gen_dt_budget_data_history'),
    path('gendt/expence-frequency/<int:pk>/', Gen_DT_ExpenseFrequencyAPIView.as_view(), name='gen_dt_expense_frequency_one'),
    path('gendt/expence-frequency/', Gen_DT_ExpenseFrequencyAPIView.as_view(), name='gen_dt_expense_frequency'),
    path('gendt/expense-type/<int:pk>/', Gen_DT_ExpenseTypeAPIView.as_view(), name='gen_dt_expense_type_one'),
    path('gendt/expense-type/', Gen_DT_ExpenseTypeAPIView.as_view(), name='gen_dt_expense_type'),
    path('gendt/legal-expenses/<int:pk>/', Gen_DT_LegalExpencesAPIView.as_view(), name='gen_dt_legal_expenses_one'),
    path('gendt/legal-expenses/', Gen_DT_LegalExpencesAPIView.as_view(), name='gen_dt_legal_expenses'),
    path('gendt/emp-legal-status/<int:pk>/', Gen_DT_EmpLegalStatusAPIView.as_view(), name='gen_dt_emp_legal_status_one'),
    path('gendt/emp-legal-status/', Gen_DT_EmpLegalStatusAPIView.as_view(), name='gen_dt_emp_legal_status'),
    path('gendt/emp-tax-type/<int:pk>/', Gen_DT_EmpTaxTypeAPIView.as_view(), name='gen_dt_emp_tax_type_one'),
    path('gendt/emp-tax-type/', Gen_DT_EmpTaxTypeAPIView.as_view(), name='gen_dt_emp_tax_type'),
    path('gendt/emp-tax-payer/<int:pk>/', Gen_DT_EmpTaxPayerAPIView.as_view(), name='gen_dt_emp_tax_payer_one'),
    path('gendt/emp-tax-payer/', Gen_DT_EmpTaxPayerAPIView.as_view(), name='gen_dt_emp_tax_payer'),
    path('gendt/company/<int:pk>/', Gen_DT_OurCompanyAPIView.as_view(), name='gen_dt_company_one'),
    path('gendt/company/', Gen_DT_OurCompanyAPIView.as_view(), name='gen_dt_company'),
    path('gendt/contract/<int:pk>/', Gen_DT_ContractAPIView.as_view(), name='gen_dt_contract_one'),
    path('gendt/contract/', Gen_DT_ContractAPIView.as_view(), name='gen_dt_contract'),
    path('gendt/emp-tax-calc/<int:pk>/', Gen_DT_EmpTaxCalcAPIView.as_view(), name='gen_dt_emp_tax_calc_one'),
    path('gendt/emp-tax-calc/', Gen_DT_EmpTaxCalcAPIView.as_view(), name='gen_dt_emp_tax_calc'),
    path('gendt/payment-bd-history/<int:pk>/', Gen_DT_PaymentBDHistoryAPIView.as_view(), name='gen_dt_payment_db_history_one'),
    path('gendt/payment-bd-history/', Gen_DT_PaymentBDHistoryAPIView.as_view(), name='gen_dt_payment_db_history'),
    path('gendt/progress-docs/<int:pk>/', Gen_DT_ProgressDocsAPIView.as_view(), name='gen_dt_progress_docs_one'),
    path('gendt/progress-docs/', Gen_DT_ProgressDocsAPIView.as_view(), name='gen_dt_progress_docs'),
    path('gendt/payments/<int:pk>/', Gen_DT_PaymentsAPIView.as_view(), name='gen_dt_payments_one'),
    path('gendt/payments/', Gen_DT_PaymentsAPIView.as_view(), name='gen_dt_payments'),
    path('doc/<int:pk>/', DocAPIView.as_view(), name='doc_one'),
    path('doc/', DocAPIView.as_view(), name='doc'),
    path('doc-bulk-upload/<int:pk>/', DocBulkUploadAPIView.as_view(), name='doc_bulk_upload_one'),
    path('doc-bulk-upload/', DocBulkUploadAPIView.as_view(), name='doc_bulk_upload'),
    path('employee/<int:pk>/', EmployeeAPIView.as_view(), name='employee_one'),
    path('employee/', EmployeeAPIView.as_view(), name='employee'),
    path('employee-bulk-upload/<int:pk>/', EmployeeBulkUploadAPIView.as_view(), name='employee_bulk_upload_one'),
    path('employee-bulk-upload/', EmployeeBulkUploadAPIView.as_view(), name='employee_bulk_upload'),
    path('patent-prices-details/<int:pk>/', PatentPricesDetailsAPIView.as_view(), name='patent_prices_details_one'),
    path('patent-prices-details/', Gen_DT_PatentPricesDetailsAPIView.as_view(), name='patent_prices_details'),
    path('client/<int:pk>/', Gen_DT_PatentPricesDetailsAPIView.as_view(), name='client_one'),
    path('client/', Gen_DT_ClientAPIView.as_view(), name='client'),
]