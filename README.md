## Survey Dud Detector

Apply methods to detect bad responses in surveys.


### Detect Straightlining

**Straightlining** involves someone answering the same item on a scale for all the questions (e.g., saying "Strongly Agree" to everything).

```Python
from survey_dud_detector import detect_straightlining

likert_cols = [c for c in mfa.columns if 'agree' in c or 'would' in c or 'favorable' in c]
straightlining = detect_straightlining(df[likert_cols])

# Examine incidence of straightlining (results are normalized to % of questions examined)
print(straightlining.value_counts())

# Drop everyone who perfectly straightlined
df = df[straightlining < 1]
```


### Multiple Low Incidence Detection

**Multiple low incidence** involves someone answering multiple questions with an unlikely answer (e.g., saying they are a Native American or that they are non-binary). Obviously unlikely answers themselves are not an issue, but multiple low incidence can indicate someone might be trolling (i.e., pretenting to be a non-binary Native American who is Very Conservative and earns over $150K).

```Python
demographics = ['gender', 'race', 'education', 'urban_rural', 'politics', 'income', 'age', 'vote2016']
# Detect low incidence - the threshold defines what rarity you want to count as "low incidence" (0.04 means anything with 4% or less occurance will be defined as "low incidence")
low_incidence_counts = detect_low_incidence(df[demographics], low_incidence_threshold=0.04)

# Examine incidence of straightlining (results are number of low incidence answers)
print(low_incidence_counts.value_counts())

# It might be good to look at the values of people with a high number of low incidence answers
# just in case this is actually legitimate.
print(df[low_incidence_counts >= 3])

# Drop everyone who gave three or more low incidence answers
df = df[low_incidence_counts < 3]
```


### Installation

`pip3 install survey_dud_detector`

