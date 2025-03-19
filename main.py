# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import pandas as pd
import openpyxl
# dp = pd.read_excel('BUSROP_Students_questionnaire_all_versions_labels_2024_04_08_19.xlsx')
# # print(dp["Gender"])
# o=0
# for i in dp['Do you agree to participate in this study?']:
#     if i=="Yes":
#         o+=1
# p=0
# for i in dp['Do you agree to participate in this study?']:
#     if i=="No":
#         p+=1
#         # dp = dp.drop(i, axis=1)
# # dp.to_excel('data.xlsx', index=False)
# # print(dp.columns)
# for index, row in dp.iterrows():
#     # Check if the specific item is found in the desired column
#     if row['Do you agree to participate in this study?'] == "No":
#         # Drop the corresponding row
#         dp.drop(index, inplace=True)
#
# print(f"{o} students chose to participate in this study")
#
# # print(dp['Do you agree to participate in this study?'])
# dp.to_csv("ACTUAL PARTICIPANTS.csv", index=False)
# # for index, row in dp.iterrows():
# #     # Check if the specific item is found in the desired column
# #     if row['Gender'] == "Male":
# #         # Drop the corresponding row
# #         dp.drop(index, inplace=True)
# # dp.to_csv("Female data.csv", index=False)
# df = pd.read_csv("ACTUAL PARTICIPANTS.csv")
# n=0
# for i in df['Gender']:
#     if i=="Male":
#         n+=1
# m=0
# for i in df['Gender']:
#     if i=="Female":
#         m+=1
# print(f"{m} Females")
# print(f"{n} Males")
# l=0
# for t in df["Do you think consuming caffeine will lead to increase in heart rate?"]:
#     if t == "Yes":
#         l+=1
# print(f"{l} students believe it will increase heart rates")
# q=0
# for t in df["Do you think consuming caffeine will lead to increase in Blood pressure?"]:
#     if t == "Yes":
#         q+=1
# print(f"{q} students believe it will lead to increase in Blood pressure")
# q=0
# for t in df["Do you think consuming caffeine causes bone weakness?"]:
#     if t == "Yes":
#         q+=1
# print(f"{q} students believe it will cause bone weakness?")
# q=0
# for t in df["Do you think caffeine is a cause for cancer?"]:
#     if t == "Yes":
#         q+=1
# print(f"{q} students believe it is a cause for cancer")
# q=0
# for t in df["Do you think consuming caffeine will lead to Diabetes?"]:
#     if t == "Yes":
#         q+=1
# print(f"{q} students believe it will lead to Diabetes")
# q=0
# for t in df["Do you think consuming caffeine increases urination?"]:
#     if t == "Yes":
#         q+=1
# print(f"{q} students believe it will lead to an increases urination")
# q=0
# for t in df["Which of the following do you think is the acceptable amount of daily consumption of caffeine?"]:
#     if t == "500mg/day":
#         q+=1
# print(f"{q} students believe 500mg/day is the acceptable amount of daily consumption of caffeine")
# q=0
# for t in df["Which of the following do you think is the acceptable amount of daily consumption of caffeine?"]:
#     if t == "400mg/day":
#         q+=1
# print(f"{q} students believe 400mg/day is the acceptable amount of daily consumption of caffeine")
# q=0
# for t in df["Which of the following do you think is the acceptable amount of daily consumption of caffeine?"]:
#     if t == "600 mg/day":
#         q+=1
# print(f"{q} students believe 600mg/day is the acceptable amount of daily consumption of caffeine")
# q=0
# for t in df["Which of the following do you think is the acceptable amount of daily consumption of caffeine?"]:
#     if t == "700mg/day":
#         q+=1
# print(f"{q} students believe 700mg/day is the acceptable amount of daily consumption of caffeine")
# q=0
# for t in df["Do you consume caffeinated drinks during the examination period?"]:
#     if t == "Yes":
#         q+=1
# print(f"{q} students consume caffeinated drinks during the examination period")
# q=0
# for t in df["What types of caffeine-containing drinks do you consume? (You can pick multiple choices)"]:
#     if "Soda" in str(t):
#         q+=1
# print(f"{q} students consume Soda")
# q=0
# for t in df["What types of caffeine-containing drinks do you consume? (You can pick multiple choices)"]:
#     if "Caffeinated tea" in str(t):
#         q+=1
# print(f"{q} students consume caffeinated tea")
# q=0
# for t in df["What types of caffeine-containing drinks do you consume? (You can pick multiple choices)"]:
#     if "Energy drinks" in str(t):
#         q+=1
# print(f"{q} students consume Energy drinks")
# q=0
# for t in df["What types of caffeine-containing drinks do you consume? (You can pick multiple choices)"]:
#     if "Coffee" in str(t):
#         q+=1
# print(f"{q} students consume Coffee")
# q=0
# for t in df["What is your preferred package?"]:
#     if t == "Bottles":
#         q+=1
# print(f"{q} students use bottles")
# q=0
# for t in df["What is your preferred package?"]:
#     if t == "Sachet":
#         q+=1
# print(f"{q} students use sachets")
# q=0
# for t in df["What is your preferred package?"]:
#     if t == "No preferences":
#         q+=1
# print(f"{q} students have no preferences")
# q=0
# for t in df["What is your preferred package?"]:
#     if t == "Cans":
#         q+=1
# print(f"{q} students use cans")
# q=0
# for t in df["How regular do you take caffeinated drinks?"]:
#     if t == "Thrice or more weekly":
#         q+=1
# print(f"{q} students take caffeinated drinks Thrice or more weekly")
# q=0
# for t in df["How regular do you take caffeinated drinks?"]:
#     if t == "Weekly":
#         q+=1
# print(f"{q} students take caffeinated drinks weekly")
# q=0
# for t in df["How regular do you take caffeinated drinks?"]:
#     if t == "Daily":
#         q+=1
# print(f"{q} students take caffeinated drinks Daily")
# print('Only 1 student mixes caffeinated drinks with alcohol')
# print('Only 1 student mixes caffeinated drinks with drugs')
# print("13 students feel nervousness from caffeinated drinks")
# print("4 students have Irritable behavior from caffeinated drinks")
# print("10 students feel mood swings from caffeinated drinks")
# print("3 students Hallucinate from caffeinated drinks")
# print("7 students feel aggression from caffeinated drinks")
# print("11 students feel Palpitation (Heart beating fast) from caffeinated drinks")
# print("24 students feel Insomnia (Poor Sleep) from caffeinated drinks")
# print("21 students feel Dizziness from caffeinated drinks")
# print("3 students feel Vomiting from caffeinated drinks")
# print("30 students feel craving for more from caffeinated drinks")
# print("18 students feel Meal skipping from caffeinated drinks")
# q=0
# for t in df["Concentrate on what to do next"]:
#     if t == "A lot":
#         q+=1
# print(f"{q} students  chose 'a lot' on Concentrate on what to do next")
# q=0
# for t in df["Concentrate on what to do next"]:
#     if t == "A medium amount":
#         q+=1
# print(f"{q} students  chose 'A medium amount' on Concentrate on what to do next")
# q=0
# for t in df["Concentrate on what to do next"]:
#     if t == "Not at all":
#         q+=1
# print(f"{q} students  chose 'Not at all' on Concentrate on what to do next")
# q=0
# for t in df["Concentrate on what to do next"]:
#     if t == "A little bit":
#         q+=1
# print(f"{q} students  chose 'A little bit' on Concentrate on what to do next")
# q=0
# for t in df["Talk to friends"]:
#     if t == "A lot":
#         q+=1
# print(f"{q} students  chose 'a lot' on Talk to friends")
# q=0
# for t in df["Talk to friends"]:
#     if t == "A medium amount":
#         q+=1
# print(f"{q} students  chose 'A medium amount' on Talk to friends")
# q=0
# for t in df["Talk to friends"]:
#     if t == "Not at all":
#         q+=1
# print(f"{q} students  chose 'Not at all' on Talk to friends")
# q=0
# for t in df["Talk to friends"]:
#     if t == "A little bit":
#         q+=1
# print(f"{q} students  chose 'A little bit' on Talk to friends")
# q=0
# for t in df["Talk to parents or relatives"]:
#     if t == "A lot":
#         q+=1
# print(f"{q} students  chose 'a lot' on Talk to parents or relatives")
# q=0
# for t in df["Talk to parents or relatives"]:
#     if t == "A medium amount":
#         q+=1
# print(f"{q} students  chose 'A medium amount' on Talk to parents or relatives")
# q=0
# for t in df["Talk to parents or relatives"]:
#     if t == "Not at all":
#         q+=1
# print(f"{q} students  chose 'Not at all' on Talk to parents or relatives")
# q=0
# for t in df["Talk to parents or relatives"]:
#     if t == "A little bit":
#         q+=1
# print(f"{q} students  chose 'A little bit' on Talk to parents or relatives")
# q=0
# for t in df["Sleeping"]:
#     if t == "A lot":
#         q+=1
# print(f"{q} students  chose 'a lot' on Sleeping")
# q=0
# for t in df["Sleeping"]:
#     if t == "A medium amount":
#         q+=1
# print(f"{q} students  chose 'A medium amount' on Sleeping")
# q=0
# for t in df["Sleeping"]:
#     if t == "Not at all":
#         q+=1
# print(f"{q} students  chose 'Not at all' on Sleeping")
# q=0
# for t in df["Sleeping"]:
#     if t == "A little bit":
#         q+=1
# print(f"{q} students  chose 'A little bit' on Sleeping")
# q=0
# for t in df["Crying"]:
#     if t == "A lot":
#         q+=1
# print(f"{q} students  chose 'a lot' on Crying")
# q=0
# for t in df["Crying"]:
#     if t == "A medium amount":
#         q+=1
# print(f"{q} students  chose 'A medium amount' on Crying")
# q=0
# for t in df["Crying"]:
#     if t == "Not at all":
#         q+=1
# print(f"{q} students  chose 'Not at all' on Crying")
# q=0
# for t in df["Crying"]:
#     if t == "A little bit":
#         q+=1
# print(f"{q} students  chose 'A little bit' on Crying")
# q=0
# for t in df["Spiritual – praying, meditation/yoga"]:
#     if t == "A lot":
#         q+=1
# print(f"{q} students  chose 'a lot' on Spiritual – praying, meditation/yoga")
# q=0
# for t in df["Spiritual – praying, meditation/yoga"]:
#     if t == "A medium amount":
#         q+=1
# print(f"{q} students  chose 'A medium amount' on Spiritual – praying, meditation/yoga")
# q=0
# for t in df["Spiritual – praying, meditation/yoga"]:
#     if t == "Not at all":
#         q+=1
# print(f"{q} students  chose 'Not at all' on Spiritual – praying, meditation/yoga")
# q=0
# for t in df["Spiritual – praying, meditation/yoga"]:
#     if t == "A little bit":
#         q+=1
# print(f"{q} students  chose 'A little bit' on Spiritual – praying, meditation/yoga")
# q=0
# for t in df["Watch television, movies"]:
#     if t == "A lot":
#         q+=1
# print(f"{q} students  chose 'a lot' on Watch television, movies")
# q=0
# for t in df["Watch television, movies"]:
#     if t == "A medium amount":
#         q+=1
# print(f"{q} students  chose 'A medium amount' on Watch television, movies")
# q=0
# for t in df["Watch television, movies"]:
#     if t == "Not at all":
#         q+=1
# print(f"{q} students  chose 'Not at all' on Watch television, movies")
# q=0
# for t in df["Watch television, movies"]:
#     if t == "A little bit":
#         q+=1
# print(f"{q} students  chose 'A little bit' on Watch television, movies")
# q=0
# for t in df["Play games/sports"]:
#     if t == "A lot":
#         q+=1
# print(f"{q} students  chose 'a lot' on Play games/sports")
# q=0
# for t in df["Play games/sports"]:
#     if t == "A medium amount":
#         q+=1
# print(f"{q} students  chose 'A medium amount' on Play games/sports")
# q=0
# for t in df["Play games/sports"]:
#     if t == "Not at all":
#         q+=1
# print(f"{q} students  chose 'Not at all' on Play games/sports")
# q=0
# for t in df["Play games/sports"]:
#     if t == "A little bit":
#         q+=1
# print(f"{q} students  chose 'A little bit' on Play games/sports")
# q=0
# for t in df["Smoking tobacco/ taking alcohol"]:
#     if t == "A lot":
#         q+=1
# print(f"{q} students  chose 'a lot' on Smoking tobacco/ taking alcohol")
# q=0
# for t in df["Smoking tobacco/ taking alcohol"]:
#     if t == "A medium amount":
#         q+=1
# print(f"{q} students  chose 'A medium amount' on Smoking tobacco/ taking alcohol")
# q=0
# for t in df["Smoking tobacco/ taking alcohol"]:
#     if t == "Not at all":
#         q+=1
# print(f"{q} students  chose 'Not at all' on Smoking tobacco/ taking alcohol")
# q=0
# for t in df["Smoking tobacco/ taking alcohol"]:
#     if t == "A little bit":
#         q+=1
# print(f"{q} students  chose 'A little bit' on Smoking tobacco/ taking alcohol")
# q=0
# for t in df["Keeping feeling to self"]:
#     if t == "A lot":
#         q+=1
# print(f"{q} students  chose 'a lot' on Keeping feeling to self")
# q=0
# for t in df["Keeping feeling to self"]:
#     if t == "A medium amount":
#         q+=1
# print(f"{q} students  chose 'A medium amount' on Keeping feeling to self")
# q=0
# for t in df["Keeping feeling to self"]:
#     if t == "Not at all":
#         q+=1
# print(f"{q} students  chose 'Not at all' on Keeping feeling to self")
# q=0
# for t in df["Keeping feeling to self"]:
#     if t == "A little bit":
#         q+=1
# print(f"{q} students  chose 'A little bit' on Keeping feeling to self")
# q=0
# for t in df["Tried to look on the bright side of life"]:
#     if t == "A lot":
#         q+=1
# print(f"{q} students  chose 'a lot' on Tried to look on the bright side of life")
# q=0
# for t in df["Tried to look on the bright side of life"]:
#     if t == "A medium amount":
#         q+=1
# print(f"{q} students  chose 'A medium amount' on Tried to look on the bright side of life")
# q=0
# for t in df["Tried to look on the bright side of life"]:
#     if t == "Not at all":
#         q+=1
# print(f"{q} students  chose 'Not at all' on Tried to look on the bright side of life")
# q=0
# for t in df["Tried to look on the bright side of life"]:
#     if t == "A little bit":
#         q+=1
# print(f"{q} students  chose 'A little bit' on Tried to look on the bright side of life")
# q=0
# for t in df["Spend more time alone"]:
#     if t == "A lot":
#         q+=1
# print(f"{q} students  chose 'a lot' on Spend more time alone")
# q=0
# for t in df["Spend more time alone"]:
#     if t == "A medium amount":
#         q+=1
# print(f"{q} students  chose 'A medium amount' on Spend more time alone")
# q=0
# for t in df["Spend more time alone"]:
#     if t == "Not at all":
#         q+=1
# print(f"{q} students  chose 'Not at all' on Spend more time alone")
# q=0
# for t in df["Spend more time alone"]:
#     if t == "A little bit":
#         q+=1
# print(f"{q} students  chose 'A little bit' on Spend more time alone")
# q=0
# for t in df["Refuse to think about it too much"]:
#     if t == "A lot":
#         q+=1
# print(f"{q} students  chose 'a lot' on Refuse to think about it too much")
# q=0
# for t in df["Refuse to think about it too much"]:
#     if t == "A medium amount":
#         q+=1
# print(f"{q} students  chose 'A medium amount' on Refuse to think about it too much")
# q=0
# for t in df["Refuse to think about it too much"]:
#     if t == "Not at all":
#         q+=1
# print(f"{q} students  chose 'Not at all' on Refuse to think about it too much")
# q=0
# for t in df["Refuse to think about it too much"]:
#     if t == "A little bit":
#         q+=1
# print(f"{q} students  chose 'A little bit' on Refuse to think about it too much")
# q=0
# for t in df["Double the efforts and work harder"]:
#     if t == "A lot":
#         q+=1
# print(f"{q} students  chose 'a lot' on Double the efforts and work harder")
# q=0
# for t in df["Double the efforts and work harder"]:
#     if t == "A medium amount":
#         q+=1
# print(f"{q} students  chose 'A medium amount' on Double the efforts and work harder")
# q=0
# for t in df["Double the efforts and work harder"]:
#     if t == "Not at all":
#         q+=1
# print(f"{q} students  chose 'Not at all' on Double the efforts and work harder")
# q=0
# for t in df["Double the efforts and work harder"]:
#     if t == "A little bit":
#         q+=1
# print(f"{q} students  chose 'A little bit' on Double the efforts and work harder")
#
# q=0
# for t in df["Convince self things aren’t as bad as it seem"]:
#     if t == "A lot":
#         q+=1
# print(f"{q} students  chose 'a lot' on Convince self things aren’t as bad as it seem")
# q=0
# for t in df["Convince self things aren’t as bad as it seem"]:
#     if t == "A medium amount":
#         q+=1
# print(f"{q} students  chose 'A medium amount' on Convince self things aren’t as bad as it seem")
# q=0
# for t in df["Convince self things aren’t as bad as it seem"]:
#     if t == "Not at all":
#         q+=1
# print(f"{q} students  chose 'Not at all' on Convince self things aren’t as bad as it seem")
# q=0
# for t in df["Convince self things aren’t as bad as it seem"]:
#     if t == "A little bit":
#         q+=1
# print(f"{q} students  chose 'A little bit' on Convince self things aren’t as bad as it seem")
# q=0
# for t in df["Avoid being with people"]:
#     if t == "A lot":
#         q+=1
# print(f"{q} students  chose 'a lot' on Avoid being with people")
# q=0
# for t in df["Avoid being with people"]:
#     if t == "A medium amount":
#         q+=1
# print(f"{q} students  chose 'A medium amount' on Avoid being with people")
# q=0
# for t in df["Avoid being with people"]:
#     if t == "Not at all":
#         q+=1
# print(f"{q} students  chose 'Not at all' on Avoid being with people")
# q=0
# for t in df["Avoid being with people"]:
#     if t == "A little bit":
#         q+=1
# print(f"{q} students  chose 'A little bit' on Avoid being with people")
# q=0
# for t in df["If you don’t take caffeinated drinks, what do you take?"]:
#     if "Water" in str(t):
#         q+=1
# print(f"{q} students students take water instead of caffeinated drinks")
# q=0
# for t in df["If you don’t take caffeinated drinks, what do you take?"]:
#     if "Energy" in str(t):
#         q+=1
#     elif "energy" in str(t):
#         q+=1
#     elif "juice" in str(t):
#         q+=1
#     elif "Juice" in str(t):
#         q+=1
#     elif "Cway" in str(t):
#         q+=1
# print(f"{q} students take energy drinks/juice instead of caffeinated drinks")
# q=0
# for t in df["If you don’t take caffeinated drinks, what do you take?"]:
#     if "Tea" in str(t):
#         q+=1
#     elif "tea" in str(t):
#         q+=1
#     elif 'Milk' in str(t):
#         q+=1
#     elif 'yoghurt' in str(t):
#         q+=1
#     elif 'fresh' in str(t):
#         q+=1
#     elif 'Fresh' in str(t):
#         q+=1
# print(f"{q} students take tea/milk/yoghurt instead of caffeinated drinks")
# q=0
# for t in df["If you don’t take caffeinated drinks, what do you take?"]:
#     if "Coke" in str(t):
#         q+=1
#     elif 'Carbonate' in str(t):
#         q+=1
#     elif 'carbonate' in str(t):
#         q+=1
# print(f"{q} students take carbonated drinks instead of caffeinated drinks")
# q=0
# for t in df["If you don’t take caffeinated drinks, what do you take?"]:
#     if "Food" in str(t):
#         q+=1
#     elif "food" in str(t):
#         q+=1
#     elif 'Snack' in str(t):
#         q+=1
#     elif 'snack' in str(t):
#         q+=1
#     elif 'Fruits' in str(t):
#         q+=1
#     elif 'fruits' in str(t):
#         q+=1
#     elif 'Suya' in str(t):
#         q+=1
# print(f"{q} students eat solid food instead of caffeinated drinks")
# q=0
# for t in df["If you don’t take caffeinated drinks, what do you take?"]:
#     if "gum" in str(t):
#         q += 1
# print(f"{q} students chew gum instead of caffeinated drinks")
# q=0
# for t in df["During the past month, what time have you usually gone to bed at night?"]:
#     if "9" in str(t):
#         q+=1
#     elif "8" in str(t):
#         q+=1
# print(f"{q} students go to bed before 10")
# q=0
# for t in df["During the past month, what time have you usually gone to bed at night?"]:
#     if "10" in str(t):
#         q+=1
# print(f"{q} students go to bed after 10")
# q=0
# for t in df["During the past month, what time have you usually gone to bed at night?"]:
#     if "11" in str(t):
#         q+=1
# print(f"{q} students go to bed after 11")
# q=0
# for t in df["During the past month, what time have you usually gone to bed at night?"]:
#     if "12" in str(t):
#         q+=1
# print(f"{q} students go to bed after 12")
# dg= pd.read_csv('output.csv')
# for i in dg.columns:
#     q = 0
#     for t in dg[i]:
#         if t == 'Not during the past month':
#             q+=1
#     if 'Unnamed' in str(i):
#         pass
#     else:
#         print(f"{q} students {i} Not during the past month")
# for i in dg.columns:
#     q = 0
#     for t in dg[i]:
#         if t == 'Less than once a week':
#             q+=1
#     if 'Unnamed' in str(i):
#         pass
#     else:
#         print(f"{q} students {i} Less than once a week")
# for i in dg.columns:
#     q = 0
#     for t in dg[i]:
#         if t == 'Three or more times a week':
#             q+=1
#     if 'Unnamed' in str(i):
#         pass
#     else:
#         print(f"{q} students {i} Three or more times a week")
# for i in dg.columns:
#     q = 0
#     for t in dg[i]:
#         if t == 'Once or twice a week':
#             q+=1
#     if 'Unnamed' in str(i):
#         pass
#     else:
#         print(f"{q} students {i} Once or twice a week")
# q=0
# for t in dg['How often during the past month have you had trouble sleeping because of other reasons?']:
#     if t == 'Three or more times a week':
#             q+=1
#     elif 'Unnamed' in str(t):
#         pass
# print(f"{q} students How often during the past month have you had trouble sleeping because of other reasons?Three or more times a week")
# q=0
# for t in dg['How often during the past month have you had trouble sleeping because of other reasons?']:
#     if t == 'Not during the past month':
#             q+=1
#     elif 'Unnamed' in str(t):
#         pass
# print(f"{q} students How often during the past month have you had trouble sleeping because of other reasons?Not during the past month")
# q=0
# for t in dg['How often during the past month have you had trouble sleeping because of other reasons?']:
#     if t == 'Less than once a week':
#             q+=1
#     elif 'Unnamed' in str(t):
#         pass
# print(f"{q} students How often during the past month have you had trouble sleeping because of other reasons?Less than once a week")
# q=0
# for t in dg['During the past month, how often have you had trouble staying awake while driving, eating meals, or engaging in social activity?']:
#     if t == 'Three or more times a week':
#             q+=1
#     elif 'Unnamed' in str(t):
#         pass
# print(f"{q} students During the past month, how often have you had trouble staying awake while driving, eating meals, or engaging in social activity?Three or more times a week")
# q=0
# for t in dg['During the past month, how often have you had trouble staying awake while driving, eating meals, or engaging in social activity?']:
#     if t == 'Not during the past month':
#             q+=1
#     elif 'Unnamed' in str(t):
#         pass
# print(f"{q} students During the past month, how often have you had trouble staying awake while driving, eating meals, or engaging in social activity?Not during the past month")
# q=0
# for t in dg['During the past month, how often have you had trouble staying awake while driving, eating meals, or engaging in social activity?']:
#     if t == 'Less than once a week':
#             q+=1
#     elif 'Unnamed' in str(t):
#         pass
# print(f"{q} students During the past month, how often have you had trouble staying awake while driving, eating meals, or engaging in social activity?Less than once a week")
# q=0
# for t in df["During the past month, how much of a problem has it been for you to keep up enough enthusiasm to get things done?"]:
#     if t == "No problem at all":
#         q+=1
# print(f"{q} students  chose 'No problem at all' on During the past month, how much of a problem has it been for you to keep up enough enthusiasm to get things done?")
# q=0
# for t in df["During the past month, how much of a problem has it been for you to keep up enough enthusiasm to get things done?"]:
#     if t == "Only a very slight problem":
#         q+=1
# print(f"{q} students  chose 'Only a very slight problem' on During the past month, how much of a problem has it been for you to keep up enough enthusiasm to get things done?")
# q=0
# for t in df["During the past month, how much of a problem has it been for you to keep up enough enthusiasm to get things done?"]:
#     if t == "Somewhat of a problem":
#         q+=1
# print(f"{q} students  chose 'Somewhat of a problem' on During the past month, how much of a problem has it been for you to keep up enough enthusiasm to get things done?")
# q=0
# for t in df["During the past month, how much of a problem has it been for you to keep up enough enthusiasm to get things done?"]:
#     if t == "A very big problem":
#         q+=1
# print(f"{q} students  chose 'A very big problem' on During the past month, how much of a problem has it been for you to keep up enough enthusiasm to get things done?")
#
# # for index, row in df.iterrows():
# #     # Check if the specific item is found in the desired column
# #     if row['Gender'] == "Female":
# #         # Drop the corresponding row
# #         df.drop(index, inplace=True)
# # df.to_csv("Male data.csv", index=False)
# # See PyCharm help at https://www.jetbrains.com/help/pycharm/
# import re
#
# # Provided text containing numbers
# text = """
# 114 students believe it will increase heart rates
# 114 students believe it will lead to increase in Blood pressure
# 54 students believe it will cause bone weakness?
# 38 students believe it is a cause for cancer
# 69 students believe it will lead to Diabetes
# 110 students believe it will lead to an increases urination
# 29 students believe 500mg/day is the acceptable amount of daily consumption of caffeine
# 121 students believe 400mg/day is the acceptable amount of daily consumption of caffeine
# 3 students believe 600mg/day is the acceptable amount of daily consumption of caffeine
# 1 students believe 700mg/day is the acceptable amount of daily consumption of caffeine
# 51 students consume caffeinated drinks during the examination period
# 27 students consume Soda
# 4 students consume caffeinated tea
# 32 students consume Energy drinks
# 21 students consume Coffee
# 27 students use bottles
# 8 students use sachets
# 9 students have no preferences
# 7 students use cans
# 6 students take caffeinated drinks Thrice or more weekly
# 38 students take caffeinated drinks weekly
# 7 students take caffeinated drinks Daily
# Only 1 student mixes caffeinated drinks with alcohol
# Only 1 student mixes caffeinated drinks with drugs
# 13 students feel nervousness from caffeinated drinks
# 4 students have Irritable behavior from caffeinated drinks
# 10 students feel mood swings from caffeinated drinks
# 3 students Hallucinate from caffeinated drinks
# 7 students feel aggression from caffeinated drinks
# 11 students feel Palpitation (Heart beating fast) from caffeinated drinks
# 24 students feel Insomnia (Poor Sleep) from caffeinated drinks
# 21 students feel Dizziness from caffeinated drinks
# 3 students feel Vomiting from caffeinated drinks
# 30 students feel craving for more from caffeinated drinks
# 18 students feel Meal skipping from caffeinated drinks
# 45 students  chose 'a lot' on Concentrate on what to do next
# 40 students  chose 'A medium amount' on Concentrate on what to do next
# 26 students  chose 'Not at all' on Concentrate on what to do next
# 43 students  chose 'A little bit' on Concentrate on what to do next
# 21 students  chose 'a lot' on Talk to friends
# 54 students  chose 'A medium amount' on Talk to friends
# 27 students  chose 'Not at all' on Talk to friends
# 52 students  chose 'A little bit' on Talk to friends
# 24 students  chose 'a lot' on Talk to parents or relatives
# 33 students  chose 'A medium amount' on Talk to parents or relatives
# 50 students  chose 'Not at all' on Talk to parents or relatives
# 47 students  chose 'A little bit' on Talk to parents or relatives
# 29 students  chose 'a lot' on Sleeping
# 60 students  chose 'A medium amount' on Sleeping
# 20 students  chose 'Not at all' on Sleeping
# 45 students  chose 'A little bit' on Sleeping
# 7 students  chose 'a lot' on Crying
# 9 students  chose 'A medium amount' on Crying
# 117 students  chose 'Not at all' on Crying
# 21 students  chose 'A little bit' on Crying
# 43 students  chose 'a lot' on Spiritual – praying, meditation/yoga
# 38 students  chose 'A medium amount' on Spiritual – praying, meditation/yoga
# 38 students  chose 'Not at all' on Spiritual – praying, meditation/yoga
# 35 students  chose 'A little bit' on Spiritual – praying, meditation/yoga
# 18 students  chose 'a lot' on Watch television, movies
# 26 students  chose 'A medium amount' on Watch television, movies
# 41 students  chose 'Not at all' on Watch television, movies
# 69 students  chose 'A little bit' on Watch television, movies
# 9 students  chose 'a lot' on Play games/sports
# 30 students  chose 'A medium amount' on Play games/sports
# 56 students  chose 'Not at all' on Play games/sports
# 59 students  chose 'A little bit' on Play games/sports
# 1 students  chose 'a lot' on Smoking tobacco/ taking alcohol
# 3 students  chose 'A medium amount' on Smoking tobacco/ taking alcohol
# 146 students  chose 'Not at all' on Smoking tobacco/ taking alcohol
# 4 students  chose 'A little bit' on Smoking tobacco/ taking alcohol
# 32 students  chose 'a lot' on Keeping feeling to self
# 27 students  chose 'A medium amount' on Keeping feeling to self
# 43 students  chose 'Not at all' on Keeping feeling to self
# 52 students  chose 'A little bit' on Keeping feeling to self
# 64 students  chose 'a lot' on Tried to look on the bright side of life
# 41 students  chose 'A medium amount' on Tried to look on the bright side of life
# 23 students  chose 'Not at all' on Tried to look on the bright side of life
# 26 students  chose 'A little bit' on Tried to look on the bright side of life
# 41 students  chose 'a lot' on Spend more time alone
# 40 students  chose 'A medium amount' on Spend more time alone
# 25 students  chose 'Not at all' on Spend more time alone
# 48 students  chose 'A little bit' on Spend more time alone
# 36 students  chose 'a lot' on Refuse to think about it too much
# 43 students  chose 'A medium amount' on Refuse to think about it too much
# 24 students  chose 'Not at all' on Refuse to think about it too much
# 51 students  chose 'A little bit' on Refuse to think about it too much
# 61 students  chose 'a lot' on Double the efforts and work harder
# 50 students  chose 'A medium amount' on Double the efforts and work harder
# 10 students  chose 'Not at all' on Double the efforts and work harder
# 33 students  chose 'A little bit' on Double the efforts and work harder
# 39 students  chose 'a lot' on Convince self things aren’t as bad as it seem
# 45 students  chose 'A medium amount' on Convince self things aren’t as bad as it seem
# 22 students  chose 'Not at all' on Convince self things aren’t as bad as it seem
# 48 students  chose 'A little bit' on Convince self things aren’t as bad as it seem
# 15 students  chose 'a lot' on Avoid being with people
# 21 students  chose 'A medium amount' on Avoid being with people
# 65 students  chose 'Not at all' on Avoid being with people
# 53 students  chose 'A little bit' on Avoid being with people
# 57 students students take water instead of caffeinated drinks
# 8 students take energy drinks/juice instead of caffeinated drinks
# 13 students take tea/milk/yoghurt instead of caffeinated drinks
# 11 students take carbonated drinks instead of caffeinated drinks
# 10 students eat solid food instead of caffeinated drinks
# 1 students chew gum instead of caffeinated drinks
# 13 students go to bed before 10
# 37 students go to bed after 10
# 38 students go to bed after 11
# 38 students go to bed after 12
# 75 students Cannot get sleep within 30 minutes Not during the past month
# 37 students Wake up in the middle of the night or early morning Not during the past month
# 32 students Have to get up to use the bathroom Not during the past month
# 126 students Cannot breathe comfortably Not during the past month
# 124 students Cough or snore loudly Not during the past month
# 98 students Feel too cold Not during the past month
# 51 students Feel too hot Not during the past month
# 109 students Had bad dreams Not during the past month
# 85 students Have pain Not during the past month
# 118 students How often during the past month have you had trouble sleeping because of other reasons? Not during the past month
# 97 students During the past month, how often have you had trouble staying awake while driving, eating meals, or engaging in social activity? Not during the past month
# 31 students Cannot get sleep within 30 minutes Less than once a week
# 26 students Wake up in the middle of the night or early morning Less than once a week
# 23 students Have to get up to use the bathroom Less than once a week
# 13 students Cannot breathe comfortably Less than once a week
# 12 students Cough or snore loudly Less than once a week
# 35 students Feel too cold Less than once a week
# 22 students Feel too hot Less than once a week
# 22 students Had bad dreams Less than once a week
# 36 students Have pain Less than once a week
# 21 students How often during the past month have you had trouble sleeping because of other reasons? Less than once a week
# 26 students During the past month, how often have you had trouble staying awake while driving, eating meals, or engaging in social activity? Less than once a week
# 20 students Cannot get sleep within 30 minutes Three or more times a week
# 56 students Wake up in the middle of the night or early morning Three or more times a week
# 55 students Have to get up to use the bathroom Three or more times a week
# 4 students Cannot breathe comfortably Three or more times a week
# 7 students Cough or snore loudly Three or more times a week
# 8 students Feel too cold Three or more times a week
# 53 students Feel too hot Three or more times a week
# 4 students Had bad dreams Three or more times a week
# 12 students Have pain Three or more times a week
# 7 students How often during the past month have you had trouble sleeping because of other reasons? Three or more times a week
# 7 students During the past month, how often have you had trouble staying awake while driving, eating meals, or engaging in social activity? Three or more times a week
# 28 students Cannot get sleep within 30 minutes Once or twice a week
# 35 students Wake up in the middle of the night or early morning Once or twice a week
# 44 students Have to get up to use the bathroom Once or twice a week
# 11 students Cannot breathe comfortably Once or twice a week
# 11 students Cough or snore loudly Once or twice a week
# 13 students Feel too cold Once or twice a week
# 28 students Feel too hot Once or twice a week
# 19 students Had bad dreams Once or twice a week
# 21 students Have pain Once or twice a week
# 8 students How often during the past month have you had trouble sleeping because of other reasons? Once or twice a week
# 24 students During the past month, how often have you had trouble staying awake while driving, eating meals, or engaging in social activity? Once or twice a week
# 7 students How often during the past month have you had trouble sleeping because of other reasons?Three or more times a week
# 118 students How often during the past month have you had trouble sleeping because of other reasons?Not during the past month
# 21 students How often during the past month have you had trouble sleeping because of other reasons?Less than once a week
# 7 students During the past month, how often have you had trouble staying awake while driving, eating meals, or engaging in social activity?Three or more times a week
# 97 students During the past month, how often have you had trouble staying awake while driving, eating meals, or engaging in social activity?Not during the past month
# 26 students During the past month, how often have you had trouble staying awake while driving, eating meals, or engaging in social activity?Less than once a week
# 62 students  chose 'No problem at all' on During the past month, how much of a problem has it been for you to keep up enough enthusiasm to get things done?
# 57 students  chose 'Only a very slight problem' on During the past month, how much of a problem has it been for you to keep up enough enthusiasm to get things done?
# 25 students  chose 'Somewhat of a problem' on During the past month, how much of a problem has it been for you to keep up enough enthusiasm to get things done?
# 10 students  chose 'A very big problem' on During the past month, how much of a problem has it been for you to keep up enough enthusiasm to get things done? code extract all the numbers here and put them in a list one by one
# """
#
# # Extract all the numbers using regular expressions
# numbers = re.findall(r'\d+', text)
#
# # Convert the extracted numbers from strings to integers
# numbers = [int(num) for num in numbers]
#
# print(numbers)
# pattern = r'([a-zA-Z\s\-\d\(\)/]+)'
#
# # Find all texts in the text
# texts = re.findall(pattern, text)
#
# # Print the texts
# print(texts)
#
# dataa =[
#     'students believe it will increase heart rates',
#     'students believe it will lead to increase in Blood pressure',
#     'students believe it will cause bone weakness?',
#     'students believe it is a cause for cancer',
#     'students believe it will lead to Diabetes',
#     'students believe it will lead to an increases urination',
#     'students believe mg/day is the acceptable amount of daily consumption of caffeine',
#     'students believe mg/day is the acceptable amount of daily consumption of caffeine',
#     'students believe mg/day is the acceptable amount of daily consumption of caffeine',
#     'students believe mg/day is the acceptable amount of daily consumption of caffeine',
#     'students consume caffeinated drinks during the examination period',
#     'students consume Soda',
#     'students consume caffeinated tea',
#     'students consume Energy drinks',
#     'students consume Coffee',
#     'students use bottles',
#     'students use sachets',
#     'students have no preferences',
#     'students use cans',
#     'students take caffeinated drinks Thrice or more weekly',
#     'students take caffeinated drinks weekly',
#     'students take caffeinated drinks Daily',
#     'Only student mixes caffeinated drinks with alcohol',
#     'Only student mixes caffeinated drinks with drugs',
#     'students feel nervousness from caffeinated drinks',
#     'students have Irritable behavior from caffeinated drinks',
#     'students feel mood swings from caffeinated drinks',
#     'students Hallucinate from caffeinated drinks',
#     'students feel aggression from caffeinated drinks',
#     'students feel Palpitation (Heart beating fast) from caffeinated drinks',
#     'students feel Insomnia (Poor Sleep) from caffeinated drinks',
#     'students feel Dizziness from caffeinated drinks',
#     'students feel Vomiting from caffeinated drinks',
#     'students feel craving for more from caffeinated drinks',
#     'students feel Meal skipping from caffeinated drinks',
#     'students chose a lot on Concentrate on what to do next',
#     'students chose A medium amount on Concentrate on what to do next',
#     'students chose Not at all on Concentrate on what to do next',
#     'students chose A little bit on Concentrate on what to do next',
#     'students chose a lot on Talk to friends',
#     'students chose A medium amount on Talk to friends',
#     'students chose Not at all on Talk to friends',
#     'students chose A little bit on Talk to friends',
#     'students chose a lot on Talk to parents or relatives',
#     'students chose A medium amount on Talk to parents or relatives',
#     'students chose Not at all on Talk to parents or relatives',
#     'students chose A little bit on Talk to parents or relatives',
#     'students chose a lot on Sleeping',
#     'students chose A medium amount on Sleeping',
#     'students chose Not at all on Sleeping',
#     'students chose A little bit on Sleeping',
#     'students chose a lot on Crying',
#     'students chose A medium amount on Crying',
#     'students chose Not at all on Crying',
#     'students chose A little bit on Crying',
#     'students chose a lot on Spiritual – praying, meditation/yoga',
#     'students chose A medium amount on Spiritual – praying, meditation/yoga',
#     'students chose Not at all on Spiritual – praying, meditation/yoga',
#     'students chose A little bit on Spiritual – praying, meditation/yoga',
#     'students chose a lot on Watch television, movies',
#     'students chose A medium amount on Watch television, movies',
#     'students chose Not at all on Watch television, movies',
#     'students chose A little bit on Watch television, movies',
#     'students chose a lot on Play games/sports',
#     'students chose A medium amount on Play games/sports',
#     'students chose Not at all on Play games/sports',
#     'students chose A little bit on Play games/sports',
#     'student chose a lot on Smoking tobacco/ taking alcohol',
#     'students chose A medium amount on Smoking tobacco/ taking alcohol',
#     'students chose Not at all on Smoking tobacco/ taking alcohol',
#     'students chose A little bit on Smoking tobacco/ taking alcohol',
#     'students chose a lot on Keeping feeling to self',
#     'students chose A medium amount on Keeping feeling to self',
#     'students chose Not at all on Keeping feeling to self',
#     'students chose A little bit on Keeping feeling to self',
#     'students chose a lot on Tried to look on the bright side of life',
#     'students chose A medium amount on Tried to look on the bright side of life',
#     'students chose Not at all on Tried to look on the bright side of life',
#     'students chose A little bit on Tried to look on the bright side of life',
#     'students chose a lot on Spend more time alone',
#     'students chose A medium amount on Spend more time alone',
#     'students chose Not at all on Spend more time alone',
#     'students chose A little bit on Spend more time alone',
#     'students chose a lot on Refuse to think about it too much',
#     'students chose A medium amount on Refuse to think about it too much',
#     'students chose Not at all on Refuse to think about it too much',
#     'students chose A little bit on Refuse to think about it too much',
#     'students chose a lot on Double the efforts and work harder',
#     'students chose A medium amount on Double the efforts and work harder',
#     'students chose Not at all on Double the efforts and work harder',
#     'students chose A little bit on Double the efforts and work harder',
#     'students chose a lot on Convince self things aren’t as bad as it seem',
#     'students chose A medium amount on Convince self things aren’t as bad as it seem',
#     'students chose Not at all on Convince self things aren’t as bad as it seem',
#     'students chose A little bit on Convince self things aren’t as bad as it seem',
#     'student chose a lot on Avoid being with people',
#     'students chose A medium amount on Avoid being with people',
#     'students chose Not at all on Avoid being with people',
#     'students chose A little bit on Avoid being with people',
#     'students students take water instead of caffeinated drinks',
#     'students take energy drinks/juice instead of caffeinated drinks',
#     'students take tea/milk/yoghurt instead of caffeinated drinks',
#     'students take carbonated drinks instead of caffeinated drinks',
#     'students eat solid food instead of caffeinated drinks',
#     'student chew gum instead of caffeinated drinks',
#     'students go to bed before ',
#     'students go to bed after ',
#     'students go to bed after ',
#     'students go to bed after ',
#     'students Cannot get sleep within  minutes Not during the past month',
#     'students Wake up in the middle of the night or early morning Not during the past month',
#     'students Have to get up to use the bathroom Not during the past month',
#     'students Cannot breathe comfortably Not during the past month',
#     'students Cough or snore loudly Not during the past month',
#     'students Feel too cold Not during the past month',
#     'students Feel too hot Not during the past month',
#     'students Had bad dreams Not during the past month',
#     'students Have pain Not during the past month',
#     'students How often during the past month have you had trouble sleeping because of other reasons? Not during the past month',
#     'students During the past month, how often have you had trouble staying awake while driving, eating meals, or engaging in social activity? Not during the past month',
#     'students Cannot get sleep within  minutes Less than once a week',
#     'students Wake up in the middle of the night or early morning Less than once a week',
#     'students Have to get up to use the bathroom Less than once a week',
#     'students Cannot breathe comfortably Less than once a week',
#     'students Cough or snore loudly Less than once a week',
#     'students Feel too cold Less than once a week',
#     'students Feel too hot Less than once a week',
#     'students Had bad dreams Less than once a week',
#     'students Have pain Less than once a week',
#     'students How often during the past month have you had trouble sleeping because of other reasons? Less than once a week',
#     'students During the past month, how often have you had trouble staying awake while driving, eating meals, or engaging in social activity? Less than once a week',
#     'students Cannot get sleep within  minutes Three or more times a week',
#     'students Wake up in the middle of the night or early morning Three or more times a week',
#     'students Have to get up to use the bathroom Three or more times a week',
#     'students Cannot breathe comfortably Three or more times a week',
#     'students Cough or snore loudly Three or more times a week',
#     'students Feel too cold Three or more times a week',
#     'students Feel too hot Three or more times a week',
#     'students Had bad dreams Three or more times a week',
#     'students Have pain Three or more times a week',
#     'students How often during the past month have you had trouble sleeping because of other reasons? Three or more times a week',
#     'students During the past month, how often have you had trouble staying awake while driving, eating meals, or engaging in social activity? Three or more times a week',
#     'students Cannot get sleep within  minutes Once or twice a week',
#     'students Wake up in the middle of the night or early morning Once or twice a week',
#     'students Have to get up to use the bathroom Once or twice a week',
#     'students Cannot breathe comfortably Once or twice a week',
#     'students Cough or snore loudly Once or twice a week',
#     'students Feel too cold Once or twice a week',
#     'students Feel too hot Once or twice a week',
#     'students Had bad dreams Once or twice a week',
#     'students Have pain Once or twice a week',
#     'students How often during the past month have you had trouble sleeping because of other reasons? Once or twice a week',
#     'students During the past month, how often have you had trouble staying awake while driving, eating meals, or engaging in social activity? Once or twice a week',
#     'students How often during the past month have you had trouble sleeping because of other reasons?Three or more times a week',
#     'students How often during the past month have you had trouble sleeping because of other reasons?Not during the past month',
#     'students How often during the past month have you had trouble sleeping because of other reasons?Less than once a week',
#     'students During the past month, how often have you had trouble staying awake while driving, eating meals, or engaging in social activity?Three or more times a week',
#     'students During the past month, how often have you had trouble staying awake while driving, eating meals, or engaging in social activity?Not during the past month',
#     'students During the past month, how often have you had trouble staying awake while driving, eating meals, or engaging in social activity?Less than once a week',
#     'students  chose No problem at all on During the past month, how much of a problem has it been for you to keep up enough enthusiasm to get things done?',
#     'students  chose Only a very slight problem on During the past month, how much of a problem has it been for you to keep up enough enthusiasm to get things done?',
#     'students  chose Somewhat of a problem on During the past month, how much of a problem has it been for you to keep up enough enthusiasm to get things done?',
#     'students  chose A very big problem on During the past month, how much of a problem has it been for you to keep up enough enthusiasm to get things done?'
# ]
# # dff = pd.DataFrame(dataa)
# #
# # # Write the DataFrame to an Excel file
# # dff.to_excel("survey_data.xlsx", index=False)
#
# print(len(numbers))
# print(len(dataa))
# import pandas as pd
#
# # Define the data
# import pandas as pd
#
# # Define the data
# data = {
#     "Category": [
#         "Increase heart rates",
#         "Increase in Blood pressure",
#         "Cause bone weakness?",
#         "Cause for cancer",
#         "Lead to Diabetes",
#         "Lead to an increase in urination",
#         "Acceptable amount of daily consumption of caffeine",
#         "Acceptable amount of daily consumption of caffeine",
#         "Acceptable amount of daily consumption of caffeine",
#         "Acceptable amount of daily consumption of caffeine",
#         "Caffeinated drinks during the examination period",
#         "Consume Soda",
#         "Consume caffeinated tea",
#         "Consume Energy drinks",
#         "Consume Coffee",
#         "Use bottles",
#         "Use sachets",
#         "No preferences",
#         "Use cans",
#         "Take caffeinated drinks Thrice or more weekly",
#         "Take caffeinated drinks weekly",
#         "Take caffeinated drinks Daily",
#         "Mixes caffeinated drinks with alcohol",
#         "Mixes caffeinated drinks with drugs",
#         "Feel nervousness from caffeinated drinks",
#         "Have Irritable behavior from caffeinated drinks",
#         "Feel mood swings from caffeinated drinks",
#         "Hallucinate from caffeinated drinks",
#         "Feel aggression from caffeinated drinks",
#         "Feel Palpitation (Heart beating fast) from caffeinated drinks",
#         "Feel Insomnia (Poor Sleep) from caffeinated drinks",
#         "Feel Dizziness from caffeinated drinks",
#         "Feel Vomiting from caffeinated drinks",
#         "Feel craving for more from caffeinated drinks",
#         "Feel Meal skipping from caffeinated drinks",
#         "Concentrate on what to do next: 'a lot'",
#         "Concentrate on what to do next: 'A medium amount'",
#         "Concentrate on what to do next: 'Not at all'",
#         "Concentrate on what to do next: 'A little bit'",
#         "Talk to friends: 'a lot'",
#         "Talk to friends: 'A medium amount'",
#         "Talk to friends: 'Not at all'",
#         "Talk to friends: 'A little bit'",
#         "Talk to parents or relatives: 'a lot'",
#         "Talk to parents or relatives: 'A medium amount'",
#         "Talk to parents or relatives: 'Not at all'",
#         "Talk to parents or relatives: 'A little bit'",
#         "Sleeping: 'a lot'",
#         "Sleeping: 'A medium amount'",
#         "Sleeping: 'Not at all'",
#         "Sleeping: 'A little bit'",
#         "Crying: 'a lot'",
#         "Crying: 'A medium amount'",
#         "Crying: 'Not at all'",
#         "Crying: 'A little bit'",
#         "Spiritual – praying, meditation/yoga: 'a lot'",
#         "Spiritual – praying, meditation/yoga: 'A medium amount'",
#         "Spiritual – praying, meditation/yoga: 'Not at all'",
#         "Spiritual – praying, meditation/yoga: 'A little bit'",
#         "Watch television, movies: 'a lot'",
#         "Watch television, movies: 'A medium amount'",
#         "Watch television, movies: 'Not at all'",
#         "Watch television, movies: 'A little bit'",
#         "Play games/sports: 'a lot'",
#         "Play games/sports: 'A medium amount'",
#         "Play games/sports: 'Not at all'",
#         "Play games/sports: 'A little bit'",
#         "Smoking tobacco/ taking alcohol: 'a lot'",
#         "Smoking tobacco/ taking alcohol: 'A medium amount'",
#         "Smoking tobacco/ taking alcohol: 'Not at all'",
#         "Smoking tobacco/ taking alcohol: 'A little bit'",
#         "Keeping feeling to self: 'a lot'",
#         "Keeping feeling to self: 'A medium amount'",
#         "Keeping feeling to self: 'Not at all'",
#         "Keeping feeling to self: 'A little bit'",
#         "Tried to look on the bright side of life: 'a lot'",
#         "Tried to look on the bright side of life: 'A medium amount'",
#         "Tried to look on the bright side of life: 'Not at all'",
#         "Tried to look on the bright side of life: 'A little bit'",
#         "Spend more time alone: 'a lot'",
#         "Spend more time alone: 'A medium amount'",
#         "Spend more time alone: 'Not at all'",
#         "Spend more time alone: 'A little bit'",
#         "Refuse to think about it too much: 'a lot'",
#         "Refuse to think about it too much: 'A medium amount'",
#         "Refuse to think about it too much: 'Not at all'",
#         "Refuse to think about it too much: 'A little bit'",
#         "Double the efforts and work harder: 'a lot'",
#         "Double the efforts and work harder: 'A medium amount'",
#         "Double the efforts and work harder: 'Not at all'",
#         "Double the efforts and work harder: 'A little bit'",
#         "Convince self things aren’t as bad as it seem: 'a lot'",
#         "Convince self things aren’t as bad as it seem: 'A medium amount'",
#         "Convince self things aren’t as bad as it seem: 'Not at all'",
#         "Convince self things aren’t as bad as it seem: 'A little bit'",
#         "Avoid being with people: 'a lot'",
#         "Avoid being with people: 'A medium amount'",
#         "Avoid being with people: 'Not at all'",
#         "Avoid being with people: 'A little bit'",
#         "Take water instead of caffeinated drinks",
#         "Take energy drinks/juice instead of caffeinated drinks",
#         "Take tea/milk/yoghurt instead of caffeinated drinks",
#         "Take carbonated drinks instead of caffeinated drinks",
#         "Eat solid food instead of caffeinated drinks",
#         "Chew gum instead of caffeinated drinks",
#         "Go to bed before 10",
#         "Go to bed after 10",
#         "Go to bed after 11",
#         "Go to bed after 12",
#         "Cannot get sleep within 30 minutes: Not during the past month",
#         "Wake up in the middle of the night or early morning: Not during the past month",
#         "Have to get up to use the bathroom: Not during the past month",
#         "Cannot breathe comfortably: Not during the past month",
#         "Cough or snore loudly: Not during the past month",
#         "Feel too cold: Not during the past month",
#         "Feel too hot: Not during the past month",
#         "Had bad dreams: Not during the past month",
#         "Have pain: Not during the past month",
#         "How often during the past month have you had trouble sleeping because of other reasons?: Not during the past month",
#         "During the past month, how often have you had trouble staying awake while driving, eating meals, or engaging in social activity?: Not during the past month",
#         "Cannot get sleep within 30 minutes: Less than once a week",
#         "Wake up in the middle of the night or early morning: Less than once a week",
#         "Have to get up to use the bathroom: Less than once a week",
#         "Cannot breathe comfortably: Less than once a week",
#         "Cough or snore loudly: Less than once a week",
#         "Feel too cold: Less than once a week",
#         "Feel too hot: Less than once a week",
#         "Had bad dreams: Less than once a week",
#         "Have pain: Less than once a week",
#         "How often during the past month have you had trouble sleeping because of other reasons?: Less than once a week",
#         "During the past month, how often have you had trouble staying awake while driving, eating meals, or engaging in social activity?: Less than once a week",
#         "Cannot get sleep within 30 minutes: Three or more times a week",
#         "Wake up in the middle of the night or early morning: Three or more times a week",
#         "Have to get up to use the bathroom: Three or more times a week",
#         "Cannot breathe comfortably: Three or more times a week",
#         "Cough or snore loudly: Three or more times a week",
#         "Feel too cold: Three or more times a week",
#         "Feel too hot: Three or more times a week",
#         "Had bad dreams: Three or more times a week",
#         "Have pain: Three or more times a week",
#         "How often during the past month have you had trouble sleeping because of other reasons?: Three or more times a week",
#         "During the past month, how often have you had trouble staying awake while driving, eating meals, or engaging in social activity?: Three or more times a week",
#         "Cannot get sleep within 30 minutes: Once or twice a week",
#         "Wake up in the middle of the night or early morning: Once or twice a week",
#         "Have to get up to use the bathroom: Once or twice a week",
#         "Cannot breathe comfortably: Once or twice a week",
#         "Cough or snore loudly: Once or twice a week",
#         "Feel too cold: Once or twice a week",
#         "Feel too hot: Once or twice a week",
#         "Had bad dreams: Once or twice a week",
#         "Have pain: Once or twice a week",
#         "How often during the past month have you had trouble sleeping because of other reasons?: Once or twice a week",
#         "During the past month, how often have you had trouble staying awake while driving, eating meals, or engaging in social activity?: Once or twice a week",
#         "Cannot get sleep within 30 minutes: Three or more times a week",
#         "Cannot get sleep within 30 minutes: Not during the past month",
#         "Cannot get sleep within 30 minutes: Less than once a week",
#         "During the past month, how often have you had trouble staying awake while driving, eating meals, or engaging in social activity?: Three or more times a week",
#         "During the past month, how often have you had trouble staying awake while driving, eating meals, or engaging in social activity?: Not during the past month",
#         "During the past month, how often have you had trouble staying awake while driving, eating meals, or engaging in social activity?: Less than once a week",
#         "During the past month, how much of a problem has it been for you to keep up enough enthusiasm to get things done?: No problem at all",
#         "During the past month, how much of a problem has it been for you to keep up enough enthusiasm to get things done?: Only a very slight problem",
#         "During the past month, how much of a problem has it been for you to keep up enough enthusiasm to get things done?: Somewhat of a problem",
#         "During the past month, how much of a problem has it been for you to keep up enough enthusiasm to get things done?: A very big problem"
#     ],
#     "Number of Students": [
#         114, 114, 54, 38, 69, 110, 29, 121, 3, 1, 51, 27, 4, 32, 21, 27, 8, 9, 7, 6, 38, 7, 1, 1, 13, 4, 10, 3, 7, 11, 24, 21,8,54, 3, 30, 18, 45, 40, 26, 43, 21, 54, 27, 52, 24, 33, 50, 47, 29, 60, 20, 45, 7, 9, 117, 21, 43, 38, 38, 35, 18, 26, 41, 69, 9, 30, 56, 59, 1, 3, 146, 4, 32, 27, 43, 52, 61, 50, 10, 33, 39, 45, 15, 21, 65, 53, 57, 8, 13, 11, 10, 1, 13, 37, 38, 38, 75, 37, 32, 126, 124, 98, 51, 109, 85, 118, 97, 31, 26, 23, 13, 12, 35, 22, 20, 56, 55, 4, 7, 8, 1, 13, 37, 38, 38, 75, 37, 32, 126, 124, 98, 51, 109, 85, 118, 97, 31, 26, 23, 13, 12, 35, 22, 20, 28, 35, 44, 11, 11, 13, 28, 19, 8, 118, 21, 7, 97, 26, 62, 57, 25, 10
#     ]
# }
#
# # Create DataFrame
# do = pd.DataFrame(data)
# do.to_excel("survey_data.xlsx", index=False)
# Display the DataFrame
df = pd.read_excel('survey_data.xlsx')
import pandas as pd

