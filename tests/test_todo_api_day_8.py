import requests
#Using for generating random id for below users at creation time
import uuid
ENDPOINT = "https://todo.pixegami.io"

#playing around APIs
def test_calling_endpoint():
    response = requests.get(ENDPOINT)
    assert response.status_code == 200

def create_task(payload):
    return requests.put(ENDPOINT + "/create-task",json=payload)

def get_task(task_id):
    return requests.get(ENDPOINT + f"/get-task/{task_id}")

def update_task(payload):
    return requests.put(ENDPOINT + "/update-task", json=payload)

def delete_task(task_id):
    return requests.delete(ENDPOINT + f"/delete-task/{task_id}")

def new_task_payload():
    user_id = f"test_user_{uuid.uuid4().hex}"
    content = f"test_content_{uuid.uuid4().hex}"
    print(f"Creating task for user {user_id} with some content i.e {content}")
    return {
        "content": content,
        "user_id": user_id,
        "is_done": False
    }

def list_tasks(user_id):
    return requests.get(ENDPOINT + f"/list-tasks/{user_id}")


def test_can_list_tasks():
    n = 3
    for _ in range(n):
        payload = new_task_payload()
        create_task_response = create_task(payload)
        assert create_task_response.status_code == 200

    list_task_response = list_tasks("test_user")
    assert list_task_response.status_code == 200
    len_of_list = len(list_task_response.json()["tasks"])
    print(len_of_list)
    assert n == len_of_list

def test_create_task():
    payload = {
            "content": "my creation test4",
            "user_id": "test_user_4",
            "is_done": False
    }
    create_task_response = create_task(payload)
    assert create_task_response.status_code == 200
    raw_data = create_task_response.json()
    print(raw_data)
    task_id = raw_data["task"]["task_id"]
    get_task_response = get_task(task_id)
    assert get_task_response.status_code == 200
    get_task_data = get_task_response.json()
    assert get_task_data["content"] == payload["content"]
    print(get_task_data)


def test_update_task():
    payload = {
        "content": "my creation test5",
        "user_id": "test_user_5",
        "is_done": False
    }
    created_task = create_task(payload)
    task_id = created_task.json()["task"]["task_id"]
    new_payload = {
        "content": "my updated content",
        "user_id": payload["user_id"],
        "task_id" : task_id,
        "is_done": True
    }
    updated_user = update_task(new_payload)
    assert updated_user.status_code == 200
    print(updated_user.json())
    get_task_after_update = get_task(task_id)
    assert get_task_after_update.json()["content"] == new_payload["content"]

def test_for_deleting_task():
    payload = new_task_payload()
    create_new_task = create_task(payload)
    assert create_new_task.status_code == 200
    task_id = create_new_task.json()["task"]["task_id"]
    delete_task_response = delete_task(task_id)
    assert delete_task_response.status_code == 200
    get_task_response = get_task(task_id)
    print(get_task_response)