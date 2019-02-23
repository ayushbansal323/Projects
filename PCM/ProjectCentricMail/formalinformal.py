import numpy as np
from sklearn.pipeline import Pipeline
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.svm import LinearSVC
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.multiclass import OneVsRestClassifier
from sklearn.preprocessing import MultiLabelBinarizer
import csv
import os

def PCM_formalinformal(username):
    module_dir = os.path.dirname(__file__)
    X_train = np.array(["Thank you",
                    "announcement",
                    "letters",
                    "notice of termination",
                    "request",
                    "I wanted to ask you",
                    "I wanted to let you know that",
                    "I am reaching out to",
                    "The reason for my email is that",
                    "The purpose of this email is to",
                    "To whom it may concern .",
                    "Dear Sir or Madam",
                    "My name is Earl Rivers. I'm contacting you to apply for the administrative assistant position listed on CareerXYZ.com.",
                    "My name is Arlene Rivers. I obtained your email address from the Westchester County Clerk website. I am writing to contest the traffic citation I received on December 31, 2009. ",
                    "Yours sincerely,",
                    "Just a quick note to invite you to…/ to tell you that",
                    "This is to invite you to join us for",
                    "I wanted to let you know that / tell you about / ask you if",
                    "I am writing to make a reservation/ to apply for the position of…/ to confirm my booking/ to ask for further information about",
                    "I am writing with regard  to the sale of …/ to the complaint you made on 29th February",
                    "With reference to our telephone conversation on Friday, I would like to let you know that"
                    "She has decided to accept the job.",
                    "The girl whom I met in Singapore was interested in working in Australia.",
                    "We went to Barcelona for the weekend. We have a lot of things to tell you.",
                    "It is best to commence the electrolytic thickening in a silver acetate bath.",
                    "The bombardment will commence on September.",
                    "But when the combat was about to commence it was interrupted by the king...",
                    "We may conveniently commence with them on account of their simplicity and great importance in respect to the theory of optical instruments.",
                    "Aphides are born, as a rule, alive, and the young soon commence to reproduce again.",
                    "All three codes contain a somewhat miscellaneous collection of laws; all alike commence with regulations as to the place of sacrifice and close with an exhortation.",
                    "With regard to claret it may be said that as a general rule the wine will not improve after twenty-five to thirty years, and that after this time it will commence to deteriorate.",
                    "We commence with processes, and see what they lead to; and thus get an idea of sums and differences.",
                    "But he was too original to remain long content with a subordinate position, and the pottery business was developing so rapidly that he had every inducement to commence work on his own account.",
                    "The expedition was to commence with a campaign against the Turcomans Herat being its later destination.",
                    "The owner could call in his land and terminate the relation at any time, for any reason, or for none at all.",
                    "Both branches terminate in a broad tidal lake immediately above Lisbon.",
                    "Salts formed from hydracids terminate in -ide, following the rule for binary compounds.",
                    "Under normal conditions, the situation could not fail to terminate favourably for the Vatican.",
                    "To the Belgian throne in 1909 a serious endeavour was made to improve the state of affairs in the Congo.",
                    "In this endeavour he met with vigorous opponents.",
                    "May I sit with you.",
                    "May we come in.",
                    "They may be too busy running.",
                    "She’s decided to accept the job.",
                    "The girl I met in Singapore was interested in working in Australia.",
                    "Went to Barcelona for the weekend. Lots to tell you.",
                    "He's acting funny today.",
                    "He's always been so alert and in control.",
                    "He's gone to heaven now.",
                    "Oh, he's thrown himself down there in the passage.",
                    "That's not funny.",
                    "He's acting funny today.",
                    "Don't laugh at me!",
                    "His laugh was short and humorless.",
                    "Suppressing the urge to laugh wasn't easy, but she managed it.",
                    "A laugh bubbled up.",
                    "He gave a husky laugh at her words.",
                    "I will choke it with my strong arms.",
                    "If the people of Boston must fight for their liberty, we will help them.",
                    "If you panic, she will be frightened.",
                    "That’s not good – you should go to the doctor.",
                    "First of all, you shouldn’t spend so much time on the computer.",
                    "Could and couldn’t are the past forms of can and can’t.",
                    "His voice was controlled.",
                    " ",
                    "Thank you and happy learning :) Regards"           
                    ])

    y_train_text = [["formal"],["formal"],["formal"],["formal"],["formal"],
                ["informal"],["informal"],["informal"],["informal"],["informal"],
                ["formal"],["formal"],["formal"],["formal"],["formal"],["informal"],["informal"],["informal"],["formal"],["formal"],["formal"]
                ,["formal"],["formal"],["formal"],["formal"],["formal"],["formal"],["formal"],["formal"],["formal"],["formal"],["formal"],["formal"]
                ,["formal"],["formal"],["formal"],["formal"],["formal"],["formal"],["formal"],["formal"],["formal"],["formal"]
                ,["informal"],["informal"],["informal"],["informal"],["informal"],["informal"],["informal"],["informal"],["informal"],["informal"],["informal"],["informal"]
                ,["informal"],["informal"],["informal"],["informal"],["informal"],["informal"],["informal"],["informal"],["informal"],["formal"]]
    f = open(os.path.join(module_dir,f'csvfile/{username}.csv'))
    reader = csv.reader(f)
    listf=[]
    listtest=[]
    listm_id=[]
    listSender=[]
    listSubject=[]
    listDate=[]
    listSnippet=[]
    listMessage_body=[]
    for m_id,Sender,Subject,Date,Snippet,Message_body in reader:
        listtest.append(Snippet+Message_body)
        listm_id.append(m_id)
        listSender.append(Sender)
        listSubject.append(Subject)
        listDate.append(Date)
        listSnippet.append(Snippet)
        listMessage_body.append(Message_body)

    X_test = np.array(listtest)
    target_names = ['informal', 'formal']

    mlb = MultiLabelBinarizer()
    Y = mlb.fit_transform(y_train_text)

    classifier = Pipeline([
    ('vectorizer', CountVectorizer()),
    ('tfidf', TfidfTransformer()),#Term Frequency (Tf),Inverse Document Frequency (idf);
    ('clf', OneVsRestClassifier(LinearSVC()))])

    classifier.fit(X_train, Y)
    predicted = classifier.predict(X_test)
    all_labels = mlb.inverse_transform(predicted)

    for item, labels,m_id,Sender,Subject,Date,Snippet,Message_body in zip(X_test, all_labels ,listm_id,listSender,listSubject,listDate,listSnippet,listMessage_body ):
        #print(f'{item} => {labels[0]} {m_id}')
        final={}
        final['m_id']=m_id
        final['Sender']=Sender
        final['Subject']=Subject
        final['Date']=Date
        final['Snippet']=Snippet
        final['Message_body']=Message_body
        final['formalinformal']=labels[0]
        listf.append(final)
    with open(os.path.join(module_dir,f'csvfile/{username}_finalformal.csv'), 'w', encoding='utf-8', newline = '') as csvfile:
        fieldnames = ['m_id','Sender','Subject','Date','Snippet','Message_body','formalinformal']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames, delimiter = ',')
        writer.writeheader()
        for val in listf:
            #print(val)
            writer.writerow(val)
    return f'csvfile/{username}_finalformal.csv'

def main():
    PCM_formalinformal("ayushbansal323")

if __name__ == '__main__':
    main()
