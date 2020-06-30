import pandas as pd 
people = {
    "first":['Corey' ,'Jane' , 'John' ] ,
    "last" : ['Schafer' , 'Doe' ,'Doe' ] ,
    "email" : ['CoreyMSchafer@gmail.com' , 'JaneDoe@email.com' ,'JohnDoe@gmail.com' ]
}
df = pd.DataFrame(people) 
df
## Adding column 
df['first']+ ' ' + df['last']

df['full_name'] = df['first']+ ' ' + df['last']
df

## Removing colums
# df.drop(columns = ['first', 'last' ] ) # first run it this command to see the result
df.drop(columns = ['first', 'last' ], inplace=True ) # then add inplace=True to commit the change 
df 

df['full_name'].str.split(' ' , expand=True  )

df[['first', 'last']] = df['full_name'].str.split(' ' , expand=True  )
df 

## Adding row of data
df.append({'first': 'Tony'} , ignore_index=True  )  # there is no index in this dataframe, so we need to add ignore_index=True

people2 = {
    "first":['Tony' ,'Steve'  ] ,
    "last" : ['Stark' , 'Rogers'  ] ,
    "email" : ['IronMan@avenger.com' , 'CapA@avenger.com'  ]
}
# create dataframe
df2 = pd.DataFrame(people2)
df2 

# Append 2 dataframe
df.append(df2, ignore_index=True , sort=False)
df = df.append(df2, ignore_index=True , sort=False) 
df 

## Remove a row
df.drop(index=4)

## Remove with conditional 
filt = df['last']== 'Doe'
df.drop(index=df[ filt ].index  )










