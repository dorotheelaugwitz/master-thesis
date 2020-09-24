# Use linear regression to predict missing values for 'precip_accumulation'

from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

trainable = df.loc[df.precip_accumulation > 0.0]

# do not use outliers in 'precip_intensity' for prediction
trainable = trainable[['precip_intensity', 'precip_accumulation']].loc[trainable.precip_intensity <= trainable.precip_intensity.quantile(0.75)]

# create training and test sets
X = trainable.iloc[:, :-1].values
y = trainable.iloc[:, 1].values

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)

# fit the training data
regressor = LinearRegression()
regressor.fit(X_train, y_train)

# predict values
y_pred = regressor.predict(X_test)

# show predictions and actual values in a data frame
pd.DataFrame({'Actual': y_test, 'Predicted': y_pred})

# use fitted model for actual missing values
Z = df.loc[df.precip_accumulation.isna()].precip_intensity.values
z_pred = regressor.predict(Z.reshape(-1, 1))

# insert predicted values into original data set
pred_slice = df.loc[df.precip_accumulation.isna()][['precip_intensity']]
pred_slice['precip_accumulation'] = z_pred
df.fillna(pred_slice, inplace=True)
