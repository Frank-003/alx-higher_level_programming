#!/usr/bin/node
def get_completed_tasks(api_url):
    try:
        response = requests.get(api_url)
        response.raise_for_status()  # Raise an exception if the request fails
        tasks = response.json()

        # Create a dictionary to store the task count for each user
        user_task_count = {}

        for task in tasks:
            if task['completed']:
                user_id = task['userId']
                user_task_count.setdefault(user_id, 0)
                user_task_count[user_id] += 1

        # Print the results
        for user_id, count in user_task_count.items():
            print(f"User {user_id} completed {count} tasks.")

    except requests.RequestException as e:
        print(f"Error fetching data: {e}")
