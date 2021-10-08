arqids = open('./soIds.txt')
arqScriptFinal = open('./scriptFinalPerfis.txt', 'a')

ids = arqids.readlines()

for id in ids:
    id = id.rstrip('\n')
    arqScriptFinal.write(f"INSERT INTO glpi_profiles_users (users_id, profiles_id)  SELECT id, 1 from glpi_users WHERE name = '{id}';\n")



