package exercise1;

public class Account {
	private double balance ; 
	public Account (double initBal) 
	{
		this.balance= initBal ; 
		
	}
	public synchronized void deposit(double amt) 
	{
		if (amt>0)
		{
			balance += amt; 
			System.out.println("deposit amt: $"+amt);
			System.out.println("updated balance : $"+balance);
			
		}
	}
	public synchronized void withdraw(double amt) 
	{
		if (amt>0 && balance >=amt) {
			balance -= amt; 
			System.out.println("withdraw amt: $"+amt);
			System.out.println("updated amt : $"+balance);
			
		} else 
		{
			System.out.println("withdraw amt: $"+amt);
			System.out.println("withrawl amount exceeds account balance");
		}
	}
	public synchronized double getBalance() 
	{
		return balance ; 
	}
}
