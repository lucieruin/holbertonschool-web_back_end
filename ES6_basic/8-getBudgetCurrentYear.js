function getCurrentYear() {
  const date = new Date();
  return date.getFullYear();
}

export default function getBudgetForCurrentYear(income, gdp, capita) {
  const CurrrentYear = getCurrentYear();
  const budget = {
    [`income-${CurrrentYear}`]: income,
    [`gdp-${CurrrentYear}`]: gdp,
    [`capita-${CurrrentYear}`]: capita,
  };
  return budget;
}
