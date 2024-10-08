from ingestion.csvhandle import get_csv_data

def main():
    df = get_csv_data()
    print(df.head())
    print('Hey Pipeline')


if __name__ == '__main__':
    main()