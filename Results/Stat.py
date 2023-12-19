#!/usr/bin/env python3
import pandas as pd

df0_v = pd.read_csv('Scenario0_minSpeed.csv')
df0_c = pd.read_csv('Scenario0_totC02.csv')

df1_v = pd.read_csv('Scenario1_minSpeed.csv')
df1_c = pd.read_csv('Scenario1_totC02.csv')

df2_v = pd.read_csv('Scenario2_minSpeed.csv')
df2_c = pd.read_csv('Scenario2_totC02.csv')

mean0_v = df0_v.iloc[:,3].mean()
mean0_c = df0_c.iloc[:,3].mean()

mean1_v = df1_v.iloc[:,3].mean()
mean1_c = df1_c.iloc[:,3].mean()

mean2_v = df2_v.iloc[:,3].mean()
mean2_c = df2_c.iloc[:,3].mean()


print(f"Scenario 0 minSpeed= {round(mean0_v, 3)}")
print(f"Scenario 0 TotCo2= {round(mean0_c,3)}\n")

print(f"Scenario 1 minSpeed= {round(mean1_v,3)}")
print(f"Scenario 1 TotCo2== {round(mean1_c,3)}\n")

print(f"Scenario 2 minSpeed= {round(mean2_v,3)}")
print(f"Scenario 2 TotCo2={round(mean2_c,3)}\n")