# Load the data into a DataFrame
data = {
    "Category": [
        "Increase heart rates", "Increase in Blood pressure", "Cause bone weakness?",
        "Cause for cancer", "Lead to Diabetes", "Lead to an increase in urination",
        "Acceptable amount of daily consumption of caffeine", "Acceptable amount of daily consumption of caffeine",
        "Acceptable amount of daily consumption of caffeine", "Acceptable amount of daily consumption of caffeine",
        "Caffeinated drinks during the examination period", "Consume Soda", "Consume caffeinated tea",
        "Consume Energy drinks", "Consume Coffee", "Use bottles", "Use sachets", "No preferences", "Use cans",
        "Take caffeinated drinks Thrice or more weekly", "Take caffeinated drinks weekly", "Take caffeinated drinks Daily",
        "Mixes caffeinated drinks with alcohol", "Mixes caffeinated drinks with drugs", "Feel nervousness from caffeinated drinks",
        "Have Irritable behavior from caffeinated drinks", "Feel mood swings from caffeinated drinks", "Hallucinate from caffeinated drinks",
        "Feel aggression from caffeinated drinks", "Feel Palpitation (Heart beating fast) from caffeinated drinks",
        "Feel Insomnia (Poor Sleep) from caffeinated drinks", "Feel Dizziness from caffeinated drinks", "Feel Vomiting from caffeinated drinks",
        "Feel craving for more from caffeinated drinks", "Feel Meal skipping from caffeinated drinks", "Concentrate on what to do next: 'a lot'",
        "Concentrate on what to do next: 'A medium amount'", "Concentrate on what to do next: 'Not at all'",
        "Concentrate on what to do next: 'A little bit'", "Talk to friends: 'a lot'", "Talk to friends: 'A medium amount'",
        "Talk to friends: 'Not at all'", "Talk to friends: 'A little bit'", "Talk to parents or relatives: 'a lot'",
        "Talk to parents or relatives: 'A medium amount'", "Talk to parents or relatives: 'Not at all'",
        "Talk to parents or relatives: 'A little bit'", "Sleeping: 'a lot'", "Sleeping: 'A medium amount'",
        "Sleeping: 'Not at all'", "Sleeping: 'A little bit'", "Crying: 'a lot'", "Crying: 'A medium amount'",
        "Crying: 'Not at all'", "Crying: 'A little bit'", "Spiritual – praying, meditation/yoga: 'a lot'",
        "Spiritual – praying, meditation/yoga: 'A medium amount'", "Spiritual – praying, meditation/yoga: 'Not at all'",
        "Spiritual – praying, meditation/yoga: 'A little bit'", "Watch television, movies: 'a lot'",
        "Watch television, movies: 'A medium amount'", "Watch television, movies: 'Not at all'", "Watch television, movies: 'A little bit'",
        "Play games/sports: 'a lot'", "Play games/sports: 'A medium amount'", "Play games/sports: 'Not at all'",
        "Play games/sports: 'A little bit'", "Smoking tobacco/ taking alcohol: 'a lot'", "Smoking tobacco/ taking alcohol: 'A medium amount'",
        "Smoking tobacco/ taking alcohol: 'Not at all'", "Smoking tobacco/ taking alcohol: 'A little bit'", "Keeping feeling to self: 'a lot'",
        "Keeping feeling to self: 'A medium amount'", "Keeping feeling to self: 'Not at all'", "Keeping feeling to self: 'A little bit'",
        "Tried to look on the bright side of life: 'a lot'", "Tried to look on the bright side of life: 'A medium amount'",
        "Tried to look on the bright side of life: 'Not at all'", "Tried to look on the bright side of life: 'A little bit'",
        "Spend more time alone: 'a lot'", "Spend more time alone: 'A medium amount'", "Spend more time alone: 'Not at all'",
        "Spend more time alone: 'A little bit'", "Refuse to think about it too much: 'a lot'", "Refuse to think about it too much: 'A medium amount'",
        "Refuse to think about it too much: 'Not at all'", "Refuse to think about it too much: 'A little bit'",
        "Double the efforts and work harder: 'a lot'", "Double the efforts and work harder: 'A medium amount'",
        "Double the efforts and work harder: 'Not at all'", "Double the efforts and work harder: 'A little bit'",
        "Convince self things aren’t as bad as it seem: 'a lot'", "Convince self things aren’t as bad as it seem: 'A medium amount'",
        "Convince self things aren’t as bad as it seem: 'Not at all'", "Convince self things aren’t as bad as it seem: 'A little bit'",
        "Avoid being with people: 'a lot'", "Avoid being with people: 'A medium amount'", "Avoid being with people: 'Not at all'",
        "Avoid being with people: 'A little bit'", "Take water instead of caffeinated drinks", "Take energy drinks/juice instead of caffeinated drinks",
        "Take tea/milk/yoghurt instead of caffeinated drinks", "Take carbonated drinks instead of caffeinated drinks", "Eat solid food instead of caffeinated drinks",
        "Chew gum instead of caffeinated drinks", "Go to bed before 10", "Go to bed after 10", "Go to bed after 11", "Go to bed after 12",
        "Cannot get sleep within 30 minutes: Not during the past month", "Wake up in the middle of the night or early morning: Not during the past month",
        "Have to get up to use the bathroom: Not during the past month", "Cannot breathe comfortably: Not during the past month",
        "Cough or snore loudly: Not during the past month", "Feel too cold: Not during the past month", "Feel too hot: Not during the past month",
        "Had bad dreams: Not during the past month", "Have pain: Not during the past month", "How often during the past month have you had trouble sleeping because of other reasons?: Not during the past month",
        "During the past month, how often have you had trouble staying awake while driving, eating meals, or engaging in social activity?: Not during the past month",
        "Cannot get sleep within 30 minutes: Less than once a week", "Wake up in the middle of the night or early morning: Less than once a week",
        "Have to get up to use the bathroom: Less than once a week", "Cannot breathe comfortably: Less than once a week", "Cough or snore loudly: Less than once a week",
        "Feel too cold: Less than once a week", "Feel too hot: Less than once a week", "Had bad dreams: Less than once a week", "Have pain: Less than once a week",
        "How often during the past month have you had trouble sleeping because of other reasons?: Less than once a week", "During the past month, how often have you had trouble staying awake while driving, eating meals, or engaging in social activity?: Less than once a week",
        "Cannot get sleep within 30 minutes: Three or more times a week", "Wake up in the middle of the night or early morning: Three or more times a week",
        "Have to get up to use the bathroom: Three or more times a week", "Cannot breathe comfortably: Three or more times a week", "Cough or snore loudly: Three or more times a week",
        "Feel too cold: Three or more times a week", "Feel too hot: Three or more times a week", "Had bad dreams: Three or more times a week", "Have pain: Three or more times a week",
        "How often during the past month have you had trouble sleeping because of other reasons?: Three or more times a week", "During the past month, how often have you had trouble staying awake while driving, eating meals, or engaging in social activity?: Three or more times a week",
        "Cannot get sleep within 30 minutes: Once or twice a week", "Wake up in the middle of the night or early morning: Once or twice a week",
        "Have to get up to use the bathroom: Once or twice a week", "Cannot breathe comfortably: Once or twice a week", "Cough or snore loudly: Once or twice a week",
        "Feel too cold: Once or twice a week", "Feel too hot: Once or twice a week", "Had bad dreams: Once or twice a week", "Have pain: Once or twice a week",
        "How often during the past month have you had trouble sleeping because of other reasons?: Once or twice a week", "During the past month, how often have you had trouble staying awake while driving, eating meals, or engaging in social activity?: Once or twice a week",
        "Cannot get sleep within 30 minutes: Three or more times a week", "Cannot get sleep within 30 minutes: Not during the past month",
        "Cannot get sleep within 30 minutes: Less than once a week", "During the past month, how often have you had trouble staying awake while driving, eating meals, or engaging in social activity?: Three or more times a week",
        "During the past month, how often have you had trouble staying awake while driving, eating meals, or engaging in social activity?: Not during the past month",
        "During the past month, how often have you had trouble staying awake while driving, eating meals, or engaging in social activity?: Less than once a week",
        "During the past month, how much of a problem has it been for you to keep up enough enthusiasm to get things done?: No problem at all",
        "During the past month, how much of a problem has it been for you to keep up enough enthusiasm to get things done?: Only a very slight problem",
        "During the past month, how much of a problem has it been for you to keep up enough enthusiasm to get things done?: Somewhat of a problem",
        "During the past month, how much of a problem has it been for you to keep up enough enthusiasm to get things done?: A very big problem"
    ],
    "Number of Students": [
        114, 114, 54, 38, 69, 110, 29, 121, 3, 1, 51, 27, 4, 32, 21, 27, 8, 9, 7, 6, 38, 7, 1, 1, 13, 4, 10, 3, 7, 11, 24, 21, 8, 54, 3, 30, 18, 45, 40, 26, 43, 21, 54, 27, 52, 24, 33, 50, 47, 29, 60, 20, 45, 7, 9, 117, 21, 43, 38, 38, 35, 18, 26, 41, 69, 9, 30, 56, 59, 1, 3, 146, 4, 32, 27, 43, 52, 61, 50, 10, 33, 39, 45, 15, 21, 65, 53, 57, 8, 13, 11, 10, 1, 13, 37, 38, 38, 75, 37, 32, 126, 124, 98, 51, 109, 85, 118, 97, 31, 26, 23, 13, 12, 35, 22, 20, 56, 55, 4, 7, 8, 1, 13, 37, 38, 38, 75, 37, 32, 126, 124, 98, 51, 109, 85, 118, 97, 31, 26, 23, 13, 12, 35, 22, 20, 28, 35, 44, 11, 11, 13, 28, 19, 8, 118, 21, 7, 97, 26, 62, 57, 25, 10
    ]
}

