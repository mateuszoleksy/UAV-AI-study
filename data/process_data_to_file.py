import pandas as pd
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler, LabelEncoder
from configuration import configuration


def advanced_processing(df):
    while True:
        print("\n--- Choose action ---")
        print("1.Standard Scaling (Normalize ranges for PCA/Model)")
        print("2.PCA (Compress multiple columns into Components)")
        print("3.Label Encoding (Convert Categories to Numbers)")
        print("4.Handle Missing Values (Imputation)")
        print("Q.Finish and Return Data")
        choice = input("\nSelect processing step: ").strip().upper()

        if choice == '1':
            # Scaling is mandatory before PCA
            cols = df.select_dtypes(include=['number']).columns.tolist()
            print(f"Scaling columns: {cols}")
            scaler = StandardScaler()
            df[cols] = scaler.fit_transform(df[cols])
            print("Done: Data now has Mean=0 and Std=1.")

        elif choice == '2':
            # PCA Compression
            n_comp = int(input("How many components to compress into? "))
            numeric_df = df.select_dtypes(include=['number'])

            pca = PCA(n_components=n_comp)
            components = pca.fit_transform(numeric_df)

            # Create a new DF for components
            pca_cols = [f'PC{i + 1}' for i in range(n_comp)]
            df_pca = pd.DataFrame(data=components, columns=pca_cols)

            print(f"Compressed {numeric_df.shape[1]} columns into {n_comp} components.")
            print(f"Explained Variance Ratio: {pca.explained_variance_ratio_.sum():.2%}")
            df = df_pca  # Usually, you replace the numeric parts with PCA results

        elif choice == '3':
            col = input("Enter categorical column to encode: ")
            if col in df.columns:
                le = LabelEncoder()
                df[col] = le.fit_transform(df[col].astype(str))
                print(f"Converted {col} to numeric labels.")

        elif choice == '4':
            print("1. Fill with Median | 2. Drop rows with NaNs")
            sub_choice = input("Choice: ")
            if sub_choice == '1':
                df = df.fillna(df.median(numeric_only=True))
            else:
                df = df.dropna()
            print("Missing values handled.")

        elif choice == 'Q':
            return df


def main():
    dataset = pd.read_csv(configuration.get_filepath_to_save())
    result = advanced_processing(dataset)
    result.to_csv(configuration.get_filepath_to_output(), index=False)
    print("Saved output data to: ", configuration.get_filepath_to_output())


if __name__ == "__main__":
    main()