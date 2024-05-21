from category_encoders import TargetEncoder
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
from sklearn.ensemble import GradientBoostingRegressor
from sklearn.preprocessing import StandardScaler

def build_pipeline(categorical_cols, numeric_cols, target_col):
    categorical_transformer = TargetEncoder()
    numeric_transformer = StandardScaler()
    
    preprocessor = ColumnTransformer(
        transformers=[
            ('categorical', categorical_transformer, categorical_cols),
            ('numeric', numeric_transformer, numeric_cols)
        ])
    
    model = GradientBoostingRegressor(
        learning_rate=0.01,
        n_estimators=300,
        max_depth=5,
        loss="absolute_error"
    )
    
    pipeline = Pipeline(steps=[
        ('preprocessor', preprocessor),
        ('model', model)
    ])
    
    return pipeline