# Convert data to DataFrame
df = pd.DataFrame(data)

# Function to map frequency categories to scores
def map_frequency_to_score(frequency):
    if "Not during the past month" in frequency:
        return 0
    elif "Less than once a week" in frequency:
        return 1
    elif "Once or twice a week" in frequency:
        return 2
    elif "Three or more times a week" in frequency:
        return 3
    elif "Not at all" in frequency:
        return 0
    elif "A little bit" in frequency:
        return 1
    elif "A medium amount" in frequency:
        return 2
    elif "a lot" in frequency:
        return 3
    else:
        return None

# Apply the function to the 'Category' column to create a new column 'Score'
df['Score'] = df['Category'].apply(map_frequency_to_score)
df = df.dropna()

# Print the DataFrame with the added 'Score' column
df.to_excel("scored_data.xlsx", index=False)
print(df)


# Create DataFrame from the updated dictionary
# df = pd.DataFrame(df)

# Print the DataFrame
# print(df)
#
# print(scored_data)
# print(df)
# import matplotlib.pyplot as plt
# gender_freq = df['Gender'].value_counts()
#
# # Frequency distribution for Age Range (you can define your own age ranges)
# age_bins = [0, 20, 30, 40, 50]  # Define your own age bins
# age_labels = ['0-16', '16-18', '19-21', '22-25']  # Labels for age ranges
# df['Age Range'] = pd.cut(df['Age'], bins=age_bins, labels=age_labels, right=False)
# age_freq = df['Age Range'].value_counts()
#
# # Frequency distribution for Faculty
# faculty_freq = df['Faculty'].value_counts()
#
# # Frequency distribution for Level
# level_freq = df['Level'].value_counts()
#
# # Plotting frequency distributions
# plt.figure(figsize=(10, 8))
#
# # Gender distribution
# plt.subplot(2, 2, 1)
# gender_freq.plot(kind='bar', rot=0)
# plt.title('Gender Distribution')
#
# # Age range distribution
# plt.subplot(2, 2, 2)
# age_freq.plot(kind='bar', rot=0)
# plt.title('Age Range Distribution')
#
# # Faculty distribution
# plt.subplot(2, 2, 3)
# faculty_freq.plot(kind='bar', rot=90)
# plt.title('Faculty Distribution')
#
# # Level distribution
# plt.subplot(2, 2, 4)
# level_freq.plot(kind='bar', rot=0)
# plt.title('Level Distribution')
#
# plt.tight_layout()
# plt.show()
# print(do)

