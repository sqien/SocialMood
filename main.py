import pymysql.cursors

def db_submit_rating():  
    mood_list = ["Barely holding on","Worse than usual", "Meh", "Pretty good", "Good", "Perfect"]

    for elements, mood in enumerate(mood_list, start=1):
        print(f"{elements}: {mood}")
        pass

    mood_input = int(input("What's your mood today, choose from the list: "))
    choosen_mood = mood_list[mood_input - 1]

    while mood_input < 1 or mood_input > len(mood_list):
        print("You only have 6 options, buddy))")
        mood_input = int(input("What's your mood today, choose from the list: "))
    print(f"You choose option: {mood_input}, which means your mood is: {choosen_mood}")
    return choosen_mood

def db_submit_comment():
    comment_input = input("Enter your commentary: ")
    return comment_input


def main():
    connection = pymysql.connect(host='localhost',
                                user='root',
                                password='',
                                database='socialmood',
                                cursorclass=pymysql.cursors.DictCursor)
    
    mood = db_submit_rating()
    comment = db_submit_comment()

    with connection:
        with connection.cursor() as cursor:
            sql = "INSERT INTO `mood_entries` (`rating`, `comment`) VALUES (%s, %s)"
            cursor.execute(sql, (mood, comment))

        connection.commit()

        with connection.cursor() as cursor:
            sql = "SELECT `id`, `rating` FROM `mood_entries`"
            cursor.execute(sql)
            return cursor.fetchone()
        
main()
