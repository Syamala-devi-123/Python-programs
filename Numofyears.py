#finding the num of years,weeks,days
days=int(input())
years=days//365
remaining_days=days%365
print("the no of years",years)
weeks=remaining_days//7
remaining_days=remaining_days%7
print("the no of weeks",weeks)
print("the no of days",remaining_days)
