# YpoxreotikiErgasia23_E20124_Papakonstantinou_Antonis

Παρακάτω θα αναλυθεί βήμα - βήμα όλη η εργασία. Αυτό το αρχείο περιγράφει λεπτομερώς (και με παραδείγματα εκτέλεσης) τις λειτουργίες του συστήματος, 
καθώς και το τρόπο με τον οποίο εκτελείται η υπηρεσία μας.

Όλη η εργασία έγινε σε windows 10 , οπότε οι εντολές που θα παρουσιαστούν παρακάτω αφορούν αποκλειστικά το συκγκεκριμένο λειτουργικό σύστημα.
                
#                                                        ΕΙΣΑΓΩΓΗ
                                                        
Στην πιο απλή της μορφή , η εργασία αυτή είναι η υλοποίηση διάφορων endpoints.

# Τι είναι τα endpoints?

Σε απλές λέξεις, ένα "endpoint" αναφέρεται σε ένα σημείο ή μια διαδρομή (URL) σε μια web εφαρμογή. Επίσης μπορεί να θεωρηθεί ως ένα API που μπορεί να κληθεί από έναν client.
Ένα endpoint ορίζει τον τρόπο πρόσβασης και τη λειτουργία που θα εκτελεστεί όταν καλεστεί από έναν client.

Σε ένα web API, τα endpoints αντιστοιχούν σε συγκεκριμένες λειτουργίες ή πόρους που η εφαρμογή παρέχει. 

- Για παράδειγμα, μια εφαρμογή που παρέχει υπηρεσία εγγραφής χρηστών μπορεί να έχει ένα endpoint με URL /register, όπου ο client μπορεί να κάνει μια αίτηση POST για να εγγραφεί ένας νέος χρήστης.

- Κάθε endpoint συνήθως έχει έναν συγκεκριμένο τύπο αιτήματος HTTP (όπως GET, POST, PUT, DELETE) και μπορεί να απαιτεί συγκεκριμένες παραμέτρους ή δεδομένα στο σώμα του αιτήματος. 

- Όταν ένας client καλεί ένα endpoint, η εφαρμογή λαμβάνει το αίτημα, εκτελεί την αντίστοιχη λειτουργία και επιστρέφει μια απάντηση (response) στον client.

- Τα endpoints αποτελούν τη δομή του API και ορίζουν τον τρόπο με τον οποίο οι clients μπορούν να αλληλεπιδρούν με την εφαρμογή ή την υπηρεσία που παρέχεται.


 #                                                       ΜΕΡΟΣ 1ο - ΤΑ ΒΉΜΑΤΑ ΠΡΙΝ ΤΗΝ ΥΛΟΠΟΙΗΣΗ ΤΟΥ ΚΑΘΕ EndPoint 
 
 - Ανοίγουμε ένα cmd και εκτελούμε τις εντολές:
      - pip install pymongo
      - pip install flask

