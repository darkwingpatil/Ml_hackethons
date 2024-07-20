def remove_Highly_Correlated(df, bar=0.8):
  # Creates correlation matrix
  corr = df.corr()

  # Set Up Mask To Hide Upper Triangle
  mask = np.triu(np.ones_like(corr, dtype=bool))
  tri_df = corr.mask(mask)

  # Finding features with correlation value more than specified threshold value (bar=0.9)
  highly_cor_col = [col for col in tri_df.columns if any(tri_df[col] > bar )]
  print("length of highly correlated columns",len(highly_cor_col))

  # Drop the highly correlated columns
  print(highly_cor_col)
  # reduced_df = df.drop(highly_cor_col, axis = 1)
  # print("shape of data",df.shape,"shape of reduced data",reduced_df.shape)
  # return reduced_df

remove_Highly_Correlated(features)