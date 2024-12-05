package exercise1;

public class Transaction implements Runnable{

	private Account acc; 
	private boolean type ;		// 0 : withdraw, 1 : deposit 
	private double amt ; 
	
	@Override
	public void run() {
		// TODO Auto-generated method stub
		if (type) {acc.deposit(amt);}
		else { acc.withdraw(amt);}
	}
	
	public Transaction(Account acc, boolean type, double amt) {
		this.acc= acc; 
		this.type= type; 
		this.amt= amt; 
	}
	
}
