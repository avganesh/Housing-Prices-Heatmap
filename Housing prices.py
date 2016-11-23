import pandas as pd

##Need data to be in format Zipcode, price to use Openheatmap.com
##df2 = pd.read_csv("Zip_Zhvi_Summary_AllHomes.csv")
##df3 = pd.read_csv("free-zipcode-database-Primary.csv")
##latlong_df = df3[['Zipcode', 'Lat', 'Long']]
##Prices_df =df2[['RegionName','Zhvi']]
##Prices_df.to_csv("OpenHeatmapdata.csv")

##Need data to be in format Latitude-Longitude, price to use Google Heat Map API
##print(latlong_df.head())
##calc_df = Prices_df.merge(latlong_df, left_on='RegionName', right_on='Zipcode', how='left')
##calc_df['Location'] = calc_df.Lat.astype(str).str.cat(calc_df.Long.astype(str), sep=', ')
##df = calc_df[['Location', 'Zhvi']]
##print(df.head())
##df.to_csv("HeatMapData.csv")

##df = pd.read_csv("OpenHeatmapdata.csv")
##print(df.loc[:10][['RegionName', 'Zhvi']])
##df.loc[:100][['RegionName', 'Zhvi']].to_csv("TestData.csv")

df = pd.read_csv("HeatMapData.csv")
df['Query'] = '{location: new google.maps.LatLng(' +df['Location'].astype(str) + '), weight: ' + df['Zhvi'].astype(str) + '},'

print(df['Query'].head())
df['Query'].to_csv("Query.json")
