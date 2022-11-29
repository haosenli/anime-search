import os # for retrieving file paths
import json # for loading json files
import pandas as pd # for data parsing

def convert_aod_to_df(filepath: str) -> pd.DataFrame:
    """Converts the anime-offline-database to a pandas DataFrame.
    
    The offline database can be found here:
    https://github.com/manami-project/anime-offline-database
    
    Args:
        filepath (str): Path to the anime-offline-database.json file.
        
    Returns:
        A pandas Dataframe containing the anime data from the database.
    """
    # load data from database
    with open(filepath, 'r', encoding='utf-8') as f:
        anime_data = json.load(f)['data']
    # convert to pandas DataFrame
    df = pd.DataFrame(anime_data)
    print(df.head())
    output = os.path.join(
        os.getcwd(), 
        'database-api/anime-offline-database/test.csv')
    df.to_csv(output)
    

def main():
    filepath = os.path.join(
        os.getcwd(), 
        'database-api/anime-offline-database/anime-offline-database.json'
        )
    convert_aod_to_df(filepath)

if __name__ == '__main__':
    main() 