#Data Analysis using PandasAI
#Now let’s begin our analysis:
#prompt 1
pandas_ai.run(df, prompt="Which players are the most costliest buys?")

#you will get the output after running this prompt1

#prompt 2
prompts = """ What players were the cheapest buys of 2023 season and which team bought them? """
pandas_ai.run(df, prompt=prompts)
#output will be the list of cheapest players purchased by team

#prompt 3
prompts = """ Draw a Bargraph showing How much money teams spent in 2023 season."""
pandas_ai.run(df, prompt=prompts)
# output will be the bar graph of expenditures


#prompt 4
pandas_ai.run(df, prompt="How many bowler remained unsold and what was their base price?")

# this will show the number of bowlers left unbaught and their base price

#prompt 5
pandas_ai.run(df, prompt="How many players remained unsold this season?")

# this will show the number of players left unbaught by teams


#prompt 6
pandas_ai.run(df, prompt="Which type of players were majorly unsold?")

#this will show the output of types of players that were unsold


#prompt 7
pandas_ai.run(df, prompt="Who are three new players Gujrat picked?")

#This will show the new players baught by Gujrat team in 1pl 2023 auction

#prompt 8
pandas_ai.run(df, prompt="What is total money spent by all teams in dollars?")

#since $ is considered as a universal representation this will show the total dollars spent by teams


#prompt 9
prompts = """ draw a barplot showing how much money was spent by Mumbai Indians on all types of players? """
pandas_ai.run(df, prompt=prompts)

#this will show the barplot of total money spent by Mumbai Indians on all types of players

#prompt 10
prompts = """ draw a barplot showing how much money was spent by Gujrat on all types of players? """
pandas_ai.run(df, prompt=prompts)


#prompt 11
pandas_ai.run(df, prompt="Perform univariate analysis")


#prompt 12
print(pandas_ai.run(df, prompt="Can you predict which team will spend the highest money in 2024?"))
# this will give output of which team will spend highest in 2024 based on 2023 reports

#prompt 13
pandas_ai.run(df, prompt="Perform multivariate analysis")

