fun main() {
            val dbManager = DatabaseManager()

                // Insert a new member
                    dbManager.insertMember("John Doe", 30, "john.doe@example.com", "123-456-7890")

                        // Retrieve and print all members
                            val members = dbManager.getMembers()
                                for (member in members) {
                                            println("ID: ${member.id}, Name: ${member.name}, Age: ${member.age}, Email: ${member.email}, Phone: ${member.phone}")
                                                }
                                }

