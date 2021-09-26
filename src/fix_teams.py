import json
import os


source_folder = 'input'
output_folder = 'output'

files = os.listdir(source_folder)

for file in files:
  with open(source_folder + '/' + file, 'r') as input_file:
    data = input_file.read()
    json_data = json.loads(data)

    if not 'awayteam' in json_data:
      print(file + ' missing team')
      bigplays = json_data['bigplays']
      teams = []
      for play in bigplays:
        if not play['team'] in teams:
          teams.append(str(play['team']))
      if 'hometeam' in json_data:    
        teams.remove(str(json_data['hometeam']))
      json_data['awayteam'] = teams[0]
      print(teams[0] + ' set as hometeam for ' + file)


    if not 'hometeam' in json_data:
      print(file + ' missing team')
      bigplays = json_data['bigplays']
      teams = []
      for play in bigplays:
        if not play['team'] in teams:
          teams.append(str(play['team']))
      if 'awayteam' in json_data:
        teams.remove(str(json_data['awayteam']))
      json_data['hometeam'] = teams[0]
      print(teams[0] + ' set as awayteam for ' + file)

    print('Outputing file: ' + file)
    with open(output_folder + '/' + file, 'w') as output_file:
      output_file.write(json.dumps(json_data))
print('Done')