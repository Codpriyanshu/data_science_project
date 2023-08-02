 import datetime

class attendance_project_system:
       def 	_init_(self):
              self.u={"tanu":"tanush"}

              self.students_records ={}
              self.students_attendance ={}


       def login(self):
              while True:
                print("Attendance Management System")
                v=input("Press * for login and press # for exit")
                if v=="*":
                    username = input("Enter the username: ")
                    pwd = input("Enter the password: ")
                    if (username in self.u and self.u[username] == pwd):
                         print("You are authenticated user")
                         print("Successful login")
                         break
                    else:
                           print("Invalid Credentials.")
                else:
                      print("Exit")
                      break


       def add_records(self,student_id,student_name):
              self.students_records[student_id]=student_name

       def mark_attendance(self, date, student_id, p):
              if date not in self.students_attendance:
                     self.students_attendance[date]={}
              self.students_attendance[date][student_id]=p
         
       def view_records(self,student_id):
             print("Attendance ",(self.students_records.get(student_id,'N/A')))
             for date, p in self.students_attendance.items():
                   if student_id in p:
                         print("present")
                   else:
                         print("Absent") 

       def del_records(self,student_id,p):
              student_id=input("Enter the student_id which you want to delete: ")
              self.students_records.pop(student_id)
              self.students_attendance.pop(p)  
              print("Successful deleteion")

       def update_records(self,student_id,student_name,p):
            print("What you want to update 1.records 2.attendance")
            choice=input("Enter your choice: ")
            if choice==1:
                 print("What you want to update name or id")
                 up=input("1.Name & 2.Id")
                 if up==1:
                     student_name=input("Enter the updated student_name: ")
                     self.students_records.update(student_name)
                 elif up==2:
                     student_id=input("Enter the new student_id: ")   
                     self.students_records.update(student_id)    
                 else:
                     print("Enter the valid choice")
            elif choice==2:
                  student_id=input("Enter the student_id: ")
                  date=input("Enter the date(yyyy-mm-dd): ")
                  p=input("Enter 'p' for present and 'a' for absent : ")
                  self.students_attendance[date][student_id]=p

            else:
                  print("Enter valid choice")
              
def main():
            attendance_project=attendance_project_system()
            attendance_project.login()

            counter=0
            while True:     
                      counter+=1
                      print("Choice: 1.add records 2.mark records 3.update records 4.delete records 5.view attendance 6.Exit")
                      inp=int(input("Enter your choice "))

                      if inp==1:
                            student_id=input("Enter student_id: ")
                            student_name=input("Enter student name: ")
                            attendance_project.add_records(student_id,student_name)
                            print("Successful Addition")
                      elif inp==2:
                            date_str= input("Enter the date(yyyy-mm-dd) for attendance: ")
                            date=datetime.datetime.strptime(date_str,'%Y-%m-%d').date()
                            student_id=input("Enter the student_id:")
                            p=input("Enter 'p' for present and 'a' for absent: ")
                            attendance_project.mark_attendance(date,student_id,p)

                      elif inp==3:
                            attendance_project.update_records(student_id,student_name,p)
                      elif inp==4:
                            attendance_project.del_records(student_id)
                      elif inp==5:
                            student_id=input("Enter the student_id: ")
                            attendance_project.view_records(student_id)

                      elif inp==6:
                            print("Exit")
                            break
                      else:
                            print("Invalid choice. Enter valid one.")

                      if counter==3:
                            break
                      
if __name__=="__main__":
    main()