![image](https://github.com/pantoine31/YpoxreotikiErgasia23_E20124_Papakonstantinou_Antonis/assets/85836153/ad2fa5b1-fda4-4473-ae47-9fb95a3aa524)

Οι εντολές "pip install pymongo" και "pip install flask" χρησιμοποιούνται για να εγκαταστήσουν τις αντίστοιχες βιβλιοθήκες στην Python. 
Ας εξηγήσουμε τι κάνει η κάθε μία από αυτές τις εντολές:

- "pip install pymongo": Αυτή η εντολή εγκαθιστά τη βιβλιοθήκη pymongo στο περιβάλλον Python μας. Το pymongo είναι ένα Python driver που επιτρέπει τη σύνδεση και την επικοινωνία με ένα MongoDB στην Python.
 Με αυτή τη βιβλιοθήκη, μπορούμε να δημιουργήσουμε, να διαγράψουμε, να ενημερώσουμε και να αναζητήσουμε δεδομένα σε ένα MongoDB.

- "pip install flask": Αυτή η εντολή εγκαθιστά τη βιβλιοθήκη Flask στο περιβάλλον Python μας. 
- Το Flask είναι ένα ελαφρύ και ευέλικτο πλαίσιο εφαρμογών για την ανάπτυξη web εφαρμογών στην Python. 
- Χρησιμοποιείται για τη δημιουργία διαδικτυακών εφαρμογών, RESTful υπηρεσιών και άλλων διαδικτυακών λειτουργιών. Το
-  Flask παρέχει ένα απλό και ευανάγνωστο συντακτικό, ενώ παράλληλα παρέχει τις απαραίτητες λειτουργίες για την ανάπτυξη πλήρως λειτουργικών εφαρμογών.

Συνολικά, οι δύο αυτές εντολές εγκαθιστούν τις απαραίτητες βιβλιοθήκες στην Python για να μπορέσουμε να χρησιμοποιήσουμε το pymongo και το Flask στα προγράμματά που θα αναπτύξουμε.

Στη συνέχεια:
       
- Ανοίγουμε ένα cmd και εκτελούμε την εντολή: docker pull mongo : 

      Η εντολή docker pull mongo χρησιμοποιείται για να κατεβάσει την εικόνα του MongoDB από το Docker Hub στον υπολογιστή μας.

      Ο Docker Hub είναι ένας δημόσιος κατάλογος εικόνων Docker όπου μπορούμε να βρούμε και να κατεβάσουμε προετοιμασμένες εικόνες (images) για διάφορες εφαρμογές και λογισμικά.

      Όταν εκτελέσουμε την εντολή docker pull mongo, το Docker θα ελέγξει το Docker Hub για την τελευταία έκδοση της εικόνας του MongoDB και θα την κατεβάσει στον υπολογιστή μας.
      Αυτό σημαίνει ότι μπορούμε να έχουμε πρόσβαση στην εικόνα (image) και να τη χρησιμοποιήσουμε για να δημιουργήσουμε και να εκτελέσουμε τα δικά μας containers βασισμένα στο MongoDB.
      
      
- Στην συνέχεια , στο cmd  εκτελούμε την εντολή: docker run -d -p 27017:27017 --name mongodb mongo : 

      Η εντολή docker run -d -p 27017:27017 --name mongodb mongo χρησιμοποιείται για να δημιουργήσει ένα container με το Image του MongoDB και να το εκτελέσει στο Docker environment μας. 
      
         Ας εξηγήσουμε τι κάνει η κάθε παράμετρος:

      -d: Αυτή η παράμετρος δηλώνει ότι ο container θα εκτελεστεί στο background (σε λειτουργία detach).
      
      -p 27017:27017: Αυτή η παράμετρος συνδέει τη θύρα 27017 του υπολογιστή μας με τη θύρα 27017 του container. Αυτό επιτρέπει την επικοινωνία με το MongoDB που εκτελείται μέσα στο container μέσω της θύρας 27017.
      
      --name mongodb: Αυτή η παράμετρος ορίζει ένα όνομα για το container που θα δημιουργηθεί. Στην περίπτωση αυτή, το όνομα είναι "mongodb".
      
      mongo: Αυτή είναι η εικόνα που θα χρησιμοποιηθεί για τη δημιουργία του container. 
      Συγκεκριμένα, εδώ χρησιμοποιείται η εικόνα του MongoDB.
      Με αυτήν την εντολή, θα δημιουργηθεί ένα container με την εικόνα του MongoDB και θα εκτελεστεί στο background. 
      Επίσης, η θύρα 27017 του υπολογιστή θα είναι συνδεδεμένη με τη θύρα 27017 του container, επιτρέποντας την επικοινωνία με το MongoDB που εκτελείται μέσα στο container. 
      Ο container θα έχει το όνομα "mongodb".
      
- Στην συνέχεια , εκτελούμε την εντολή: docker start mongodb :   

      Η εντολή docker start mongodb χρησιμοποιείται για να ξεκινήσει το container που δημιουργήσαμε στο προηγούμενο βήμα και έχει το όνομα "mongodb". 
      Αν ο container "mongodb" έχει τερματιστεί ή διακόπηκε, η εντολή docker start τον επανεκκινεί και τον εκτελεί ξανά.

      Επομένως, αν εκτελέσουμε την εντολή docker start mongodb, θα ξεκινήσουμε ξανά το container με το όνομα "mongodb" και θα θέσουμε την κατάσταση του σε εκτέλεση (running).  
      
- Στην συνέχεια , εκτελούμε την εντολή: docker exec -it mongodb mongosh :   

       Η εντολή docker exec -it mongodb mongosh χρησιμοποιείται για να εκτελέσει μια εντολή μέσα σε ένα εκτελούμενο container. 
       Συγκεκριμένα, η εντολή εκτελεί το πρόγραμμα mongosh μέσα στο container με όνομα "mongodb".

       Το mongosh είναι ένα εργαλείο γραμμής εντολών που παρέχεται από τη MongoDB και χρησιμοποιείται για τη διαχείριση και αλληλεπίδραση με μια MongoDB database.

       Με την εντολή docker exec -it mongodb mongosh,  έχουμε πρόσβαση στις λειτουργίες του mongosh και θα μπορούμε να εκτελέσουμε εντολές MongoDB για να αλληλεπιδράσουμε
       με τη βάση δεδομένων MongoDB που εκτελείται μέσα στο container.
       
       !!! Στην ουσία αυτή η εντολή , μας βάζει μέσα στη διαχείριση τον βάσεων !!!
       
 - Στην συνέχεια , εφόσον διαχειριζόμαστε τις διάφορες βάσεις, εκτελούμε την εντολή: use DigitalAirlines :       
 
          Η εντολή use DigitalAirlines χρησιμοποιείται μέσα σε ένα mongosh για να αλλάξoυμε την τρέχουσα βάση δεδομένων (database) που χρησιμοποιούμε για τη συνέχεια.

          Όταν εκτελούμε την εντολή use DigitalAirlines, το mongosh θα ενημερωθεί ότι η τρέχουσα βάση δεδομένων είναι η "DigitalAirlines" (Εμφανίζεται το μήνυμα: switched to db DigitalAirlines). 
          
          Αυτό σημαίνει ότι όλες οι επόμενες εντολές που εκτελούμε στο mongosh θα εφαρμοστούν στη βάση δεδομένων "DigitalAirlines". 
          
          Αν η βάση δεδομένων "DigitalAirlines" δεν υπάρχει, τότε θα δημιουργηθεί μια νέα βάση δεδομένων με αυτό το όνομα.

          Με την αλλαγή της τρέχουσας βάσης δεδομένων μέσω της εντολής use, μπορούμε να εκτελέσουμε εντολές για την προβολή και επεξεργασία των δεδομένων που ανήκουν στη συγκεκριμένη βάση δεδομένων "DigitalAirlines".
       
- Αφού , λοιπόν, αποκτήσαμε πρόσβαση στην βάση δεδομένων "DigitalAirlines" ήρθε η ώρα να δημιουργήσουμε τις συλλογές (collections) που απαιτούνται για την εργασία μας. 


# Τι είναι όμως τα collections σε μία βάση δεδομένων mongodb?


    Σε μια βάση δεδομένων MongoDB, τα "collections" αναφέρονται σε ομάδες έγγραφων που αποθηκεύονται μαζί. 
    Ας φανταστούμε τις συλλογές (collections) ως ένα ταμπλό σε έναν πίνακα βάσης δεδομένων, όπου κάθε συλλογή αντιπροσωπεύει μια κατηγορία ή έναν τύπο δεδομένων.

    Κάθε συλλογή αποτελείται από ένα σύνολο έγγραφων MongoDB που μπορεί να έχουν διαφορετική δομή, αλλά σχετίζονται με μια κοινή θεματική ή λογική ομάδα. 

    Για παράδειγμα, στη δική μας βάση δεδομένων για το σύστημα με τα εισιτήρια, θα υπάρχουν συλλογές για τους χρήστες, τις πτήσεις και τις κρατήσεις.

    Οι συλλογές στη MongoDB είναι αναλογικές με τους πίνακες σε συμβατικές σχεσιακές βάσεις δεδομένων.

    Κάθε συλλογή μπορεί να περιέχει πολλά έγγραφα, όπου κάθε έγγραφο αντιστοιχεί σε ένα εγγραφικό σειρά ή μια εγγραφή στον πίνακα. 

    Κάθε έγγραφο σε μια συλλογή είναι ένα JSON-επιπεδο κείμενο, το οποίο σημαίνει ότι μπορεί να έχει διαφορετική δομή από ένα άλλο έγγραφο στην ίδια συλλογή.

    Οι συλλογές στη MongoDB είναι ευέλικτες και δεν απαιτούν προκαθορισμένη δομή σαν τις συμβατικές σχεσιακές βάσεις δεδομένων. 

    Αυτό επιτρέπει την αποθήκευση δεδομένων με διαφορετική δομή στην ίδια συλλογή, επιτρέποντάς μας να έχουμε ευκολία και ευελιξία κατά την αποθήκευση και ανάκτηση των δεδομένων μας.


# Δημιουργία των 3 collections μας για την υλοποίηση της εργασίας
 
  - Δημιουργία collection για τα usernames:     ->  db.createCollection("usernames")
  - Δημιουργία collection για τα flights:       ->  db.createCollection("flights")
  - Δημιουργία collection για τα reservations:  ->  db.createCollection("rsv")


- Από εδώ και πέρα είμαστε έτοιμοι να ξεκινήσουμε τον σχεδιασμό και τον προγραμματισμό κάθε endpoint. Όλα αυτά θα αναλυθούν παρακάτω με τη σειρά.

# Ένα άλλο εργαλείο που θα χρησιμοποιήσουμε στην εργασία μας είναι το postman. 
# Τι είναι όμως το Postman και πως λειτουργεί;

- Το Postman είναι ένα πρόγραμμα ανάπτυξης API που χρησιμοποιείται για την δοκιμή, την αποσφαλμάτωση και την τεκμηρίωση των APIs. 
 
- Αρχικά, δημιουργήθηκε ως μια επέκταση για τον περιηγητή Chrome, αλλά τώρα είναι διαθέσιμο και ως αυτόνομη εφαρμογή για Windows, macOS και Linux.

- Το Postman μας επιτρέπει να κατασκευάσουμε HTTP αιτήματα (όπως GET, POST, PUT, DELETE κ.λπ.) σε διάφορες μορφές όπως JSON ή XML, και να τις στείλουμε σε έναν διακομιστή (server) για να αλληλεπιδράσουμε με το API. 
 
- Μπορούμε να ορίσουμε διάφορες παραμέτρους, επικεφαλίδες, σώματα αιτήσεων και να εξετάσουμε τις απαντήσεις για να ελέγξουμε τη σωστή λειτουργία του API μας.

- Με το Postman μπορούμε να αποσφαλματώσουμε τα APIs μας πριν την ενσωμάτωσή τους στις εφαρμογές μας, εξοικονομώντας χρόνο και αποφεύγοντας πιθανά σφάλματα. 

- Συνολικά, το Postman προσφέρει ένα πλήρες περιβάλλον για τη διαχείριση και τη δοκιμή των API, καθιστώντας τον εύκολο για τους προγραμματιστές να επικοινωνούν με υπηρεσίες και να αναπτύσσουν τις δικές τους εφαρμογές.



# Βήματα για την χρήση του postman στη δική μου εργασία
- Θα γίνει η επεξήγηση του endpoint για το /register. Όλα τα υπόλοιπα ακολουθούν την ίδια λογική , και για εξοικονόμηση χρόνου- χώρου θα γίνει η επέξηγηση μόνο για το 1.

  - Βήμα 1: Καταβάζουμε την εφαρμογή του Postman από εδώ: https://www.postman.com/downloads/ Μόλις κατέβει , δεν χρειάζεται κάποια εγγραφή , προχωράμε χωρίς εγγραφή στο πρόγραμμα.

  - Βήμα 2: Πάνω - Πάνω μας έχει μία μπάρα η οποία δέχεται URL's καθώς και το αντίστοιχο αίτημα. Τρέχουμε λοιπόν το αρχείο μας infoSys , είτε με διπλό κλικ , είτε με την εντολή python infoSys.py , σε κάποιο cmd.

  - Βήμα 3: Μόλις το τρέξουμε θα μας εμφανίσει το αντίστοιχο μήνυμα: 

![image](https://github.com/pantoine31/YpoxreotikiErgasia23_E20124_Papakonstantinou_Antonis/assets/85836153/f35a1a1d-7fa5-40f7-9b7a-667e23752157)
                               
  - Βήμα 4: Παίρνουμε το url http://127.0.0.1:5000 και το τοποθετούμε στην μπάρα αναζήτησης του postman ως εξής: http://127.0.0.1:5000/register


  - Βήμα 5: !!!ΠΡΟΣΟΧΗ!!! Στο body του postman πρέπει να είναι raw καθώς και ο τύπος αρχείου JSON - και για το συγκεκριμένο παράδειγμα το method είναι POST.


  - Βήμα 6: Αφού είμαστε έτοιμοι να δοκιμάσουμε το endpoint του /register θα περάσουμε τα δεδομένα μας με τον εξής τρόπο με το ακόλουθο JSON αρχείο και πατάμε SEND:

          {
            "username": "antonhspap",
            "last_name": "doe",
            "email": "antonis@example.com",
            "password": "password123",
            "date_of_birth": "2002-01-03",
            "country": "London",
            "passport_number": "ABCD1244"
           }

# Από εδώ και στο εξής έχουμε τις ακόλουθες περιπτώσεις:

1) Εφόσον πάνε όλα καλά θα μας εμφανίστεί το ακόλουθο μήνυμα:

            {
                "New user has user_id": "6483553f7c30ffff318f90e9",
                "message": "A new user has been successfully registered! Welcome to our family!"
            }
        
        
2) Αν ο χρήστης που πάμε να προσθέσουμε έχει το ίδιο email με κάποιον άλλον χρήστη τότε μας εμφανίζεται το ακόλουθο μήνυμα όταν πατάμε SEND:

            {
                "Message": "User with the same email already exists. Try for an other email."
            }

