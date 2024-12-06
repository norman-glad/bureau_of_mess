package exercise1;

import java.util.ArrayList;
import java.util.List;
import java.util.concurrent.ExecutorService;
import java.util.concurrent.Executors;
import java.util.concurrent.TimeUnit;

public class AccountTest {

	public static void main(String[] args) {

		Account acc = new Account (777);
		
		List<Transaction> Trans = new ArrayList<>(); 
		Trans.add(new Transaction(acc, true, 999));   // Deposit
		Trans.add(new Transaction(acc, true, 888));  
		Trans.add(new Transaction(acc, true, 777));   // Insufficient withdrawal
		Trans.add(new Transaction(acc, false, 666));  // Withdraw 
		Trans.add(new Transaction(acc, false, 555)); 

		 ExecutorService executor = Executors.newFixedThreadPool(5);

	        // Execute transactions
	        for (Transaction transaction : Trans) {
	            executor.execute(transaction);
	        }

	        // Shutdown executor
	        executor.shutdown();

	        // Wait for all threads to complete
	        try {
	            executor.awaitTermination(5, TimeUnit.SECONDS);
	        } catch (InterruptedException e) {
	            e.printStackTrace();
	        }

	        // Print final balance
	        System.out.println("\nFinal Account Balance: $" + acc.getBalance());
	}

}
