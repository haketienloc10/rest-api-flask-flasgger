getAllTask_dict = {   
    "tags":[
        "Hello"
    ],
    "summary": "Get all task",
    "responses": {
        "200": {
            "description": "Get all task",
            "schema": {
                "properties":{
                    "id": {
                        "type": "string",
                        "description": "id task"
                    },
                    "title": {
                        "type": "string",
                        "description": "title a task"
                    },
                    "description": {
                        "type": "string",
                        "description": "description a task"
                    },
                    "done": {
                        "type": "boolean",
                        "description": "done task"
                    }
                }
            }
        }
    }
}

getTask_dict = {
    "tags":[
        "Hello"
    ],
    "summary": "Get task",
    "parameters": [
        {
            "name": "id",
            "in": "path",
            "type": "string",
            "required": "true",
            "description": "The id task"
        }
    ],
    "responses": {
        "200": {
            "description": "Get task",
            "schema": {
                "properties":{
                    "id": {
                        "type": "string",
                        "description": "id task"
                    },
                    "title": {
                        "type": "string",
                        "description": "title a task"
                    },
                    "description": {
                        "type": "string",
                        "description": "description a task"
                    },
                    "done": {
                        "type": "boolean",
                        "description": "done task"
                    }
                }
            }
        }
    }
}

createTask_dict = {
    "tags":[
        "Hello"
    ],
    "summary": "Create new task",
    "parameters": [
        {
            "name": "data",
            "in": "body",
            "schema":{
                "id": "task"
            }
        }
    ],
    "responses": {
        "200": {
            "description": "Get task",
            "schema": {
                "properties":{
                    "id": {
                        "type": "string",
                        "description": "id task"
                    },
                    "title": {
                        "type": "string",
                        "description": "title a task"
                    },
                    "description": {
                        "type": "string",
                        "description": "description a task"
                    },
                    "done": {
                        "type": "boolean",
                        "description": "done task"
                    }
                }
            }
        }
    }
}

updateTask_dict = {
    "tags":[
        "Hello"
    ],
    "summary": "Update task",
    "parameters": [
        {
            "name": "id",
            "in": "path",
            "type": "string",
            "required": "true",
            "description": "The id task"
        },
        {
            "name": "data",
            "in": "body",
            "schema":{
                "properties": {
                    "title": {
                        "type": "string",
                        "description": "title a task"
                    },
                    "description": {
                        "type": "string",
                        "description": "description a task"
                    },
                    "done": {
                        "type": "boolean",
                        "description": "done task"
                    }
                }    
            }
        }
    ],
    "responses": {
        "200": {
            "description": "Update task",
            "schema": {
                "properties":{
                    "id": {
                        "type": "string",
                        "description": "id task"
                    },
                    "title": {
                        "type": "string",
                        "description": "title a task"
                    },
                    "description": {
                        "type": "string",
                        "description": "description a task"
                    },
                    "done": {
                        "type": "boolean",
                        "description": "done task"
                    }
                }
            }
        }
    }
}

deleteTask_dict = {
    "tags":[
        "Hello"
    ],
    "summary": "Delete task",
    "parameters": [
        {
            "name": "id",
            "in": "path",
            "type": "string",
            "required": "true",
            "description": "Id task"
        }
    ],
    "responses": {
        "200": {
            "description": "delete success",
            "schema": {
                "properties":{
                    "result": {
                        "type": "boolean",
                        "description": "result"
                    }
                }
            }
        }
    }
}