package exercise1;

public class Transaction implements Runnable 
{
	private Account acc; 
	private boolean type ; // 0 for withdraw, 1 for deposit 
	private double amt ;
	public Transaction (Account acc, boolean type, double amt) 
	{
		this.acc= acc; 
		this.type= type; 
		this.amt= amt; 
	}
	
	@Override 
	public void run () {
		if (type) acc.deposit(amt);		// deposit 
		else acc.withdraw(amt);			// withdraw 
	}
	
}
