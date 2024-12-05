package exercise1;
import java.util.ArrayList;
import java.util.List;
import java.util.concurrent.ExecutorService;
import java.util.concurrent.Executors;
import java.util.concurrent.TimeUnit;

public class AccountTest {

	public static void main(String[] args) {
        Account account = new Account(1000);

        // Create a list of transactions
        List<Transaction> trans = new ArrayList<>();
        trans.add(new Transaction(account, true, 500));   // Deposit
        trans.add(new Transaction(account, false, 200));  // Withdraw
        trans.add(new Transaction(account, true, 300));   // Deposit
        trans.add(new Transaction(account, false, 1500)); // Insufficient withdrawal
        trans.add(new Transaction(account, true, 700));   // Deposit

        // Create thread pool
        ExecutorService executor = Executors.newFixedThreadPool(5);

        // Execute transactions
        for (Transaction transaction : trans) {
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
        System.out.println("\nFinal Account Balance: $" + account.getBal());
    }
}
