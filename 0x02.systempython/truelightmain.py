def main():
        db_manager = DatabaseManager()

            # Insert a new member
                db_manager.insert_member("John Doe", 30, "john.doe@example.com", "123-456-7890")

                    # Retrieve and print all members
                        members = db_manager.get_members()
                            for member in members:
                                        print(f"ID: {member[0]}, Name: {member[1]}, Age: {member[2]}, Email: {member[3]}, Phone: {member[4]}")

                                            db_manager.close()

                                            if __name__ == "__main__":
                                                    main()

