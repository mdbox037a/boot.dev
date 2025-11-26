from queue import Queue

queue = Queue()


def matchmake(queue, user):
    name = user[0]
    action = user[1]
    if action is "leave":
        queue.search_and_remove(name)
    elif action is "join":
        queue.push(name)

    if queue.size() >= 4:
        user1 = queue.pop()
        user2 = queue.pop()
        return f"{user1} matched {user2}!"
    else:
        return "No match found"
