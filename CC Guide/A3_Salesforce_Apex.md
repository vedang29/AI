# Assignment A3: Salesforce Apex

### Step 1: Login to Salesforce

1. Go to the Salesforce login page:
   - [Salesforce Login](https://login.salesforce.com/?locale=in)

### Step 2: Create "User" Class

1. Click on the **gear icon** and go to **Developer Console**.
2. Go to **File > New > Apex Class** and create a new class named `user`.
3. Paste the following code into the class:

   ```java
   public class user {
       public static void createAccount(String accountName) {
           // Create a new Account instance
           Account newAccount = new Account(); 
           newAccount.Name = accountName;
   
           // Insert the Account into the database
           try {
               insert newAccount;
               System.debug('Account created with Id: ' + newAccount.Id);
           } catch (DmlException e) {
               System.debug('Error creating account: ' + e.getMessage());
           }
       }
   }

4. Press Ctrl + E to save.

5. Click on Execute to run the code.

### Step 3: View Newly Created Users
1. Click on the left menu icon.

2. Click on View All.

3. Scroll down and go to Accounts.

4. Edit the newly created users and perform deletion if needed.