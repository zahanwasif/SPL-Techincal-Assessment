STATUS =  ['freshman', 'sophomore','junior', 'senior']

class User:
	def __init__(self,fname='',lname='',pwd='',uname=''):
		self.firstName = fname
		self.lastName = lname
		self.password = pwd
		self.userName = uname
		self.isSignedIn = False
	
	def signin(self,username,password):
		if self.userName == username and self.password ==password:
			self.isSignedIn = True
			print("signed in")
			return True
		else:
			print("incorrect username/password")
			return False
	def signOut(self):
		if self.isSignedIn:
			self.isSignedIn = False
			print("signed out")
			return True
		else:
			print("could not sign out/ trying signing in first")
			return False

	def getProfile(self):
		print("im just an lms user")


		

class Course:
	def __init__(self,cname='',ccode='',offeringsch='',capacity=0,instructors = [],students=[],resources=[]):
		self.courseName=cname
		self.courseCode = ccode
		self.offeringSchool = offeringsch
		self.capacity = capacity
		self.instructors = instructors
		self.resources = resources
		self.roster = self.instructors+students
		self.assignments = []
	
	

class Assignment:
	def __init__(self,name='',studentsMarks={},dueDate='',totalMarks=0):
		self.name=name
		self._studentMarks=studentsMarks
		self.dueDate = dueDate
		self.totalMarks = totalMarks
	def getStudentMarks(self,rollNumber):
		return self.studentsMarks.get(rollNumber)
	def addStudentsMarks(self,sroll=[],smarks=[]):
		self._studentMarks.update(dict(zip(sroll,smarks)))

class Student(User):
	def __init__(self,fname='',lname='',pwd='',uname='',rnum='',status='',courses=[]):
		User.__init__(self,fname,lname,pwd,uname)
		self.rollNumber=rnum
		if status in STATUS:
			self.status= status
		else:
			print("incorrect status can only be  freshman, sophomore, junior or senior")
		self.courses = courses
	def getProfile(self):
		print("{} is a {} at LUMS".format(self.firstName+' '+self.lastName,self.status))
	def getCourse(self,courseCode):
		for course in self.courses:
			if course.courseCode == courseCode:
				return course
		
	def viewResources(self,courseCode):
		resources= self.getCourse(courseCode).resouces
		print("following are resouces for course {}".format(courseCode))
		for resource in resources:
			print(resource.name)
	
	def viewRoster(self,courseCode):
		roster = self.getCourse(courseCode).roster
		print("following is the roster for course {}".format(courseCode))
		for person in roster:
			print(person.firstName+" "+person.lastName)

	def viewAssignments(self,courseCode):
		print("following are assignments for course {}".format(courseCode))
		assignments = self.getCourse(courseCode).assignments
		print("Name | Due Date | obtained marks | total Marks")
		for assignment in assignments:
			print("{} | {}| | {}".format(assignment.name,assignment.dueDate,assignment.getStudentMarks(self.rollNumber),assignment.totalMarks))
	
		

class Instructor(User):
	def __init__(self,fname='',lname='',pwd='',uname='',designation='',qualification='',courses=[]):
		User.__init__(self,fname,lname,pwd,uname)
		self.designation = designation
		self.qualification = qualification
		self.courses = courses

	def getProfile(self):
		print("{} is a {} at LUMS".format(self.firstName+' '+self.lastName,self.designation))
	
	def viewRoster(self,courseCode):
		roster = self.getCourse(courseCode).roster
		print("following is the roster for course {}".format(courseCode))
		for person in roster:
			print(person.firstName+" "+person.lastName)
	def getCourse(self,courseCode):
		for course in self.courses:
			if course.courseCode == courseCode:
				return course
	def viewResources(self,courseCode):
		resources= self.getCourse(courseCode).resouces
		print("following are resouces for course {}".format(courseCode))
		for resource in resources:
			print(resource.name)
	
	def addResource(self,courseCode,name):
		for course in self.courses:
			if course.courseCode == courseCode:
				course.resouces.append(name)
	
	
	def viewAssignments(self,courseCode):
		print("following are assignments for course {}".format(courseCode))
		assignments = self.getCourse(courseCode).assignments
		print("Name | Due Date | total Marks")
		for assignment in assignments:
			print("{} | {}| | {}".format(assignment.name,assignment.dueDate,assignment.totalMarks))

	def addAssignment(self,courseCode,aname='',tmarks=0,ddate=''):
		for course in self.courses:
			if course.courseCode == courseCode:
				course.assignments.append(Assignment(name=aname,dueDate=ddate,totalMarks=tmarks))

	def viewMarks(self,sRoll,smarks,courseCode):
		print("marks of student {} for course {}".format(sRoll,courseCode))
		assignments = self.getCourse(courseCode).assignments
		print("Name | Due Date | obtained marks | total Marks")
		for assignment in assignments:
			print("{} | {}| | {}".format(assignment.name,assignment.dueDate,assignment.getStudentMarks(sRoll),assignment.totalMarks))

	def addMarks(self,courseCode,assignmentName,omarks,sroll):
		for course in self.courses:
			if course.courseCode == courseCode:
				for assignment in course.assignments:
					if assignment.name== assignmentName:
						assignment.addStudentsMarks([sroll],[omarks])
	