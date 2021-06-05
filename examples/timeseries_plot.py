
from covid19pyclient import CovidData

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

covid = CovidData()

cases = covid.germany_timeseries(selected_type='cases')['data']
deaths = covid.germany_timeseries(selected_type='deaths')['data']
df_cases = pd.DataFrame(cases)
df_deaths = pd.DataFrame(deaths)
df_cases.set_index('date', inplace=True)
df_deaths.set_index('date', inplace=True)
df_cases.index = pd.to_datetime(df_cases.index, format="%Y-%m-%dT%H:%M:%S.%fZ")
df_deaths.index = pd.to_datetime(df_deaths.index, format="%Y-%m-%dT%H:%M:%S.%fZ")
df_cases['cases'] = df_cases.rolling(7).mean()
df_deaths['deaths'] = df_deaths.rolling(7).mean()
result = df_cases.join(df_deaths, how='outer')
colors = [(1, 0.615, 0.180, 0.85), (1, 0.180, 0.372, 0.75)]
result.plot(color=colors, linewidth=0.8)
plt.xlabel('Date')
plt.title('Corona-related Cases and Deaths', fontsize=10)
plt.fill_between(result.index, result['cases'], color=(1, 0.615, 0.180, 0.45))
plt.fill_between(result.index, result['deaths'], color=(1, 0.180, 0.372, 0.50))
plt.grid(linewidth=0.3)

# plt.rcParams['font.family'] = 'sans-serif'
# plt.rcParams['font.sans-serif'] = 'Comic Sans MS'
# plt.show()


plt.savefig("germany_timeseries.svg")
