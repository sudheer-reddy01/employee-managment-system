from unittest import TestCase
import pandas as pd


file = "./data/employee_retention_data.csv"
data = pd.read_csv(file)
df = pd.DataFrame(data)


class TestGet_categorical_variables(TestCase):
    def test_get_categorical_variables(self):
        from build import get_categorical_variables
        res = get_categorical_variables(df=df)
        self.assertTrue("dept" in res)
        self.assertTrue("join_date" in res)
        self.assertTrue("quit_date" in res)

    def test_get_numerical_variables(self):
        from build import get_numerical_variables
        res = get_numerical_variables(df=df)
        self.assertTrue("employee_id" in res)
        self.assertTrue("company_id" in res)
        self.assertTrue("seniority" in res)
        self.assertTrue("salary" in res)

    def test_get_numerical_variables_percentile(self):
        from build import get_numerical_variables_percentile
        res = get_numerical_variables_percentile(df=df)
        self.assertTrue(isinstance(res, pd.DataFrame))

    def test_get_categorical_variables_modes(self):
        from build import get_categorical_variables_modes
        res = get_categorical_variables_modes(df=df)
        self.assertTrue(isinstance(res, pd.DataFrame))

    def test_get_missing_values_count(self):
        from build import get_missing_values_count
        res = get_missing_values_count(df=df)
        self.assertTrue(isinstance(res, pd.DataFrame))
