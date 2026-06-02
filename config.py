SOURCES = {
    "life_expectancy": "https://ourworldindata.org/grapher/life-expectancy.csv?tab=chart",
    "obesity": "https://ourworldindata.org/grapher/share-of-adults-defined-as-obese.csv?tab=chart",
    "child_mortality": "https://ourworldindata.org/grapher/child-mortality.csv?tab=chart",
    "healthcare_spending": "https://ourworldindata.org/grapher/public-health-expenditure-share-gdp-owid.csv?tab=chart",
}

METRICS = list(SOURCES.keys())

COLUMN_MAP = {
    "life_expectancy": "Life expectancy",
    "obesity": "Prevalence of obesity among adults, BMI >= 30 (crude estimate) (%) - Sex: both sexes - Age group: 18+  years of age",
    "child_mortality": "Under-five mortality rate (selected)",
    "healthcare_spending": "Public health expenditure as a share of GDP",
}
