from connect_mysql import connect_database
from mysql.connector import Error

conn = connect_database()

def view_members_table():
    query = f"Select * from Members"
    cursor.execute(query)
    print(f"\nMembers table:")
    for row in cursor.fetchall():
        print(f"Member ID#: {row[0]}, Name: {row[1]}, Age: {row[2]}.")

def add_member(id, name, age):
    new_member = (id, name, age)
   
    if type(id) is not int:
        raise TypeError(f"ID must be an integer.")
    if type(name) is int:
        raise TypeError(f"Name cannot be an integer.")
    if type(age) is not int:
        raise TypeError(f"Age must be an integer.")
    if age < 18 or age > 120:
        raise ValueError(f"Member must be at least 18 and less than 120.")
    
    query = "Insert into Members (id, name, age) values (%s, %s, %s)"

    cursor.execute(query, new_member)
    conn.commit()
    print(f"New member: {name}, added successfully. ID#: {id}.")

def update_member(name, age, id):
    updated_member = (name, age, id)
    if type(id) is not int:
        raise TypeError(f"ID must be an integer.")
    if type(name) is int:
        raise TypeError(f"Name cannot be an integer.")
    if type(age) is not int:
        raise TypeError(f"Age must be an integer.")
    if age < 18 or age > 120:
        raise ValueError(f"Member must be at least 18 and less than 120.")

    query = "UPDATE Members\nSET\nname = %s,\nage = %s\nWHERE id = %s"
    cursor.execute(query, updated_member)
    conn.commit()
    print(f"Member id:{id} udpated to Name:{name}, Age:{age}.")

def delete_member(id):
    deleted_member = (id, )
    query = "DELETE FROM Members WHERE id = %s"
    cursor.execute(query, deleted_member)
    conn.commit()
    print(f"Member ID#:{id} deleted.")

def add_workout(member_id, session_date, session_time, activity):
    new_member = (member_id, session_date, session_time, activity)
   
    if type(member_id) is not int:
        raise TypeError(f"ID must be an integer.")
    if type(session_time) is not int:
        raise TypeError(f"Duration must be an integer in minutes.")
    if type(activity) is int:
        raise TypeError(f"Activity cannot be an integer.")
    
    query = "Insert into WorkoutSessions (member_id, session_date, session_time, activity) values (%s, %s, %s, %s)"

    cursor.execute(query, new_member)
    conn.commit()
    print(f"New workout logged for ID#{member_id}: {activity} for {session_time} minutes on {session_date}.")

def delete_workout(session_id):
    j = 0
    query = f"Select * from WorkoutSessions"
    cursor.execute(query)
    for row in cursor.fetchall():
        if session_id == row[0]:
            j = 1
            deleted_workout = (session_id, )
            query = "DELETE FROM WorkoutSessions WHERE session_id = %s"
            cursor.execute(query, deleted_workout)
            conn.commit()
            print(f"Workout Session ID#: {session_id} deleted.")
    if j == 0: 
        print(f"Error: No workout session with ID#: {session_id} to delete.")

def view_workouts_table():
    query = f"Select * from WorkoutSessions"
    cursor.execute(query)
    print(f"\nWorkout Sessions Table:")
    for row in cursor.fetchall():
        print(f"Session ID#: {row[0]}, Member ID#: {row[1]}, Workout Date: {row[2]}, Workout Duration: {row[3]}, Workout: {row[4]}.")

def get_members_in_age_range(start_age, end_age):
    query = f"Select * from Members\nWHERE age between {start_age} AND {end_age}"
    cursor.execute(query)
    print(f"\nMembers table:")
    for row in cursor.fetchall():
        print(f"Member ID#: {row[0]}, Name: {row[1]}, Age: {row[2]}.")

if conn is not None:
    try:
        cursor = conn.cursor()


        ## Members Table Functions ##

        #add_member(7, "Jonny", 19) 
        #update_member("Lauren", 50, 2)
        #delete_member(1)
        #view_members_table()

        #------------------------------#

        ## Workout Seesions Table Functions ##

        #add_workout(1, "2024/03/21", 90, "running")
        #view_workouts_table()
        #delete_workout(3)

        get_members_in_age_range(25, 30)

    except Error as db_err:
        print(f"Error: {db_err}") 
    
    except Exception as e:
        print(f"Error: {e}") 
    
    finally:
        cursor.close()
        conn.close()
        print("\nMySQL connection is closed.")