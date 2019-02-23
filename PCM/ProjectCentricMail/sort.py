import csv
import os

listp=[]
module_dir = os.path.dirname(__file__)
def ip_pro():
 for i in range(n):
  pro_name=input("Enter projects name:")
  pro_name=pro_name.lower()
  project.insert(i,pro_name) 






def read(username,project,n):
	f = open(os.path.join(module_dir,f"csvfile/{username}.csv"))
	reader = csv.reader(f)
	cnt=0
	for m_id,Sender,Subject,Date,Snippet,Message_body in reader:
		cnt=cnt+1
		sort(m_id,Sender,Subject,Date,Snippet,Message_body,project,n)
	#print("Total count: ",cnt)
	

	with open(os.path.join(module_dir,f'csvfile/{username}_finalproject.csv'), 'w', encoding='utf-8', newline = '') as csvfile:
		fieldnames = ['m_id','Sender','Subject','Date','Snippet','Message_body','project']
		writer = csv.DictWriter(csvfile, fieldnames=fieldnames, delimiter = ',')
		writer.writeheader()
		for val in listp:
			#print(val)
			writer.writerow(val)
		return f'csvfile/{username}_finalproject.csv'



def sort(m_id,Sender,Subject,Date,Snippet,Message_body,project,n):
 Subject=Subject.lower()
 Message_body=Message_body.lower()
 Sender=Sender.lower()
 for i in range(n):
  
  flag_sub=Subject.find(project[i].lower())
  flag_mail=Message_body.find(project[i].lower())
  flag_sender=Sender.find(project[i].lower())
  if(flag_sub!=-1 or flag_mail!=-1 or flag_sender!=-1):
   final={}
   final['m_id']=m_id
   final['Sender']=Sender
   final['Subject']=Subject
   final['Date']=Date
   final['Snippet']=Snippet
   final['Message_body']=Message_body
   final['project']=project[i]
   listp.append(final)
   break
     
 
    
		



def main():
 csv.field_size_limit(100000000)
 project=[]
 project.append("cn")
 project.append("toc")
 print(project)
 read("ayushbansal323",project,2)
 print (listp)
 
if __name__=='__main__':
 main() 
 