3) Αν ο χρήστης που πάμε να προσθέσουμε έχει το ίδιο username με κάποιον άλλον χρήστη τότε μας εμφανίζεται το ακόλουθο μήνυμα όταν πατάμε SEND:


            {
                "Message": "Username is already in Use. Try with an other Username."
            }


# Για του λόγου το αληθές:

      - Εκτελούμε αμέσως την εντολή db.usernames.find({}) μέσα στη βάση DigitalAirlines στο cmd μας. 
      Θα δούμε τον χρήστη antonhspap ακριβώς όπως τον περάσαμε λίγο παραπάνω , δηλαδή:
  
  ![image](https://github.com/pantoine31/YpoxreotikiErgasia23_E20124_Papakonstantinou_Antonis/assets/85836153/7f9b198a-ccb4-4dfa-83c4-831c5df02c12)

      - Αν πάμε να ξαναπροσθέσουμε τον ίδιο χρήστη , τότε:
       (Βγάζει error για το ίδιο email καθώς στον κώδικα το email ελέγχεται για το εάν υπάρχει , πρώτο)
       
   ![image](https://github.com/pantoine31/YpoxreotikiErgasia23_E20124_Papakonstantinou_Antonis/assets/85836153/e2eddb09-bdcc-4442-b404-07ad0fe41a1f)






#                                                     EndPoints for ADMIN ONLY

- Ο admin έχει δηλωθεί στο σύστημα μας και δεν χρειάζεται να κάνει register. Τα στοιχεία του ADMIN είναι:

    ![image](https://github.com/pantoine31/YpoxreotikiErgasia23_E20124_Papakonstantinou_Antonis/assets/85836153/d4309f2f-fbde-4a3b-971f-44c29210e6db)

 - Ο ADMIN έχει στα ακόλουθα endpoionts πρόσβαση:

![image](https://github.com/pantoine31/YpoxreotikiErgasia23_E20124_Papakonstantinou_Antonis/assets/85836153/da49f370-f54b-4581-a41f-44225e08ad6d)

# ΚΑΘΕ φορά που κάποιος δεν είναι ADMIN ή δεν έχει προηγηθεί login as ADMIN - και προσπαθεί να μπει στα παραπάνω endpoints- εμφανίζεται το αντίστοιχο μήνυμα:

![image](https://github.com/pantoine31/YpoxreotikiErgasia23_E20124_Papakonstantinou_Antonis/assets/85836153/b157526c-eb6b-4612-9add-78424ca63fd9)


#                                                     EndPoints for USER ONLY
- Ο απλός user πριν κάνει login στο σύστημα μας , χρειάζεται να κάνει register. Ένας απλός user , αφού κάνει register , εφόσον ακολουθήσει το endpoint του login , έχει πρόσβαση στα ακόλουθα endpoints:
  
![image](https://github.com/pantoine31/YpoxreotikiErgasia23_E20124_Papakonstantinou_Antonis/assets/85836153/20cc50ce-6ba9-4eeb-9fa6-b0cc6bcdf758)


# ΚΑΘΕ φορά που κάποιος δεν είναι USER ή δεν έχει προηγηθεί login/register as USER - και προσπαθεί να μπει στα παραπάνω endpoints- εμφανίζεται το αντίστοιχο μήνυμα:

![image](https://github.com/pantoine31/YpoxreotikiErgasia23_E20124_Papakonstantinou_Antonis/assets/85836153/58d46f93-e542-4708-8ce7-2c93674cda6f)



#                                                     EndPoints for ADMIN ONLY

# 1) Endpoint /create 
-> Δημιουργία νέας πτήσης από τον admin:
   Εδώ παρατηρούμε πως φτιάχνουμε στο postman το flight μας και μετά μέσω cmd βλέπουμε πως το flight έχει δημιουργηθεί κανονικά:

   ![image](https://github.com/pantoine31/YpoxreotikiErgasia23_E20124_Papakonstantinou_Antonis/assets/85836153/f41ef3f0-ac3a-4ac3-8cfb-81032aed5d9a)
# 2) Endpoint /price 
-> Ανανέωση τιμών μίας πτήσης από τον admin βάση του id της πτήσης:
   Εδώ παρατηρούμε πως στο postman , αφού βάλουμε το /price που είναι το endpoint μας, πρέπει να βάλουμε και /id_flight. 
   Παραθέτω την αλλαγή του flight με id 6491bee21d99d41bd1bd5e79. 
   Τα price από 85 και 600 αλλάζουν σε 19 και 21:
   
   ΠΡΙΝ την αλλαγή:

   ![image](https://github.com/pantoine31/YpoxreotikiErgasia23_E20124_Papakonstantinou_Antonis/assets/85836153/08b38c0f-56f6-407d-9f44-bc53dbba6fa8)

   ΜΕΤΑ την αλλαγή:

   ![image](https://github.com/pantoine31/YpoxreotikiErgasia23_E20124_Papakonstantinou_Antonis/assets/85836153/ac528b00-f9b1-4246-b0c3-725854e7a24f)
# 3) Endpoint /searchFlights
-> Αναζήτηση πτήσεων από τον admin βάση: 
  - Αεροδρόμιο προέλευσης και αεροδρόμιο τελικού προορισμού
  - Αεροδρόμιο προέλευσης, αεροδρόμιο τελικού προορισμού και ημερομηνία διεξαγωγής
  - Ανά ημερομηνία
  - Εμφάνιση όλων των διαθέσιμων πτήσεων

   Εδώ παρατηρούμε πως στο postman , αφού βάλουμε το /searchFlights που είναι το endpoint μας, πρέπει να βάλουμε και το τρόπο που θέλουμε να αναζητήσουμε.
   Έστω ότι αναζητούμε με Αεροδρόμιο προέλευσης και αεροδρόμιο τελικού προορισμού.
   Βλέπουμε πως στο collection flights , μεταξύ άλλων , υπάρχει και η πτήση από parisi προς ellada:

   ![image](https://github.com/pantoine31/YpoxreotikiErgasia23_E20124_Papakonstantinou_Antonis/assets/85836153/1a80c865-639b-40b4-8e49-32a5c948c156)

   Κάνουμε την αναζήτηση στο postman και βλέπουμε ότι:

   ![image](https://github.com/pantoine31/YpoxreotikiErgasia23_E20124_Papakonstantinou_Antonis/assets/85836153/293183b5-47b1-4cbd-a701-37a3431f7b0a)

  !Σημείωση!
  Για την εμφάνιση ΟΛΩΝ των διαθέσιμων πτήσεων εκτελούμε στο postman το ακόλουθο:

  ![image](https://github.com/pantoine31/YpoxreotikiErgasia23_E20124_Papakonstantinou_Antonis/assets/85836153/4666deb9-61b1-49eb-87ac-c35041f0b8bb)

  Αυτό γιατί όταν κανένα από τα πεδία airportFrom, airportTo και flightDate δεν έχει συμπληρωθεί, η συνθήκη είναι αληθής και θα επιστραφούν όλες οι πτήσεις που υπάρχουν στη συλλογή.

 # 4) Endpoint 

   

