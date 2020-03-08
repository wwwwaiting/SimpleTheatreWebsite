from flask import Flask, jsonify, request
from flask_cors import CORS
import csv
import os

# Start the app and setup the static directory for the html, css, and js files.
app = Flask(__name__, static_url_path='', static_folder='static')
CORS(app)

# This is your 'database' of scripts with their blocking info.
# You can store python dictionaries in the format you decided on for your JSON
   # parse the text files in script_data to create these objects - do not send the text
   # files to the client! The server should only send structured data in the sallest format necessary.
scripts = {}


### DO NOT modify this route ###
@app.route('/')
def hello_world():
    return 'Theatre Blocking root route'

### DO NOT modify this example route. ###
@app.route('/example')
def example_block():
    example_script = "O Romeo, Romeo, wherefore art thou Romeo? Deny thy father and refuse thy name. Or if thou wilt not, be but sworn my love And I’ll no longer be a Capulet."

    # This example block is inside a list - not in a dictionary with keys, which is what
    # we want when sending a JSON object with multiple pieces of data.
    return jsonify([example_script, 0, 41, 4])


''' Modify the routes below accordingly to 
parse the text files and send the correct JSON.'''
def getActorIds():
    with open('/app/actors.csv', 'r') as csvfile:
        result = {}
        spamreader = csv.reader(csvfile, delimiter=',')
        for row in spamreader:
            result[row[1]] = row[0]
        return result


## GET route for script and blocking info
@app.route('/script/<int:script_id>')
def script(script_id):
    # right now, just sends the script id in the URL
    directory = '/app/script_data/'
    for file in os.listdir(directory):
        content = open(directory+ file, 'r').read().splitlines()
        scripts["script_" + str(content[0])] = {"script_name": file, "line": content[2], "actors":{}}
        # if content[0] == str(script_id):
        actor_map = getActorIds()
        for line in content[4:]:
            line_tokens = line.replace(",", "").split(" ")
            part = {"start_idx": int(line_tokens[1]), "end_idx":int(line_tokens[2]),"actor_blocks":{}}
            for actor_positions in line_tokens[3:]:
                position = actor_positions.split('-')[-1]
                actor_name = actor_positions.replace('-' + position, '')
                if actor_name in actor_map:
                    actor_id = actor_map[actor_name]
                    part["actor_blocks"][actor_id] = int(position)
                    if actor_name not in scripts["script_" + str(content[0])]["actors"]:
                        scripts["script_" + str(content[0])]["actors"][actor_id] = actor_name                
            scripts["script_" + str(content[0])]["part_" + line_tokens[0].replace(".", "")] = part
    if "script_" + str(script_id) in scripts:
        return jsonify(scripts["script_" + str(script_id)])
            

    return jsonify({})


## POST route for replacing script blocking on server
# Note: For the purposes of this assignment, we are using POST to replace an entire script.
# Other systems might use different http verbs like PUT or PATCH to replace only part
# of the script.
@app.route('/script', methods=['POST'])
def addBlocking():
    # right now, just sends the original request json
    directory = '/app/script_data/'
    request_data = request.json
    script = scripts["script_" + request_data['scriptNum']]
    script_name = script['script_name']
    with open(directory + script_name, 'r') as file:
    # read a list of lines into data
        data = file.readlines()
    for part, positions in request_data.items():
        if part != "scriptNum":
            line_num = int(part[5:]) + 3
            temp = data[line_num].replace(",", "").split(" ")
            idx = 3
            for t in temp[3:]:
                actor = t[:t.rfind('-')]
                temp[idx] = actor + '-' + str(positions[actor])
                idx += 1
            new_line = ", ".join(temp) + '\n'
            data[line_num] = new_line.replace(".,", ".")
    with open(directory + script_name, 'w') as file:
        file.writelines(data)

    return jsonify(request_data)



if __name__ == "__main__":
    # Only for debugging while developing
    app.run(host='0.0.0.0', debug=True, port=os.environ.get('PORT', 80))

