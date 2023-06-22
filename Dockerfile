# Βήμα 1: Βάση εικόνας
FROM python:3.9

# Βήμα 2: Εργαστεία
WORKDIR /app

# Βήμα 3: Αντιγραφή απαραίτητων αρχείων στον εσωτερικό φάκελο του container
COPY infoSys.py .

# Βήμα 4: Εγκατάσταση απαιτούμενων εξαρτημάτων
RUN pip install flask

# Βήμα 5: Αποκαλυπτήρια της πόρτας που χρησιμοποιείται από το web service
EXPOSE 5000

# Βήμα 6: Εκτέλεση του web service κατά την έναρξη του container
CMD ["python", "infoSys.py"]
