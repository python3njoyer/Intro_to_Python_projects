import pandas as pd

# import data set
data = pd.read_csv('review_phx_class.csv')


# fill null values, convert review count to an integer, convert postal code to int then string
data = data.fillna(value=-9999)
data['review_count'] = data['review_count'].astype(int)

data['postal_code'] = data['postal_code'].astype(int)
data['postal_code'] = data['postal_code'].astype(str)


# return first 15 and last 10 lines of the cleaned dataset
df1 = pd.DataFrame(data)
print('First fifteen observations:')
print(df1.head(n=15))
print('----------------------------------------------------------------------------')
print('Last ten observations:')
print(df1.tail(n=10))
print('----------------------------------------------------------------------------')


# create new DataFrame without the missing values, display number of reviews, rating, and open status
df2 = df1.loc[(df1['review_count'] != -9999) & (df1['stars'] != -9999)]
print('Summary statistics:')
print(df2[['review_count','stars','is_open']].describe())
print('----------------------------------------------------------------------------')


# locates popular restaurants, displays the average rating and greatest review count out of the restaurants
# in each zip code
pop_df = df2.loc[(df2['review_count'] > 500) | (df2['stars'] > 4.0)]
agg1 = pop_df.groupby('postal_code').agg(
    avg_rating = ('stars','mean'),
    max_reviews = ('review_count','max')
).reset_index()
print('Popular restaurants statistics:')
print(agg1)


# locates all the open restaurants located in zip codes 85014, 85016, and 85018
open_df = df2.loc[((df2['postal_code'] == '85014') | (df2['postal_code'] =='85016') | (df2['postal_code'] == '85018'))
               & (df2['is_open'] == 1)]


# combines the popular restaurants and open restaurants in the above zip codes into one DataFrame, deletes duplicates
df3 = pop_df.append(open_df)
df3 = df3.drop_duplicates()


# sort the combined DataFrame and drop unneeded columns, export result to a csv file
df3 = df3.sort_values(by=['postal_code','review_count','stars'], ascending=[True,False,False])
columns = df3.drop(columns=['business_id','city','state','review_count','is_open'])

columns.to_csv('libbymerchant_assignment5.csv', index=False)
