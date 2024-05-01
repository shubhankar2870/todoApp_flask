from flask import Flask, request

app = Flask(__name__)

"""
create todo repository
"""
todo = {
    1: {
        "id": 1,
        "task": "Create a flask project",
        "deadline": "01/05/2024"
    },
    2: {
        "id": 2,
        "task": "Solve aptitude for 1 hr",
        "deadline": "02/05/2024"
    },
    3: {
        "id": 3,
        "task": "Learn power BI for 2 hr",
        "deadline": "01/05/2024"
    },
}

"""
create an RESTful endpoint for fetching the todos
"""
@app.get('/todoApp/api/v1/todos')
def get_todos():
    deadline = request.args.get('deadline')

    if deadline:
        todo_res = {}

        for key, value in todo.items():
            if value['deadline'] == deadline:
                todo_res[key] = value
        #return todo with deadline given
        return todo_res
    
    #fetch all the tasks
    return todo

"""
create an RESTful endpoint for creating a todo
"""
@app.post('/todoApp/api/v1/todos')
def create_todo():
    #get the data from the request body
    request_body = request.get_json()

    if request_body["id"] and request_body["id"] in todo:
        return {"error": "id already exists"}, 400
    
    #insert the passe todo in the todo list
    todo[request_body["id"]] = request_body
    return "task created and saved",201

"""
create a RESTful endpoint to fetch task based on todo id
"""
@app.get('/todoApp/api/v1/todos/<todo_id>')
def get_task_by_id(todo_id):
    if int(todo_id) in todo:
        return todo[int(todo_id)],200
    else:
        return {"error": "task not found"}, 404
    

"""
create a RESTful endpoint to update a task
"""
@app.put('/todoApp/api/v1/todos/<todo_id>')
def update_task(todo_id):
    if int(todo_id) in todo:
        todo[int(todo_id)] = request.get_json()
        return todo[int(todo_id)],200 
    else:
        return {"error": "task not found"}, 404
    

"""
create a RESTful endpoint to delete a task
"""
@app.delete('/todoApp/api/v1/todos/<todo_id>')
def delete_task(todo_id):
    if int(todo_id) in todo:
        todo.pop(int(todo_id))
        return {"message": "task deleted"}, 200
    else:
        return {"error": "task not found"}, 404



if __name__ == '__main__':
    app.run(port=8080)