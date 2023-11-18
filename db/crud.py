from dotenv import load_dotenv
import os

load_dotenv()


def create_table(name: str):
    return f'''
        CREATE TABLE IF NOT EXISTS {name} (
            id UUID DEFAULT uuid_generate_v4() PRIMARY KEY,
            title TEXT,
            description TEXT,
            tags TEXT[],
            status TEXT,
            rating DOUBLE PRECISION,
            deleted BOOLEAN,
            created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
            image BYTEA,
            current TEXT
        );
    '''


anime_table = create_table(os.getenv("ANIME_TABLE_NAME", "anime"))
manga_table = create_table(os.getenv("MANGA_TABLE_NAME", "manga"))


# insert
def insert(table: str, **values):
    columns_str = ', '.join(values.keys())
    values_str = ', '.join([f"'{value}'" for value in values.values()])
    query = f"INSERT INTO {table} ({columns_str}) VALUES ({values_str});"
    return query
