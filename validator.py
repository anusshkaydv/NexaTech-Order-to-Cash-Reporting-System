def validate_datasets(datasets):

    print("\n" + "=" * 70)
    print("NEXATECH ETL DATA QUALITY REPORT")
    print("=" * 70)

    total_rows = 0
    total_missing = 0
    total_duplicates = 0

    for name, df in datasets.items():

        rows = df.shape[0]
        columns = df.shape[1]
        missing = df.isnull().sum().sum()
        duplicates = df.duplicated().sum()

        total_rows += rows
        total_missing += missing
        total_duplicates += duplicates

        # Business Rule
        if name == "shipments":
            status = "WARNING"
            remark = "Shipment dates are blank for pending/cancelled orders."
        elif missing == 0 and duplicates == 0:
            status = "PASS"
            remark = "Dataset passed validation."
        else:
            status = "CHECK"
            remark = "Needs review."

        print(f"\n{name.upper()}")
        print("-" * 55)
        print(f"Rows              : {rows}")
        print(f"Columns           : {columns}")
        print(f"Missing Values    : {missing}")
        print(f"Duplicate Rows    : {duplicates}")
        print(f"Status            : {status}")
        print(f"Remark            : {remark}")

    print("\n" + "=" * 70)
    print("SUMMARY")
    print("=" * 70)

    print(f"Total Datasets    : {len(datasets)}")
    print(f"Total Rows        : {total_rows}")
    print(f"Total Missing     : {total_missing}")
    print(f"Total Duplicates  : {total_duplicates}")