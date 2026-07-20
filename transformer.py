import pandas as pd


def transform_datasets(datasets):

    print("\n" + "=" * 70)
    print("TRANSFORMING DATASETS")
    print("=" * 70)

    transformed = {}

    for name, df in datasets.items():

        df = df.copy()

        # ----------------------------
        # Remove Duplicate Rows
        # ----------------------------
        before = len(df)

        df = df.drop_duplicates()

        after = len(df)

        # ----------------------------
        # Trim Spaces from Column Names
        # ----------------------------
        df.columns = df.columns.str.strip()

        # ----------------------------
        # Convert Object Columns to String
        # ----------------------------
        for col in df.select_dtypes(include="object").columns:

            df[col] = df[col].astype(str).str.strip()

        transformed[name] = df

        print(f"✅ {name:<20} Rows: {before} → {after}")

    print("\n🎉 All datasets transformed successfully!")

    return transformed