from decouple import config

print("Database Name:", config('DATABASE_NAME'))
print("Database User:", config('DATABASE_USER'))
print("Database Password:", config('DATABASE_PASSWORD'))
